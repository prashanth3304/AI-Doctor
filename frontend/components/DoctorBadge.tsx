export default function DoctorBadge({ specialist }: { specialist: string }) {
  return (
    <span style={{ padding: "4px 10px", borderRadius: 999, background: "#e8f0ff", color: "#113377" }}>
      Routed to: {specialist}
    </span>
  );
}
