"use client";

import { useState } from "react";
import DoctorBadge from "./DoctorBadge";

const requiredFields = [
  "symptoms",
  "duration",
  "severity",
  "age",
  "existing_diseases",
  "medication_history",
  "sleep_pattern",
  "diet_habits",
];

export default function ConsultationForm() {
  const [payload, setPayload] = useState({
    patient_id: 1,
    symptoms: "",
    duration: "",
    severity: "",
    age: 30,
    existing_diseases: "",
    medication_history: "",
    sleep_pattern: "",
    diet_habits: "",
  });
  const [result, setResult] = useState<any>(null);

  const submit = async () => {
    const missing = requiredFields.filter((f) => !(payload as any)[f]);
    if (missing.length > 0) {
      alert(`Missing required fields: ${missing.join(", ")}`);
      return;
    }
    setResult({
      specialist: "General Physician",
      disclaimer: "AI advisory only. Not a replacement for real doctors.",
      emergency: false,
      advice: "Connect backend and auth token to perform real consultation.",
    });
  };

  return (
    <div style={{ display: "grid", gap: 8, maxWidth: 700 }}>
      {Object.keys(payload).map((key) => (
        <input
          key={key}
          placeholder={key}
          value={(payload as any)[key]}
          onChange={(e) => setPayload({ ...payload, [key]: e.target.value })}
          style={{ padding: 10 }}
        />
      ))}
      <button onClick={submit} style={{ padding: 10 }}>Start Consultation</button>
      {result && (
        <div style={{ border: "1px solid #ddd", padding: 12 }}>
          <DoctorBadge specialist={result.specialist} />
          <p>{result.advice}</p>
          <p><strong>Disclaimer:</strong> {result.disclaimer}</p>
        </div>
      )}
    </div>
  );
}
