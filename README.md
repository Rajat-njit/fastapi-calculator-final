
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
