# Cluster Nodes

Nodes may change or be added to the cluster.  Use cluster commands to get up-to-date info.

## GPU Nodes:

### gpu-srv-02:
  - Type: HP-workstation
  - CPU: i7-12700 (12C)
  - RAM: 16GB
  - GPU-0: A2000
  - Temporary local storage: 512GB nvme SSD (/tmp/your-job)
  - Slurm GPU resource name: **nvidia-rtx-a2000**

### gpu-srv-03:
  - Type: Asus Server
  - CPU: EPYC 7543 (32C/64T)
  - RAM: 256GB
  - GPU-0: A6000
  - GPU-1: A6000
  - Temporary local storage: 512GB nvme SSD (/tmp/your-job)
  - Slurm GPU resource name: **nvidia-rtx-a6000**

### gpu-srv-04:
  - Type: AlianWare workstation
  - CPU: Ryzen 9 5900 (12C/24T)
  - RAM: 96GB
  - GPU-0: RTX 4070
  - Temporary local storage: NONE
  - Slurm GPU resource name: **nvidia-rtx-4070**

(More to be added in the future)

## CPU Nodes:

### cpu-srv-01:
  - Type: SuperMicro Server
  - CPU: AMD EPYC 9354P (32/64)
  - RAM: 768GB (DDR5)
  - Temporary local storage: None at the moment

### cpu-srv-02:
  - Type: Dell PowerEdge R730
  - CPU: Intel® Xeon® E5-2670 (12/24)
  - RAM: 192GB
  - Temporary local storage: None at the moment

### cpu-srv-03:
  - Type: SuperMicro Server
  - CPU: AMD EPYC 9355P (32/64)
  - RAM: 256GB
  - Temporary local storage: 512GB nvme SSD (/tmp/your-job)

(More to be added in the future)

## Login Node:
  - Type: VM
  - CPU: 22 Cores
  - RAM: 66GB
