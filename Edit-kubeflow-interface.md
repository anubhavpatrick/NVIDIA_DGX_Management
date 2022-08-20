### Follow given steps to modify the user interface of Kubeflow:

1. List all available configmaps

    ```sudo kubectl get configmap --all-namespaces```
    
2. Find the configmap starting with

     ```jupyter-web-app-*```
     
3. Edit the configmap:

      ```sudo kubectl edit configmap -n kubeflow jupyter-web-app-jupyter-web-app-config-8kcgd8t8th -o yaml```
      
