# 🔐 Secure Note API

> A production-grade DevSecOps demo project — a REST API built with FastAPI, secured and shipped through a fully automated security pipeline on GitHub Actions.

![CI Pipeline](https://github.com/jimsidi/secure-note-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136.1-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![Security](https://img.shields.io/badge/Security-DevSecOps-critical?logo=shield)
![ZAP](https://img.shields.io/badge/OWASP%20ZAP-119%2F119%20Passed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 What is this project?

This project demonstrates the **DevSecOps** approach — integrating security at every stage of the CI/CD pipeline, not as an afterthought. Security is automated, enforced, and visible on every commit.

Built as a portfolio project to showcase the difference between DevOps and DevSecOps in practice.

---

## 🛡️ Security Pipeline

Every push to `main` triggers a full automated security pipeline:

| # | Stage | Tool | What it checks |
|---|-------|------|----------------|
| 1 | 🧪 Unit Tests | pytest | Functional correctness |
| 2 | 🔍 SAST | Bandit | Python security anti-patterns |
| 3 | 🔎 SAST | Semgrep | Vulnerability patterns |
| 4 | 🔑 Secret Scan | Gitleaks | Leaked credentials in git history |
| 5 | 📦 SCA | pip-audit | Known CVEs in dependencies |
| 6 | 🐳 Container Scan | Trivy | CVEs in Docker image layers |
| 7 | 🕷️ DAST | OWASP ZAP | Live attack simulation (119/119 ✅) |

---

## 🔥 Real CVEs Found & Fixed

During development, the pipeline caught and fixed real vulnerabilities:

| CVE | Package | Severity | Fix |
|-----|---------|----------|-----|
| CVE-2025-71176 | pytest 8.2.0 | Medium | Upgraded to 9.0.3 |
| CVE-2024-47874 | starlette 0.37.2 | High | Upgraded via FastAPI 0.136.1 |
| CVE-2025-54121 | starlette 0.37.2 | High | Upgraded via FastAPI 0.136.1 |
| CVE-2025-62727 | starlette 0.46.2 | High | Upgraded via FastAPI 0.136.1 |

---

## 🚀 Stack

- **FastAPI** — REST API framework
- **Docker** — Containerization
- **GitHub Actions** — CI/CD + Security pipeline
- **Bandit** — Python SAST
- **Semgrep** — Multi-rule SAST
- **Gitleaks** — Secret scanning
- **pip-audit** — Dependency vulnerability audit
- **Trivy** — Container image scanning
- **OWASP ZAP** — Dynamic application security testing

---

## 🏃 Run locally

```bash
# With Docker
docker compose up --build

# Without Docker
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit **http://localhost:8000/docs** for the interactive API.

---

## 🧪 Run tests

```bash
pytest tests/ -v
```

---

## 📊 DevOps vs DevSecOps

| Layer | DevOps | DevSecOps (this project) |
|-------|--------|--------------------------|
| CI/CD | Build & deploy | Build, scan, gate, deploy |
| Dependencies | Install | Audit for CVEs |
| Code | Lint & test | SAST security analysis |
| Containers | Build & push | Scan for vulnerabilities |
| Secrets | Use env vars | Detect leaks in history |
| Runtime | Monitor uptime | Live attack simulation |

---

## 👨‍💻 Author

**Jim Sidi** — [Portfolio](https://jimsidi.github.io)