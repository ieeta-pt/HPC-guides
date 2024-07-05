# Cuda example

This example shows how you can compile and run a cuda program in one of the clusters GPU nodes. We expected that you already have access and know how to login.

## 0. Git clone the guides repo with the examples

To facilitate the demonstration we already prepared the code and scripts necessary, your job is to first run and then understand by looking into more detail.

```bash
$ git clone https://github.com/ieeta-pt/HPC-guides.git
$ cd HPC-guides/examples/cuda
```

## 1. Preprare the environment

First step is the preparation of the development enviroment which in this case would be to load the gcc compiler and CUDA libraries.

```bash
$ module load gcc/11
$ module load cuda
```

Here we load gcc 11 and not 12, since the currently installed CUDA version (11.8) advises to run with gcc 11.

## 2. Compile the cuda program

For compiling the cuda program just call the nvcc

```bash
$ nvcc vector_addition.cu -o vector_addition
```

## 3. Submit the job

`lunch_cuda.sh` already contains the code to lunch the slurm job while requesting a gpu.

```bash
$ sbatch lunch_cuda.sh
```

Check your directly for the output file and cat:

```bash
$ ll
total 808
drwxr-xr-x 2 tiagoalmeida students   4096 Jul  5 15:49 ./
drwxr-xr-x 3 tiagoalmeida students   4096 Jul  5 15:48 ../
-rw-r--r-- 1 tiagoalmeida students    248 Jul  5 15:49 Cuda-93.out
-rw-r--r-- 1 tiagoalmeida students    504 Jul  5 15:48 lunch_cuda.sh
-rwxr-xr-x 1 tiagoalmeida students 803936 Jul  5 15:48 vector_addition*
-rw-r--r-- 1 tiagoalmeida students   2051 Jul  5 15:48 vector_addition.cu
```

```bash
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

