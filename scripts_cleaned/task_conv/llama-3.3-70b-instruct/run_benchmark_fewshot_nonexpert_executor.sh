num_runs=5
task="task_conv"

for run_id in $(seq 1 $num_runs); do
    echo "Running Llama3-3-70b with run ID: $run_id"
    python scripts_cleaned/run_benchmark_fewshot_nonexpert_executor.py \
        --model_name "Llama3-3-70b" \
        --task_name $task \
        --run_id $run_id \
        --max_steps 10 \
        --save_dir "logs_fewshot_nonexpert_executor"
done