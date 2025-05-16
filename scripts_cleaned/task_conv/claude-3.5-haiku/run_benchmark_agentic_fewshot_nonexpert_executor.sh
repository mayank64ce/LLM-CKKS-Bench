#!/bin/bash

num_runs=5
task="task_conv"

for run_id in $(seq 1 $num_runs); do
    echo "Running Claude-3-5-Haiku with run ID: $run_id"

    # Create the directory for this run to ensure it exists
    mkdir -p logs_agentic_fewshot_nonexpert_executor/$task/claude-3.5-haiku/$run_id # change the folder and model here

    python scripts_cleaned/run_benchmark_agentic_fewshot_nonexpert_executor.py \
        --model_name "Claude-3-5-Haiku" \
        --task_name $task \
        --run_id $run_id \
        --max_steps 10 \
        --save_dir "logs_agentic_fewshot_nonexpert_executor" 2>&1 | tee logs_agentic_fewshot_nonexpert_executor/$task/claude-3.5-haiku/$run_id/result.log # change the folder and model here

    sleep $((RANDOM % 10 + 1))
done