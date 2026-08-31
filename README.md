# Flask API - Docker & Kubernetes Journey

A simple Python Flask application structured for transitioning from Docker containers to Kubernetes orchestration.

## 🚀 Local Development Setup

To test the application on your host machine inside the virtual environment:

```bash
python3 m venv .venv
# 1. Activate your virtual environment
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1

# 2. Install requirements
pip install -r requirements.txt

# 3. Run the development app
python app.py
```

---

## 🐳 Core Docker Commands

Run these commands from the root directory where your `Dockerfile` is located.

### 1. Build the Docker Image
Build your application container image and tag it as version `v1`:
```bash
docker build -t flask-app:v1 .
```

### 2. Run the Container
Run the container in detached mode (`-d`), mapping port 5000 of your machine to port 5000 inside the container:
```bash
docker run -d -p 8000:8000 --name running-flask-container flask-app:v1
```

### 3. Verify and Test Endpoints
Test both endpoints locally using your browser or `curl`:
```bash
# Test the Home path
curl http://localhost:8000/

# Test the HEALTH path (for Ingress testing)
curl http://localhost:5000/health
```

---

## 🛠️ Docker Maintenance & Debugging

```bash
docker ps
docker ps -a
docker logs -f running-flask-container
docker stop running-flask-container
docker rm running-flask-container
docker images
```
