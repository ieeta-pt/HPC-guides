# Cuda example

This example demonstrates how to compile and execute a CUDA program on one of the cluster's GPU nodes. It is assumed that you already have access and know how to log in.

## 0. Git clone the guides repo with the examples

To facilitate the demonstration, we have pre-prepared the necessary code and scripts in a repo. Your just need to execute the code and then explore it in further detail.

```bash
$ git clone https://github.com/ieeta-pt/HPC-guides.git
$ cd HPC-guides/examples/cuda
```

## 1. Preprare the environment

The initial step involves setting up the development environment, which in this case means loading the GCC compiler and CUDA libraries.

```bash
$ module load gcc
$ module load cuda
```

Currently there are two versions of CUDA installed (12.1 and 11.8). By default the latest one is always loaded when a version is not specified.

Note that if you want to run CUDA 11.8 you aldo need to use gcc 11 due to compatibility issues from CUDA.

## 2. Compile the cuda program

To compile the CUDA program, simply use the NVCC compiler:

```bash
$ nvcc vector_addition.cu -o vector_addition
```

## 3. Submit the job

The launch_cuda.sh script contains the necessary code to submit the Slurm job while requesting a GPU.

```bash
$ sbatch launch_cuda.sh
Submitted batch job 93
```

Check your directory for the output file and view its contents:

```bash
$ ll
total 808
drwxr-xr-x 2 tiagoalmeida students   4096 Jul  5 15:49 ./
drwxr-xr-x 3 tiagoalmeida students   4096 Jul  5 15:48 ../
-rw-r--r-- 1 tiagoalmeida students    248 Jul  5 15:49 Cuda-93.out
-rw-r--r-- 1 tiagoalmeida students    504 Jul  5 15:48 launch_cuda.sh
-rwxr-xr-x 1 tiagoalmeida students 803936 Jul  5 15:48 vector_addition*
-rw-r--r-- 1 tiagoalmeida students   2051 Jul  5 15:48 vector_addition.cu
$
$ cat Cuda-93.out 
Job Information for Job ID: 93 from tiagoalmeida
------------ ------------
Account: students
CPUs per Node: 2
GPU: NVIDIA RTX A2000
Partition: gpu
QOS: normal
Start Time: 2024-07-05 14:49:32 UTC
Running On Node: dl-srv-02
------------ ------------

---------------------------
__SUCCESS__
---------------------------
N                 = 1048576
Threads Per Block = 256
Blocks In Grid    = 4096
---------------------------
```
