num_runs=5
task="task_matmul"

for run_id in $(seq 1 $num_runs); do
    echo "Running Claude-3-5-Haiku with run ID: $run_id"
    python scripts_cleaned/run_benchmark_executor.py \
        --model_name "Claude-3-5-Haiku" \
        --task_name $task \
        --run_id $run_id \
        --max_steps 10 \
        --save_dir "logs_executor"
done