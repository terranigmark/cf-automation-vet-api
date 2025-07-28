
# Veterinary API (FastAPI Scaffold)

This is a minimal scaffold for a veterinary‑clinic backend using **FastAPI** and **SQLAlchemy 2.0**.
It includes:

* Project layout
* Example patient model, schema, CRUD helper and router
* Configuration stub
* Dependency for DB session
* Requirements file ready to `pip install -r requirements.txt`

Use this as a starting point—add the remaining models (Employee, InventoryItem, etc.) by following
the pattern shown in the *patient* files.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000/docs> for interactive API docs.
# cf-automation-vet-api
