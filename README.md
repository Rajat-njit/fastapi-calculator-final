
# FastAPI Calculator — Full-Stack Web App with JWT Auth, BREAD Operations, Reporting, and CI/CD

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.8-009688?style=for-the-badge&logo=fastapi)
![Build](https://img.shields.io/badge/Build-Passing-success?style=for-the-badge)

## 1) Project Summary

This project is a full-stack web application implemented with **FastAPI** (backend), **SQLAlchemy** (ORM), and a relational database (**PostgreSQL in CI / Docker**, SQLite optionally for local), with a browser-based UI rendered using **Jinja2 templates**.

The system supports:

* **Secure user registration and login**
* **JWT-based authentication and authorization**
* **Multiple calculation types** (basic + advanced arithmetic)
* **Persisting calculation history** per user
* **BREAD operations** on calculation resources (Browse, Read, Edit, Add, Delete)
* **Reporting / export features** (user statistics + CSV export)
* **Full test suite** (unit + integration + end-to-end via Playwright)
* **CI/CD pipeline** that runs tests, enforces coverage, security scanning, and deploys Docker image to Docker Hub

> **Note:** This README is intentionally detailed because it is used for grading and explains implementation decisions and rubric alignment.

---

## 📁 Project Structure

```text
module14_is601/
│
├── app/
│   ├── __init__.py
│   ├── main.py                     # Application entry point & route definitions
│   │
│   ├── core/                       # Global config & settings
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── database.py                 # SQLAlchemy engine & session setup
│   ├── database_init.py
│   │
│   ├── auth/                       # Security & Auth logic
│   │   ├── __init__.py
│   │   ├── jwt.py
│   │   └── dependencies.py
│   │
│   ├── models/                     # Database Models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── calculation.py
│   │
│   ├── schemas/                    # Pydantic Schemas (Data Validation)
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── calculation.py
│   │   ├── token.py
│   │   └── stats.py
│   │
│   ├── services/                   # Business Logic Services
│   │   └── statistics_service.py
│   │
│   ├── operations/                 # Modular arithmetic logic
│   │   └── __init__.py
│   │
│   ├── static/                     # CSS/JS assets
│   └── templates/                  # Jinja2 HTML templates
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
├── .env.example
├── .github/
│   └── workflows/
│       └── test.yml
└── README.md
````


