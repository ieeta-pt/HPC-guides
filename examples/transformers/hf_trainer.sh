#!/bin/bash
#SBATCH --job-name=hf_trainer                   # create a short name for your job
#SBATCH --output="hf_trainer-%j.out" # %j will be replaced by the slurm jobID
#SBATCH --nodes=1                         # node count
#SBATCH --ntasks=1                        # total number of tasks across all nodes
#SBATCH --cpus-per-task=4                 # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --gres=gpu:nvidia-rtx-a6000:1                      # number of gpus per node
#SBATCH --mem-per-cpu=2G
source virtual-venv/bin/activate

echo "User can use the local tmp dir $TMPDIR"

python hf_classification_trainer.py 

deactivate
