# Quick start

In this page you can find a quick start guide on how to use IEETA cluster (Pleiades). 

## 1. Access IEETA cluster (Pleiades)

Access the cluster via SSH using the credentials provided to you by email. If you do not have access yet, please refer to the `how_to_access.md` page.

```bash
$ ssh user@pleiades.ieeta.pt
```

By default, upon logging in, you will land on our **login** node in your home directory, which is located at `/data/home`. This is a network storage partition visible to all cluster nodes.

The **login** node is where you should prepare your code in order to submit jobs to run on the **worker** nodes of the cluster. The worker nodes are equipped with powerful resources. Currently, we have:

- **CPU nodes**: Nodes with a high amount of RAM and faster CPUs. *Currently not added to the cluster yet*
- **GPU nodes**: Nodes equipped with GPUs and more modest CPU/RAM configurations.

For more information about each node check the [nodes page](detail_material/nodes.md).

## 2. Prepare your software environment

The next step is to prepare your environment to run/build your application. We recommend using a virtual environment so that you can install any package locally. First, load the Python module.

```bash
$ module load python
```
Then create and activate your virtual environment.

```bash
$ python -m venv virtual-venv
$ source virtual-venv/bin/activate
```
You can then install your package dependencies with pip.
```bash
(virtual-venv)$ pip install --upgrade pip
(virtual-venv)$ pip install torch transformers
```

## 3. Create your SLURM job script

After setting up your runtime environment, you should create a SLURM job script to submit your job. For example:

```bash
#!/bin/bash
#SBATCH --job-name=trainer                # create a short name for your job
#SBATCH --output="trainer-%j.out"         # %j will be replaced by the slurm jobID
#SBATCH --nodes=1                         # node count
#SBATCH --ntasks=1                        # total number of tasks across all nodes
#SBATCH --cpus-per-task=2                 # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --gres=gpu:1                      # number of gpus per node
#SBATCH --mem=4G                          # Total amount of RAM requested

source /virtual-venv/bin/activate # If you have your venv activated when you submit the job, then you do not need to activate/deactivate

python your_trainer_script.py

deactivate
```
The script is made of two parts:
1. Specification of the resources needed and some job information;
2. Comands that will be executed on the destination node.

As an example, in the first part of the script, we define the job name, the output file and the requested resources (1 GPU, 2 CPUs and 4GB RAM). Then, in the second part, we define the tasks of the job.

By default since no partition was defined the job will run under the default partitaion that in this cluster is the gpu partition, you can check which partitions and nodes are available with:

```bash
  $ sinfo
```

## 4. Submit the job

To submit the job, you should run the following command:

```bash
$ sbatch script_trainer.sh
Submitted batch job 144
```
You can check the job status using the following command:

```bash
$ squeue
```
