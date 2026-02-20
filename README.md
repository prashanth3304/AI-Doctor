# AI Family Doctor - Phase 1 MVP (Backend)

> ⚠️ **Safety Disclaimer:** This system is for AI-assisted health guidance only. It is NOT a replacement for licensed doctors, diagnosis, treatment, or emergency services.

## Phase 1 Scope
This MVP includes a working FastAPI backend with:
- Project folder structure
- SQLite database schema
- JWT authentication
- Doctor agent modules (7 specialties)
- Symptom consultation flow with SOAP output and emergency detection

## Backend Folder Structure

```text
backend/
├── app/
│   ├── agents/
│   │   ├── base.py
│   │   ├── specialists.py
│   │   └── factory.py
│   ├── api/
│   │   ├── auth.py
│   │   ├── consultation.py
│   │   ├── deps.py
│   │   └── profiles.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── consultation.py
│   │   ├── patient.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── consultation.py
│   │   └── patient.py
│   ├── services/
│   │   ├── emergency.py
│   │   ├── soap.py
│   │   └── specialist_router.py
│   └── main.py
├── requirements.txt
└── tests/
    └── test_phase1.py
```

## SQLite Schema
- `users`: auth + family roles
- `patients`: family memory (name, age, allergies, BP, sugar, previous illnesses)
- `consultations`: consultation intake + specialist + emergency + SOAP + advice

## API Endpoints
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/profiles`
- `GET /api/v1/profiles`
- `GET /api/v1/profiles/{patient_id}`
- `GET /api/v1/consultation/required-questions`
- `POST /api/v1/consultation/start`

## Local Run
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Test
```bash
cd backend
pytest -q
```
