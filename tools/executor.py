import subprocess
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Any
import sys
sys.path.append("..")

@dataclass
class TestResult:
    args: List[str]
    stdin: str
    expected_stdout: str
    stdout: str
    stderr: str
    exit_code: int
    passed: bool

class Executor:
    """
    Runs all tests in tests/{task_name}/:
      - test_1.txt  → stdin for test #1
      - sol_1.txt   → expected stdout for test #1
      - etc.
    """
    def __init__(
        self,
        executable: Path = None,
        args: Optional[Any] = None,
        tests_root: Path = Path("tests")
    ):
        self.executable = executable
        self.args = args
        self.task_name = getattr(args, "task_name", None)
        if not self.task_name:
            raise ValueError("Executor needs args.task_name to locate tests")
        
        # Discover and load all (stdin, expected) pairs
        test_dir = tests_root / self.task_name
        if not test_dir.is_dir():
            raise FileNotFoundError(f"No tests folder at {test_dir}")
        
        self.tests: List[tuple[str,str]] = []
        # Look for test_*.txt and sol_*.txt pairs
        for test_file in sorted(test_dir.glob("test_*.txt")):
            idx = test_file.stem.split("_", 1)[1]   # e.g. "1", "2", ...
            sol_file = test_dir / f"sol_{idx}.txt"
            if not sol_file.exists():
                logging.warning("Missing solution file for %s", test_file)
                continue
            
            stdin_data = test_file.read_text()
            expected = sol_file.read_text()
            self.tests.append((stdin_data, expected))
        
        self.results: List[TestResult] = []
    
    def set_executable_path(self, executable):
        self.executable = executable

    def run_test(self, stdin_data: str, expected_stdout: str) -> TestResult:
        cmd = [str(self.executable)]
        logging.info("Running %s with stdin length %d", cmd, len(stdin_data))
        proc = subprocess.run(
            cmd,
            input=stdin_data,
            capture_output=True,
            text=True
        )
        # Compare exact match (you may want to .strip() both sides)
        passed = (proc.returncode == 0 and proc.stdout.strip() == expected_stdout.strip())
        return TestResult(
            args=cmd,
            stdin=stdin_data,
            expected_stdout=expected_stdout.strip(),
            stdout=proc.stdout.strip(),
            stderr=proc.stderr.strip(),
            exit_code=proc.returncode,
            passed=passed
        )

    def run_all(self):
        """
        Execute every loaded test, store TestResult in self.results,
        and return (num_passed, total_tests).
        """
        self.results.clear()
        for stdin_data, expected in self.tests:
            res = self.run_test(stdin_data, expected)
            self.results.append(res)
        
        passed = sum(1 for r in self.results if r.passed)
        total  = len(self.results)
        logging.info("Executor: %d/%d tests passed", passed, total)
        return passed, total, self.results

class Args:
    def __init__(self, task_name):
        self.task_name = task_name

if __name__ == "__main__":
    args = Args(task_name="task_add")
    tests_root = Path("../tests")
    executor = Executor(executable="/home/anon/Documents/Code/Project/LLM-CKKS-Benchmark/references/build/task_add", args=args, tests_root=tests_root)

    passed, total, results = executor.run_all()

    breakpoint()
