
# Transformers example

This example demonstrates how to execute a standard deep learning training pipeline using the transformers library on one of the GPU nodes in the cluster. It is assumed that you already have access and know how to log in.

## 0. Git clone the guides repo with the examples

To facilitate the demonstration, we have prepared the necessary code and scripts in a repository. Your task is to run the code and then delve into it to understand the details more thoroughly.

```bash
$ git clone https://github.com/ieeta-pt/HPC-guides.git
$ cd HPC-guides/examples/transformers
```

## 1. Preprare the environment

The first step is to prepare the development environment. This involves loading Python, creating a virtual environment, and installing the dependencies.

```bash
$ module load python
$ python -m venv virtual-venv
$ source virtual-venv/bin/activate
(virtual-venv)$ pip install --upgrade pip
(virtual-venv)$ pip install transformers accelerate evaluate datasets scikit-learn
```

## 2. Submit the job

The hf_classification_trainer.py file contains the essential code needed to train a BERT base model for a classification task using the Yelp dataset. hf_trainer.sh is the launch script that includes SBATCH directives for acquiring resources. Specifically, we are requesting one A6000 GPU (--gres=gpu:nvidia-rtx-a6000:1).

```bash
(virtual-venv)$ sbatch hf_trainer.sh
Submitted batch job 95
```

After submitting the job, you can check its status in the queue by running squeue:

```bash
$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                94       gpu hf_train tiagoalm  R       0:02      1 dl-srv-03
```

Here you can see that your job (94) is running (ST = R) and has been allocated to the node dl-srv-03, which contains the A6000 GPU.

To monitor the progress of your training, inspect the output file specified in the launch script:

```bash
$ cat hf_trainer-94.out 
Job Information for Job ID: 94 from tiagoalmeida
------------ ------------
Account: students
CPUs per Node: 4
GPU: NVIDIA RTX A6000
Partition: gpu
QOS: normal
Start Time: 2024-07-05 15:12:29 UTC
Running On Node: dl-srv-03
------------ ------------
/var/lib/slurm-llnl/slurmd/job00094/slurm_script: line 9: virtual-venv/bin/activate: No such file or directory
User can use the local tmp dir /tmp/slurm-tiagoalmeida-94
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-cased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
amout of GPU memory 51033931776
BATCH SIZE 60
 33%|███▎      | 17/51 [00:26<00:34,  1.01s/i{'eval_loss': 1.6087651252746582, 'eval_accuracy': 0.257, 'eval_runtime': 6.7322, 'eval_samples_per_second': 148.539, 'eval_steps_per_second': 1.337, 'epoch': 1.0}
 43%|████▎     | 22/51 [00:51<01:27,  3.02s/it]
```
