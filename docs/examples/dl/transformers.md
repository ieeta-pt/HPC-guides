
# Cuda example

This example shows how you can run a normal dl training pipelie with the transformers library on one of the clusters GPU nodes. We expected that you already have access and know how to login.

## 0. Git clone the guides repo with the examples

To facilitate the demonstration we already prepared the code and scripts necessary, your job is to first run and then understand by looking into more detail.

```bash
$ git clone https://github.com/ieeta-pt/HPC-guides.git
$ cd HPC-guides/examples/transformers
```

## 1. Preprare the environment

First step is the preparation of the development enviroment which in this case would be to load python, creating a virtual environment and install the dependencies.

```bash
$ module load python
$ python -m venv virtual-venv
$ source virtual-venv/bin/activate
$ pip install --upgrade pip
$ pip install transformers accelerate evaluate datasets scikit-learn
```

## 2. Submit the job

The `hf_classification_trainer.py` contains the barebone code to train a bert base model in a classification task using the yelp dataset.
`hf_trainer.sh` corresponds to the lunch script that has the SBATCH directives for resources aquisition. Note that in the lunch script
were are specifically requestion for a A6000 gpu (`--gres=gpu:nvidia-rtx-a6000:1 `).

```bash
$ sbatch hf_trainer.sh
Submitted batch job 95
```

```bash
$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                94       gpu hf_train tiagoalm  R       0:02      1 dl-srv-03
```

Check your directly for the output file and cat:

```bash
$ ll
total 24
drwxr-xr-x 3 tiagoalmeida students 4096 Jul  5 16:12 ./
drwxr-xr-x 4 tiagoalmeida students 4096 Jul  5 16:11 ../
-rw-r--r-- 1 tiagoalmeida students 2425 Jul  5 16:12 hf_classification_trainer.py
-rw-r--r-- 1 tiagoalmeida students 2152 Jul  5 16:13 hf_trainer-94.out
-rw-r--r-- 1 tiagoalmeida students  643 Jul  5 16:11 hf_trainer.sh
drwxr-xr-x 2 tiagoalmeida students 4096 Jul  5 16:12 output_dir/
```

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
