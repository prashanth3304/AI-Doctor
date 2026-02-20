# Personal AI Family Doctor System - Architecture

## 1. Solution Overview
The system is a **multi-specialty AI medical advisory platform** for household usage. It simulates a doctor-style consultation workflow while clearly stating that it is **not a replacement for licensed medical professionals**.

Core capabilities:
- Multi-doctor symptom routing (General Physician, Gastroenterologist, Dermatologist, Cardiologist, Nutritionist, Mental Health Advisor, Hair Specialist)
- Structured consultation intake + SOAP notes
- Family memory via SQLite patient profiles
- Report analyzer for PDF/Image lab reports
- Emergency risk detection
- Knowledge base uploads + retrieval-augmented generation (RAG)
- Voice support (STT/TTS in English & Telugu)
- Authentication + family role-based access

## 2. High-Level Architecture

```mermaid
flowchart LR
    UI[Next.js Frontend\n(Web + Voice)] --> API[FastAPI Backend]
    API --> AUTH[JWT Auth + Role Guards]
    API --> DB[(SQLite)]
    API --> ORCH[Consultation Orchestrator]
    ORCH --> ROUTER[Specialist Router]
    ORCH --> EMR[Emergency Detector]
    ORCH --> SOAP[SOAP Generator]
    ORCH --> OLLAMA[Ollama Llama3]
    API --> RAG[RAG Service\nLangChain + Chroma]
    RAG --> CHROMA[(ChromaDB)]
    RAG --> OLLAMA
    API --> REPORT[Report Analyzer\nOCR/Text Extraction]
    API --> VOICE[STT/TTS Service]
```

## 3. Backend Service Design

### 3.1 API Gateway (FastAPI)
- Receives user requests, validates payloads, enforces auth.
- Exposes endpoints for consultation, profiles, reports, knowledge docs, and voice.

### 3.2 Consultation Orchestrator
- Ensures mandatory pre-advice questions are completed:
  - symptoms, duration, severity, age, existing diseases, medication history, sleep, diet
- Reads patient history from SQLite before advice generation.
- Routes to specialist using symptom classifier + rule engine.
- Injects safety disclaimer and emergency warnings when needed.
- Produces SOAP output.

### 3.3 Specialist Router
Rules + LLM classification hybrid:
- Chest pain/palpitations → Cardiologist
- Stomach pain/acidity/diarrhea → Gastroenterologist
- Rash/acne/itching → Dermatologist
- Hairfall/scalp issues → Hair Specialist
- Anxiety/depression/suicidal ideation → Mental Health Advisor
- Diet/weight management → Nutritionist
- Default/unclear → General Physician

### 3.4 Family Memory Layer (SQLite)
- Stores family users, patient profiles, vitals trends, illnesses, allergies, medications.
- Consultation service fetches latest history and adds context prompt.

### 3.5 Report Analyzer
- Accept PDF/image uploads.
- Extract text (PyMuPDF + OCR fallback).
- Parse common markers (HbA1c, glucose, LDL, BP, TSH, etc.) with reference ranges.
- Mark abnormal values and explain in plain language.

### 3.6 RAG Knowledge Base
- Upload medical PDFs to knowledge corpus.
- Chunk + embed + index in Chroma.
- Retrieve top-k chunks for grounded responses.
- Restrict to advisory language (no diagnosis certainty).

### 3.7 Voice Service
- STT: Whisper/faster-whisper (en/te).
- TTS: Coqui or gTTS-compatible service (en/te).
- Frontend microphone capture + playback.

## 4. Security & Access Model
- JWT-based auth (`/auth/register`, `/auth/login`).
- Roles:
  - `admin`: manages family profiles and KB uploads.
  - `member`: can consult, upload reports.
  - `viewer`: read-only profile/reports.
- Password hashing with bcrypt.
- Input sanitization and file-type validation for uploads.
- API rate limits (recommended in production).

## 5. Safety Framework
Every response must include:
1. **Medical disclaimer** (AI advisory only, not a replacement for doctors).
2. **Emergency escalation** when red flags appear:
   - chest pain
   - breathing difficulty
   - suicidal thoughts
3. **Urgency recommendation** (ER now / doctor within 24h / routine follow-up).

## 6. Deployment Architecture
- `backend` container (FastAPI + LangChain).
- `frontend` container (Next.js).
- `ollama` container (Llama3 inference).
- `chromadb` container.
- Shared network via `docker-compose`.
