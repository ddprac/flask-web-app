## ⚖️ Compute Quotas (Requests & Limits)

```bash
# Generate base deployment blueprint frame
kubectl create deployment resource-demo --image=nginx --dry-run=client -o yaml > deployment.yaml
```

### Resource Snippet Reference
```yaml
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
```
