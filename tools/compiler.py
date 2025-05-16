import subprocess
import os
import shutil
import logging

class Compiler:
    def __init__(self, source_dir=None, build_dir='build', preload_file=None, args=None):
        """
        :param source_dir: Path to the directory containing the CMakeLists.txt
        :param build_dir: Path to the directory where build files will go
        :param preload_file: Optional CMake preload file (e.g., toolchain or OpenFHE config)
        """
            
        self.preload_file = preload_file
        self.args = args

        if source_dir:
            self.set_directory(source_dir, build_dir)
    
    def set_directory(self, source_dir=None, build_dir="build"):
        """
        Set the source and build directories.
        """
        # breakpoint()
        if source_dir:
            self.source_dir = os.path.abspath(source_dir)
        if build_dir:
            if os.path.isabs(build_dir):
                self.build_dir = build_dir
            else:
                self.build_dir = os.path.join(self.source_dir, build_dir)

        # Ensure the build directory exists and is clean
        if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)
        os.makedirs(self.build_dir, exist_ok=True)

        self.copy_requirements()

        self.preload_file = os.path.join(self.source_dir, self.preload_file) if self.preload_file else None
    
    def copy_requirements(self):
        """
        Copies files from the 'compiler_requirements' folder to the source directory.
        """
        requirements_dir = os.path.join(os.path.dirname(__file__), "compiler_requirements")
        if not os.path.exists(requirements_dir):
            logging.warning(f"Requirements directory '{requirements_dir}' does not exist.")
            return

        for item in os.listdir(requirements_dir):
            source_path = os.path.join(requirements_dir, item)
            dest_path = os.path.join(self.source_dir, item)

            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy2(source_path, dest_path)
    
    def configure(self):
        cmd = ['cmake', self.source_dir]

        if self.preload_file:
            preload_path = os.path.abspath(self.preload_file)
            cmd.extend(['-C', preload_path])

        print("[CMake Configure] Running:", ' '.join(cmd))
        result = subprocess.run(cmd, cwd=self.build_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            logging.info("❌ Configuration failed:\n")
        else:
            logging.info("✅ Configuration succeeded.")

        return result

    def build(self, target=None):
        cmd = ['cmake', '--build', '.']
        if target:
            cmd.extend(['--target', target])

        print("[CMake Build] Running:", ' '.join(cmd))
        result = subprocess.run(cmd, cwd=self.build_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            logging.info("❌ Build failed:\n")
        else:
            logging.info("✅ Build succeeded.")

        return result

    def compile(self, target=None):
        if not self.configure():
            return False
        return self.build(target)


if __name__ == "__main__":
    source_dir = '/home/anon/Documents/Code/Project/ckks-comp-test'
    compiler = Compiler(source_dir=source_dir, build_dir='build', preload_file='PreLoad.cmake')
    result = compiler.compile()
    breakpoint()