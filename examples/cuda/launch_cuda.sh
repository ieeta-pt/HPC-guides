#!/bin/bash
#SBATCH --job-name=Cuda                   # create a short name for your job
#SBATCH --output="Cuda-%j.out" # %j will be replaced by the slurm jobID
#SBATCH --nodes=1                         # node count
#SBATCH --ntasks=1                        # total number of tasks across all nodes
#SBATCH --cpus-per-task=2                 # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --gres=gpu:1                      # number of gpus per node
#SBATCH --partition=gpu                   # Partition where job will be submitted

# run the compiled binary
./vector_addition
