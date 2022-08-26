### Note- These steps are recommended when Kubernetes/Kubeflow service are running


Follow given steps to partition GPUs using MIG in NVIDIA DGX A100 (40 GB) if high level tool like NVIDIA GPU operator is not available:


1. Clone and install mig-parted <br>https://github.com/NVIDIA/mig-parted


2. Guide for mig-parted systemd service <br>https://github.com/NVIDIA/mig-parted/tree/main/deployments/systemd


3. cd deployments/systemd/


3. vim config-ampere.yaml 


4. Edit the configuration according to requirements. A sample configuration is given below:
```
version: v1
mig-configs:
  all-disabled:
    - devices: all
      mig-enabled: false

  # A100-40GB
  all-1g.5gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "1g.5gb": 7

  all-2g.10gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "2g.10gb": 3

  all-3g.20gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "3g.20gb": 2

  all-7g.40gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "7g.40gb": 1

  custom-config:
    - device-filter: "0x20B010DE"
      devices: [0,1]
      mig-enabled: false
    - device-filter: "0x20B010DE"
      devices: [2]
      mig-enabled: true
      mig-devices:
        "3g.20gb": 2
    - device-filter: "0x20B010DE"
      devices: [3]
      mig-enabled: true
      mig-devices:
        "3g.20gb": 2
    - device-filter: "0x20B010DE"
      devices: [4]
      mig-enabled: true
      mig-devices:
        "3g.20gb": 2
    - device-filter: "0x20B010DE"
      devices: [5]
      mig-enabled: true
      mig-devices:
        "3g.20gb": 2
    - device-filter: "0x20B010DE"
      devices: [6]
      mig-enabled: true
      mig-devices:
        "3g.20gb": 2
    - device-filter: "0x20B010DE"
      devices: [7]
      mig-enabled: true
      mig-devices:
        "3g.20gb": 2

  # A100-80GB
  all-1g.10gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "1g.10gb": 7

  all-2g.20gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "2g.20gb": 3

  all-3g.40gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "3g.40gb": 2

  all-7g.80gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "7g.80gb": 1

  # A30-24GB
  all-1g.6gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "1g.6gb": 4

  all-2g.12gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "2g.12gb": 2

  all-4g.24gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "4g.24gb": 1

  # PG506-96GB
  all-1g.12gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "1g.12gb": 7

  all-2g.24gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "2g.24gb": 3

  all-3g.48gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "3g.48gb": 2

  all-7g.96gb:
    - devices: all
      mig-enabled: true
      mig-devices:
        "7g.96gb": 1

  # A100-40GB, A100-80GB, A30-24GB
  all-balanced:
    # A100-40GB
    - device-filter: ["0x20B010DE", "0x20B110DE", "0x20F110DE"]
      devices: all
      mig-enabled: true
      mig-devices:
        "1g.5gb": 2
        "2g.10gb": 1
        "3g.20gb": 1

    # A100-80GB
    - device-filter: ["0x20B210DE", "0x20B510DE"]
      devices: all
      mig-enabled: true
      mig-devices:
        "1g.10gb": 2
        "2g.20gb": 1
        "3g.40gb": 1

    # A30-24GB
    - device-filter: "0x20B710DE"
      devices: all
      mig-enabled: true
      mig-devices:
        "1g.6gb": 2
        "2g.12gb": 1

    # PG506-96GB
    - device-filter: "0x20B610DE"
      devices: all
      mig-enabled: true
      mig-devices:
        "1g.12gb": 2
        "2g.24gb": 1
        "3g.48gb": 1
```



5. sudo ./install.sh


6. In future, if new MIG configurations are required, they can be edited using

sudo vim /etc/nvidia-mig-manager/config-ampere.yaml 


7. Apply MIG

```
sudo nvidia-mig-parted apply -f /etc/nvidia-mig-manager/config-ampere.yaml -k /etc/nvidia-mig-manager/hooks.yaml -c custom-config
```

or

```
sudo nvidia-mig-parted apply -f /etc/nvidia-mig-manager/config-ampere.yaml -k /etc/nvidia-mig-manager/hooks.yaml -c all-disabled
```

Follow above mig-parted systemd guide for further options
