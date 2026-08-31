## ⚡ CKAD Probes Imperative Reference

Use these dry-run commands to generate your base manifests instantly, then add the readiness and liveness probe blocks under the container specification.

### 1. Pod Generation Command
```bash
kubectl run flask-pod --image=flask-app:v1 --port=8000 --dry-run=client -o yaml > k8s/pod1.yaml
```

### 2. Deployment Generation Command (3 Replicas)
```bash
kubectl create deployment flask-deploy --image=flask-app:v1 --replicas=3 --port=8000 --dry-run=client -o yaml > k8s/deployment-probes.yaml
```

---

## 🛠️ Probe Snippet for Copy-Pasting

Paste this block directly under the container properties (`ports:` block), matching the required indentation level (4 spaces for Pods, 8 spaces for Deployments).

```yaml
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /live
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
```
