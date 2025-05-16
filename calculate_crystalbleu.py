import os
import re
from collections import Counter
from nltk.util import ngrams
from pygments import lex
from pygments.lexers.c_cpp import CLexer
from pygments.token import Comment
from crystalbleu import corpus_bleu
from nltk.translate.bleu_score import SmoothingFunction

# Tokenization Function (Excludes Comments)
def tokenize_code(code):
    lexer = CLexer()
    return [
        token[1] for token in lexer.get_tokens(code)
        if not (re.fullmatch(r'\s+', token[1]) or token[0] in Comment)
    ]

# Function to Calculate Trivially Shared N-grams
def get_trivially_shared_ngrams(ref_tokens, gen_tokens, k=50):
    combined_tokens = ref_tokens + gen_tokens
    all_ngrams = []
    for n in range(3, 5):  # Focus on 3-grams and 4-grams
        all_ngrams.extend(list(ngrams(combined_tokens, n)))
    frequencies = Counter(all_ngrams)
    return dict(frequencies.most_common(k))

# Function to Compute CrystalBLEU Score
def compute_crystalbleu(reference_code, generated_code, k=50):
    ref_tokens = tokenize_code(reference_code)
    gen_tokens = tokenize_code(generated_code)
    
    trivially_shared_ngrams = get_trivially_shared_ngrams(ref_tokens, gen_tokens, k)
    
    smoothing = SmoothingFunction().method1
    score = corpus_bleu(
        [[ref_tokens]], 
        [gen_tokens],
        ignoring=trivially_shared_ngrams,
        smoothing_function=smoothing
    )
    return score


# Paths
# logs_dir = 'logs_agentic_rag_tag_executor'
references_dir = 'references'

log_dir_list = [
    "logs_agentic_rag_tag_executor",
    "logs_agentic_fewshot_expert_executor",
    "logs_agentic_fewshot_nonexpert_executor",
    "logs_agentic_executor",
    "logs_rag_tag_executor",
    "logs_fewshot_expert_executor",
    "logs_fewshot_nonexpert_executor",
    "logs_executor",

]

# Iterate over tasks first
def call(logs_dir):
    for task_name in os.listdir(logs_dir):
        task_path = os.path.join(logs_dir, task_name)
        if not os.path.isdir(task_path):
            continue

        # Load the reference for this task
        reference_file = os.path.join(references_dir, f"{task_name}.cpp")
        if not os.path.exists(reference_file):
            print(f"[WARN] Reference not found for task {task_name}")
            continue

        with open(reference_file, 'r') as ref_f:
            reference_code = ref_f.read()

        # Under each task, iterate over models
        for model_name in os.listdir(task_path):
            model_path = os.path.join(task_path, model_name)
            if not os.path.isdir(model_path):
                continue

            # Now each run under model
            for run_id in os.listdir(model_path):
                run_path = os.path.join(model_path, run_id)
                if not os.path.isdir(run_path):
                    continue

                # Your generated file is always named solution.cpp
                generated_file = os.path.join(run_path, 'solution.cpp')
                report_file    = os.path.join(run_path, 'crystalbleu.log')

                if not os.path.exists(generated_file):
                    print(f"[WARN] solution.cpp not found in {run_path}")
                    continue

                with open(generated_file, 'r') as gen_f:
                    generated_code = gen_f.read()

                # Compute CrystalBLEU
                score = compute_crystalbleu(reference_code, generated_code, k=50)

                # Save Report
                with open(report_file, 'w') as report_f:
                    report_f.write(f"CrystalBLEU Score: {score:.6f}\n")

                print(f"Task={task_name}  Model={model_name}  Run={run_id}  → CrystalBLEU = {score:.6f}")

if __name__ == "__main__":
    for logs_dir in log_dir_list:
        call(logs_dir)