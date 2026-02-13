# Kubernetes CI/CD Platform

A comprehensive Kubernetes-based CI/CD platform with containerized applications, automated deployments, and Jenkins pipeline orchestration.

## 📋 Repository Structure

This project has been reorganized for clarity and maintainability:

```
├── docs/                    # Documentation & Configuration
│   ├── README.md           # Original project documentation
│   ├── LICENSE.md          # Project license
│   ├── part[1-4].yml       # Setup and configuration guides
│   ├── steps.yml           # Deployment step-by-step guide
│   └── DLP_05072023.csv    # Data files
│
├── deployment/             # Infrastructure & Deployment
│   ├── manifests/          # Kubernetes YAML manifests
│   │   ├── registry.yaml
│   │   ├── all-services.yaml
│   │   ├── etcd-cluster.yaml
│   │   ├── etcd-service.yaml
│   │   ├── jenkins.yaml
│   │   └── monitor-scale-serviceaccount.yaml
│   │
│   └── scripts/            # Deployment automation
│       ├── etcd.sh
│       ├── etcd-crd.sh
│       ├── kr8sswordz-pages.sh
│       ├── monitor-scale.sh
│       ├── puzzle.sh
│       └── kubescale.sh
│
├── applications/           # Application Source Code
│   ├── puzzle/            # Main puzzle game application
│   ├── kr8sswordz-pages/  # Frontend pages & UI
│   ├── monitor-scale/     # Monitoring & auto-scaling service
│   ├── jenkins/           # Jenkins configuration
│   ├── hello-kenzan/      # Kenzan hello world example
│   ├── socat/             # Socket utility application
│   └── spinnaker-helm/    # Spinnaker Helm charts
│
├── ci-cd/                  # CI/CD Pipeline Configuration
│   ├── Jenkinsfile        # Jenkins pipeline definition
│   └── package.json       # Node.js dependencies
│
├── tests/                  # Test Suite
│   ├── java/              # Java unit tests
│   ├── python/            # Python tests
│   └── test.txt           # Test documentation
│
├── tools/                  # Utilities & Scripts
│   ├── start.js           # Application startup script
│   └── readme.js          # README generator utility
│
└── config/                 # Configuration Files (extensible)
```

## 🚀 Quick Start

### Prerequisites
- Kubernetes cluster
- Docker
- Jenkins (for CI/CD)
- Node.js

### View Documentation
```bash
# Read the main project documentation
cat docs/README.md

# Review deployment steps
cat docs/steps.yml

# Check configuration guides
cat docs/part*.yml
```

### Deploy to Kubernetes
```bash
# Apply manifests
kubectl apply -f deployment/manifests/

# Run deployment scripts
./deployment/scripts/etcd.sh
./deployment/scripts/puzzle.sh
./deployment/scripts/kr8sswordz-pages.sh
./deployment/scripts/monitor-scale.sh
```

### Run Tests
```bash
# Run Java tests
cd tests/java/
# Execute test files

# Run Python tests
cd tests/python/
# Execute test files
```

## 📦 Key Components

| Component | Location | Purpose |
|-----------|----------|---------|
| **Puzzle App** | `applications/puzzle/` | Main interactive application |
| **Frontend** | `applications/kr8sswordz-pages/` | Web UI and pages |
| **Monitoring** | `applications/monitor-scale/` | Performance monitoring & scaling |
| **Jenkins** | `ci-cd/` + `applications/jenkins/` | CI/CD pipeline orchestration |
| **ETCD** | `deployment/manifests/etcd-*.yaml` | Distributed configuration |
| **Registry** | `deployment/manifests/registry.yaml` | Docker image registry |

## 🔧 CI/CD Pipeline

The Jenkins pipeline is defined in `ci-cd/Jenkinsfile` and automates:
- Building applications
- Running tests
- Deploying to Kubernetes
- Health checks and monitoring

## 📄 File Organization

- **Documentation**: All markdown, guides, and CSVs → `docs/`
- **Infrastructure**: Kubernetes manifests and scripts → `deployment/`
- **Applications**: Source code and services → `applications/`
- **Pipeline**: Jenkins configuration → `ci-cd/`
- **Quality**: Test files organized by language → `tests/`
- **Tools**: Utility and helper scripts → `tools/`

## 🔍 For Detailed Information

Start with `docs/README.md` for comprehensive project information, architecture details, and advanced usage instructions.

## 📜 License

See `docs/LICENSE.md` for licensing information.

---

**Last Updated**: February 13, 2026  
**Repository**: https://github.com/newmoonsun/kubernetes-ci-cd
