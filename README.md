# 🚀 K8s CI/CD Pipeline — Flask API + GitHub Actions + Kubernetes

![CI/CD Pipeline](https://github.com/SEU_GITHUB_USERNAME/k8s-cicd-pipeline/actions/workflows/deploy.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)

## 📋 Overview

End-to-end CI/CD pipeline that automatically builds, pushes, and deploys a Python Flask API to a Kubernetes cluster (Kind) using GitHub Actions.

Every push to `main` triggers the full pipeline:
1. Builds the Docker image
2. Pushes to Docker Hub
3. Creates a Kind cluster
4. Deploys to Kubernetes
5. Validates all endpoints

---

## 🏗️ Architecture

```
Developer → GitHub Push → GitHub Actions
                               │
                    ┌──────────┴──────────┐
                    │                     │
              Build & Push          Deploy to K8s
              Docker Image          (Kind Cluster)
                    │                     │
              Docker Hub           Kubernetes
                                   ├── Namespace: cicd-lab
                                   ├── Deployment (2 replicas)
                                   └── Service (NodePort)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python + Flask** | REST API application |
| **Gunicorn** | Production WSGI server |
| **Docker** | Containerization |
| **Kubernetes (Kind)** | Container orchestration |
| **GitHub Actions** | CI/CD automation |
| **Docker Hub** | Container registry |

---

## 📁 Project Structure

```
k8s-cicd-pipeline/
├── app/
│   ├── app.py              # Flask API (3 endpoints)
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Container definition
├── k8s/
│   ├── namespace.yaml      # Kubernetes namespace
│   ├── deployment.yaml     # Deployment (2 replicas + probes)
│   └── service.yaml        # NodePort service
└── .github/
    └── workflows/
        └── deploy.yml      # Full CI/CD pipeline
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main response with hostname |
| `/health` | GET | Liveness check |
| `/info` | GET | App info and tech stack |

---

## ⚙️ Setup & Run Locally

### Prerequisites
- Docker
- Kind
- kubectl

### 1. Clone the repository
```bash
git clone https://github.com/SEU_GITHUB_USERNAME/k8s-cicd-pipeline.git
cd k8s-cicd-pipeline
```

### 2. Create Kind cluster
```bash
kind create cluster --name cicd-lab
```

### 3. Build and push Docker image
```bash
cd app
docker build -t YOUR_DOCKERHUB_USERNAME/k8s-cicd-pipeline:latest .
docker push YOUR_DOCKERHUB_USERNAME/k8s-cicd-pipeline:latest
```

### 4. Update image in deployment
```bash
sed -i "s|SEU_DOCKERHUB_USERNAME|YOUR_DOCKERHUB_USERNAME|g" k8s/deployment.yaml
```

### 5. Deploy to Kubernetes
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 6. Verify deployment
```bash
kubectl get pods -n cicd-lab
kubectl get services -n cicd-lab
```

### 7. Test the API
```bash
kubectl port-forward service/flask-api-service 8080:80 -n cicd-lab
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/info
```

---

## 🔐 GitHub Actions Secrets

To run the pipeline, configure these secrets in your repository (`Settings → Secrets → Actions`):

| Secret | Description |
|--------|-------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token (not your password) |

---

## 📊 Pipeline Stages

```
push to main
     │
     ▼
┌─────────────────────┐
│   build-and-push    │
│  ─────────────────  │
│  • Checkout code    │
│  • Login Docker Hub │
│  • Build image      │
│  • Push image       │
└──────────┬──────────┘
           │ needs: build-and-push
           ▼
┌─────────────────────┐
│       deploy        │
│  ─────────────────  │
│  • Install Kind     │
│  • Create cluster   │
│  • Apply manifests  │
│  • Wait rollout     │
│  • Test endpoints   │
└─────────────────────┘
```

---

## 📝 Key Concepts Demonstrated

- **Infrastructure as Code** — Kubernetes manifests declaratively define the desired state
- **Automated testing** — Pipeline validates all endpoints before finishing
- **Health checks** — Liveness and readiness probes ensure pod reliability
- **Resource management** — CPU and memory limits defined per container
- **Multi-job pipeline** — Build and deploy are separated, deploy depends on build success

---

## 👤 Author

**Douglas Deveza**
- LinkedIn: [linkedin.com/in/douglasdeveza](https://linkedin.com/in/douglasdeveza)
- GitHub: [github.com/SEU_GITHUB_USERNAME](https://github.com/SEU_GITHUB_USERNAME)
