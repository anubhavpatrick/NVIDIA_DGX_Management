### To give find current ip of bmc

```bash
sudo ipmitool lan print  
```

### To give static ip to bmc

```bash
sudo ipmitool lan set 1 ipsrc static
sudo ipmitool lan set 1 ipaddr <ipaddr>
sudo impitool lan set 1 netmask <netmask>
sudo ipmitool lan set 1 defgw ipaddr <ipaddr>
```

### User Management of BMC

1. View existing BMC users
```bash
sudo ipmitool user list 1
```

2. To enable a BMC user - first note down id of user using above command then
```bash
sudo ipmitool user enable <id>
```

3. To disable a BMC user - first note down id of user using above command then
```bash
sudo ipmitool user disable <id>
```

4. To add a new BMC user
```bash
ipmitool user set name <id> <username>
```

5. To modify password of existing user
```bash
ipmitool user set password <id>
```

6. To restart BMC without restarting the server
```bash
ipmitool bmc reset cold
```

### Reference
[1] https://www.intel.in/content/www/in/en/support/articles/000055688/server-products.html
[2] https://serverfault.com/questions/205658/restarting-an-ibm-bmc-without-restarting-the-server-itself
