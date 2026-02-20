import ConsultationForm from "../../components/ConsultationForm";

export default function ConsultationPage() {
  return (
    <main style={{ padding: 24 }}>
      <h2>Consultation Intake</h2>
      <p>Complete all mandatory fields before AI advice is generated.</p>
      <ConsultationForm />
    </main>
  );
}
