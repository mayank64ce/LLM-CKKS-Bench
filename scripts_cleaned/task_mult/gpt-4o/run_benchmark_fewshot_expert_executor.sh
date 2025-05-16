num_runs=5
task="task_mult"

for run_id in $(seq 1 $num_runs); do
    echo "Running GPT-4o with run ID: $run_id"
    python scripts_cleaned/run_benchmark_fewshot_expert_executor.py \
        --model_name "GPT-4o" \
        --task_name $task \
        --run_id $run_id \
        --max_steps 10 \
        --save_dir "logs_fewshot_expert_executor"
done