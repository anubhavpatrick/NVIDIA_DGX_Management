Reference - https://youtu.be/_QmgQQ7wSpQ

Use netplan and edit \*.yaml in the /etc/netplan/ directory similar to configuration given below:

```
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    ens3f0np0:
      addresses: [ 192.168.12.2/16]
      #gateway4: 192.168.1.4
      nameservers:
        addresses: [192.168.1.4]
      routes:
        - to: 0.0.0.0/0
          via: 192.168.1.4
          metric: 0
          table: 60
      routing-policy:
        - from: 192.168.0.0/16
          table: 60
    eno6:
      addresses: [ 117.55.242.133/29]
      gateway4: 117.55.242.129
      nameservers:
        addresses: [117.55.240.4, 8.8.8.8]
```
