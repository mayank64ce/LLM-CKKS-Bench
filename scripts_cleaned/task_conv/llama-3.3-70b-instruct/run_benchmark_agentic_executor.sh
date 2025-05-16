#!/bin/bash

num_runs=5
task="task_conv" # change the task here

for run_id in $(seq 1 $num_runs); do
    echo "Running Llama3-3-70b with run ID: $run_id"

    # Create the directory for this run to ensure it exists
    mkdir -p logs_agentic_executor/$task/llama-3.3-70b-instruct/$run_id # change the folder and model here

    python scripts_cleaned/run_benchmark_agentic_executor.py \
        --model_name "Llama3-3-70b" \
        --task_name $task \
        --run_id $run_id \
        --max_steps 10 \
        --save_dir "logs_agentic_executor" 2>&1 | tee logs_agentic_executor/$task/llama-3.3-70b-instruct/$run_id/result.log # change the folder and model here

    sleep $((RANDOM % 10 + 1))
done