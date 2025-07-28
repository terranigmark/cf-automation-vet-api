
# Veterinary API (FastAPI Scaffold)

This project provides a veterinary‑clinic backend using **FastAPI** and **SQLAlchemy 2.0**.
It now includes CRUD APIs for:

* Patients
* Employees
* Inventory items and equipment
* Prescriptions and patient histories
* Payments and orders

The codebase comes with a configuration stub, a DB session dependency and a ready‑to‑install `requirements.txt`.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000/docs> for interactive API docs.
# cf-automation-vet-api
