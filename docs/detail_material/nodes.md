# Cluster Nodes

We are currently in a testing phase, and nodes will be gradually added or migrated to the cluster.

## GPU Nodes:

### dl-srv-02:
  - Type: HP-workstation
  - CPU: i7-12700 (12C)
  - RAM: 16GB
  - GPU-0: A2000
  - Temporal local storage: 512GB nvme (/tmp/your-job)
  - Slurm GPU resource name: **nvidia-rtx-a2000**

### dl-srv-03:
  - Type: Asus Server
  - CPU: EPYC 7543 (32C/64T)
  - RAM: 256GB
  - GPU-0: A6000
  - GPU-1: A6000
  - Temporal local storage: 512GB nvme (/tmp/your-job)
  - Slurm GPU resource name: **nvidia-rtx-a6000**

### dl-srv-04:
  - Type: AlianWare workstation
  - CPU: Ryzen 9 5900 (12C/24T)
  - RAM: 96GB
  - GPU-0: RTX 4070
  - Temporal local storage: NONE
  - Slurm GPU resource name: **nvidia-rtx-4070**

(More to be added in the future)

## CPU Nodes:

(More to be added in the future)

## Login Node:
  - Type: VM
  - CPU: 22 Cores
  - RAM: 66GB
