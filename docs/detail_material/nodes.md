# Cluster Nodes

__This page is very OUTDATED!__
Do not rely on it.

Use cluster commands to get up-to-date info.

```sh
$ cluster-info     # on 2026-07-17
```
<pre>=== Nodes Resources Information ===

NODE         Av. CPUs     Av. Mem. (GB)      Av. GPUs            
==============================================================
cpu-srv-01   <font color="#A2734C"><b>62</b></font>/64        <font color="#A2734C"><b>304.5</b></font>/754.5        0/0 ()      
cpu-srv-03   <font color="#26A269">64</font>/64        <font color="#26A269">250.7</font>/250.7        0/0 ()      
gpu-srv-01   <font color="#A2734C"><b>32</b></font>/64        <font color="#26A269">374.4</font>/502.4        <font color="#A2734C"><b>1</b></font>/2 (nvidia-rtx-pro-6000-blackwell-max-q-workstation-edition)
gpu-srv-02   <font color="#26A269">12</font>/12        <font color="#26A269">14.4</font>/14.4          <font color="#26A269">1</font>/1 (nvidia-rtx-a2000)
gpu-srv-03   <font color="#26A269">64</font>/64        <font color="#26A269">250.6</font>/250.6        <font color="#26A269">4</font>/4 (nvidia-rtx-pro-5000-blackwell, nvidia-rtx-a6000)

=== Partition Resources Information ===

PARTITION    NODES    Av. CPUs     Av. Mem. (GB)      Av. GPUs    
==============================================================
cpu          2        <font color="#A2734C"><b>126</b></font>/128      <font color="#A2734C"><b>555.2</b></font>/1005.2       0/0 
gpu          3        <font color="#A2734C"><b>108</b></font>/140      <font color="#26A269">639.5</font>/767.5        <font color="#A2734C"><b>6</b></font>/7
</pre>

Try `scontrol show node` for more details.


----

# OLD INFO

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
