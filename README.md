# 📦 Project Setup

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

| `GET` | `/dashboard/view/{calc_id}` | View calculation |
| `GET` | `/dashboard/edit/{calc_id}` | Edit calculation |

-----

## 11\) Testing Strategy

This project follows a layered testing strategy aligned with industry best practices.

### 🧱 Testing Pyramid Overview

| Layer | Purpose | Scope |
| :--- | :--- | :--- |
| **Unit Tests** | Validate isolated logic | Models, services, schemas, utilities |
| **Integration Tests** | Validate API + DB interaction | Routes, auth, persistence |
| **E2E Tests** | Validate real user flows | UI + API + auth |

### 📌 Unit Test Coverage Map (`tests/unit/`)

| Test File | Covers | Application File |
| :--- | :--- | :--- |
| `test_calculator.py` | Basic arithmetic logic | `app/models/calculation.py` |
| `test_calculation_factory_unit.py` | Factory pattern mapping | `Calculation.create()` |
| `test_calculation_operations_unit.py` | Add/Sub/Mul/Div/Power/Modulus | Operation subclasses |
| `test_calculation_schema_unit.py` | Input validation | `app/schemas/calculation.py` |
| `test_dependencies_unit.py` | Auth dependency logic | `app/auth/dependencies.py` |
| `test_jwt_unit.py` | Token creation & decoding | `app/auth/jwt.py` |
| `test_user_unit.py` | User model behavior | `app/models/user.py` |
| `test_statistics_service_unit.py` | Stats computation | `compute_user_stats()` |

### 📌 Integration Test Coverage Map (`tests/integration/`)

| Test File | Covers | Application Area |
| :--- | :--- | :--- |
| `test_auth_routes.py` | Register + login routes | `/auth/*` |
| `test_calculation_routes.py` | CRUD calculations | `/calculations` |
| `test_api_new_operations.py` | Advanced ops (power, modulus) | Calculation extensions |
| `test_api_stats_and_report.py` | CSV + stats endpoints | Export & reporting |
| `test_database.py` | DB initialization | `database.py` |

### 📌 E2E Test Coverage Map (`tests/e2e/`)

| Test File | Covers | Scenario |
| :--- | :--- | :--- |
| `test_fastapi_calculator.py` | API + UI flow | Login → Calculate |
| `test_ui_playwright.py` | Browser automation | Full UI journey |

-----

## 14\) CI/CD Pipeline (`.github/workflows/test.yml`)

The CI pipeline is designed to satisfy both real-world best practices and professor requirements.

1.  **Test Job:**
      * Sets up Python & Dependencies.
      * Installs Playwright browsers.
      * Runs Unit Tests (**Enforces 90% Coverage**).
      * Runs Integration & E2E Tests.
2.  **Security Job:**
      * Runs **Trivy** scan on the Docker image.
3.  **Deploy Job:**
      * Builds & Pushes image to **Docker Hub** (on `main` branch).

-----

## 16\) Configuration: `.env` and `requirements.txt`

### `.env` File

Used for `DATABASE_URL`, `JWT_SECRET_KEY`, `BCRYPT_ROUNDS`, and `IS_TEST`.

### `requirements.txt`

Dependencies are pinned to ensure reproducibility. Key libraries include:

  * `fastapi`, `uvicorn`, `starlette` (Core)
  * `SQLAlchemy`, `psycopg2-binary` (DB)
  * `pydantic` (Validation)
  * `python-jose`, `passlib`, `bcrypt` (Auth)
  * `pytest`, `playwright`, `httpx` (Testing)

-----

# Conclusion

This project demonstrates an end-to-end FastAPI system including secure auth, DB-backed CRUD/BREAD resources, reporting implementation, frontend integration, thorough tests at multiple levels, CI/CD enforcement, and Docker deployment readiness.

----
## Author: Rajat Pednekar

```
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📝 7. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Complete Module X"
git push origin main
```

Then submit the GitHub repository link as instructed.

---

# 🔥 Useful Commands Cheat Sheet

| Action                         | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Install Homebrew (Mac)          | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Install Git                     | `brew install git` or Git for Windows installer |
| Configure Git Global Username  | `git config --global user.name "Your Name"`      |
| Configure Git Global Email     | `git config --global user.email "you@example.com"` |
| Clone Repository                | `git clone <repo-url>`                          |
| Create Virtual Environment     | `python3 -m venv venv`                           |
| Activate Virtual Environment   | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages        | `pip install -r requirements.txt`               |
| Build Docker Image              | `docker build -t <image-name> .`                |
| Run Docker Container            | `docker run -it --rm <image-name>`               |
| Push Code to GitHub             | `git add . && git commit -m "message" && git push` |

---

# 📋 Notes

- Install **Homebrew** first on Mac.
- Install and configure **Git** and **SSH** before cloning.
- Use **Python 3.10+** and **virtual environments** for Python projects.
- **Docker** is optional depending on the project.

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
