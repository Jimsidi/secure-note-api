# 🔐 Secure Note API

A DevSecOps demo project — REST API with a full security pipeline.

![CI Pipeline](https://github.com/jimsidi/secure-note-api/actions/workflows/ci.yml/badge.svg)

## 🚀 Stack
- **FastAPI** — REST API
- **Docker** — Containerization
- **GitHub Actions** — CI/CD + Security pipeline

## 🛡️ Security Pipeline
| Step | Tool | Status |
|------|------|--------|
| SAST | Bandit + Semgrep | ✅ Active |
| Secret Scan | Gitleaks | ✅ Active |
| Dependency Audit | pip-audit | ✅ Active |
| Container Scan | Trivy | ✅ Active |
| DAST | OWASP ZAP | ✅ Active |

## 🏃 Run locally
```bash
docker compose up --build
```
Visit http://localhost:8000/docs