These commands must be executed either in DGX directly or via ssh access

1. **vim profile.yaml**

   Given below is a template for user creation with quotas
```
apiVersion: kubeflow.org/v1beta1
kind: Profile
metadata:
  name: amit-seth   # replace with the name of profile you want, this will be user's namespace name
spec:
  owner:
    kind: User
    name: amit-seth   # replace with the email of the user

  resourceQuotaSpec:    # resource quota can be set optionally
   hard:
     cpu: "8"
     memory: "32Gi"
     requests.nvidia.com/gpu: "2"
     requests.nvidia.com/mig-3g.20gb: "2"
     persistentvolumeclaims: "1"
     requests.storage: "50Gi"
```

2. **kubectl apply -f profile.yaml**

3. Check whether profile is properly created 
   
   **kubectl get profile**
   
4. Create hashed password for use for Dex (Authentication mechanism of kubeflow) using:
   
   https://bcrypt-generator.com/

5. Make hashed password entry in Dex
   
   **kubectl edit configmap dex -n aut**
   
   A sample configmap after entry of user amit-seth is shown below
   
```
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: v1
data:
  config.yaml: |
    issuer: http://dex.auth.svc.cluster.local:5556/dex
    storage:
      type: kubernetes
      config:
        inCluster: true
    web:
      http: 0.0.0.0:5556
    logger:
      level: "debug"
      format: text
    oauth2:
      skipApprovalScreen: true
    enablePasswordDB: true
    staticPasswords:
    - email: admin@kubeflow.org
      hash: $2y$12$ruoM7FqXrpVgaol44eRZW.4HWS8SAvg6KYVVSCIwKQPBmTpCm.EeO
      username: admin
      userID: 08a8684b-db88-4b73-90a9-3cd1661f5466
    - email: amit-seth
      hash: $2a$12$/uRCY1ImpuhcDPEGsonb4u8yew0gukqjCgvUCnjSJdp1vRbQ8afrK
      username: amit
    - email: rishabh-kamal
      hash: $2a$12$.ev4dMMtvgyzy3RclPgvxO1P29L9K/GSPIZdk34tjvc8wJM7RNwpW
      username: rishabh
    - email: sachin-jain
      hash: $2a$12$e3kv4IKZA/kdMfGXV0zM2evD17BA7dodHua5Ti3tw/mbk5c1DOVjq
      username: sachin
    - email: faculty
      hash: $2a$12$hi8ofkm.ALLZ3aEojmSxYOC9aw8CnE3hybypJ8C9czOEt2NsDXWuC
      username: faculty
    staticClients:
    - id: kubeflow-oidc-authservice
      redirectURIs: ["/login/oidc"]
      name: 'Dex Login Application'
      secret: pUBnBOY80SnXgjibTYM9ZWNzY2xreNGQok
kind: ConfigMap
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"config.yaml":"issuer: http://dex.auth.svc.cluster.local:5556/dex\nstorage:\n  type: kubernetes\n  config:\n    inCluster: true\nweb:\n  http: 0.0.0.0:5556\nlogger:\n  level: \"debug\"\n  format: text\noauth2:\n  skipApprovalScreen: true\nenablePasswordDB: true\nstaticPasswords:\n- email: admin@kubeflow.org\n  hash: $2y$12$ruoM7FqXrpVgaol44eRZW.4HWS8SAvg6KYVVSCIwKQPBmTpCm.EeO\n  username: admin\n  userID: 08a8684b-db88-4b73-90a9-3cd1661f5466\nstaticClients:\n- id: kubeflow-oidc-authservice\n  redirectURIs: [\"/login/oidc\"]\n  name: 'Dex Login Application'\n  secret: pUBnBOY80SnXgjibTYM9ZWNzY2xreNGQok\n"},"kind":"ConfigMap","metadata":{"annotations":{},"name":"dex","namespace":"auth"}}
  creationTimestamp: "2022-08-19T12:41:35Z"
  name: dex
  namespace: auth
  resourceVersion: "4668062"
  uid: 13d86399-ab89-49e1-acd2-cd2b248988a3
```

6. Restart Dex authentication service

   **kubectl rollout restart deployment dex -n auth**
