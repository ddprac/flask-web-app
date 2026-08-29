## ☸️ Core Kubernetes Commands

Run these commands from your root folder to manage the Pod, Deployment, Service, and Ingress resources.

### 2. Verify Status
```bash
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get ingress
kubectl get ingressclasses

```

### 3. Debug & Logs
```bash
kubectl logs -f deployment/flask-deployment
kubectl describe service flask-service
kubectl describe ingress flask-ingress
```

### 4. Test Ingress Routing
```bash
curl http://flask-app.local
curl http://flask-app.localapi
```

### 5. Clean Up Cluster
```bash
kubectl delete -f k8s/ingress.yaml
kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/pod1.yaml
```
