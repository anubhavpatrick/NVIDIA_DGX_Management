### Note- These steps will only work when Kubernetes service is not running


Follow given steps to partition GPUs using MIG in NVIDIA DGX A100 if high level tool like NVIDIA GPU operator is not available:


1. Clone and Install Mig-Parted <br>https://github.com/NVIDIA/mig-parted


2. cd mig-parted/cmd


3. sudo systemctl stop nvsm


4. sudo systemctl stop dcgm


5. sudo modprobe -r nvidia_drm


6. sudo nvidia-smi --gpu-reset


7. sudo nvidia-mig-parted apply -f ../examples/config.yaml -c custom-config


8. sudo systemctl start nvsm


9. sudo systemctl start dcgm



