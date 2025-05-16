#!/bin/bash

num_runs=5
task="task_add"

for run_id in $(seq 1 $num_runs); do
    echo "Running GPT-4o with run ID: $run_id"

    # Create the directory for this run to ensure it exists
    mkdir -p logs_agentic_rag_tag_executor/$task/gpt-4o/$run_id # change the folder and model here

    python scripts_cleaned/run_benchmark_agentic_rag_tag_executor.py \
        --model_name "GPT-4o" \
        --task_name $task \
        --run_id $run_id \
        --max_steps 10 \
        --save_dir "logs_agentic_rag_tag_executor" 2>&1 | tee logs_agentic_rag_tag_executor/$task/gpt-4o/$run_id/result.log # change the folder and model here

    sleep $((RANDOM % 10 + 1))
done