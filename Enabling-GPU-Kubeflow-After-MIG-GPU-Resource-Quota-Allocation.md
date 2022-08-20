### Follow given steps:

1. kubectl get daemonset --all-namespaces

2. kubectl edit daemonset -n kube-system nvidia-device-plugin --namespace kube-system

3. Edit file as given in https://www.editcode.net/thread-78334-1-1.html

```
......
    spec:
      containers:
      - args:
        - --mig-strategy=mixed
        - --pass-device-specs=false
        - --fail-on-init-error=true
        - --device-list-strategy=envvar
        - --device-id-strategy=uuid
        - --nvidia-driver-root=/
+       env:
+       - name: NVIDIA_MIG_MONITOR_DEVICES
+         value: all
 ......
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
-           drop:
-           - ALL
+           add:
+           - SYS_ADMIN
 ......
 ```
