from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def cleanup_db() -> None:
    db_file = Path("family_doctor.db")
    if db_file.exists():
        db_file.unlink()


def test_phase1_auth_profile_consultation_flow():
    cleanup_db()

    register_resp = client.post(
        "/api/v1/auth/register",
        json={
            "email": "phase1@example.com",
            "full_name": "Phase One",
            "password": "securepass123",
            "role": "admin",
        },
    )
    assert register_resp.status_code == 200
    token = register_resp.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    profile_resp = client.post(
        "/api/v1/profiles",
        headers=headers,
        json={
            "name": "Parent",
            "age": 45,
            "allergies": "penicillin",
            "bp_history": "130/85",
            "sugar_history": "normal",
            "previous_illnesses": "asthma",
        },
    )
    assert profile_resp.status_code == 200
    patient_id = profile_resp.json()["id"]

    consult_resp = client.post(
        "/api/v1/consultation/start",
        headers=headers,
        json={
            "patient_id": patient_id,
            "symptoms": "I have chest pain and mild palpitations",
            "duration": "2 hours",
            "severity": "moderate",
            "age": 45,
            "existing_diseases": "hypertension",
            "medication_history": "amlodipine",
            "sleep_pattern": "6 hours",
            "diet_habits": "high salt food",
        },
    )
    assert consult_resp.status_code == 200
    payload = consult_resp.json()
    assert payload["specialist"] == "Cardiologist"
    assert payload["emergency_flag"] is True
    assert "Disclaimer" in payload["advice"]

    cleanup_db()
