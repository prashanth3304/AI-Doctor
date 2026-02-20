import re

MARKERS = {
    "glucose": (70, 99),
    "hba1c": (4.0, 5.6),
    "ldl": (0, 100),
    "tsh": (0.4, 4.0),
}


def parse_abnormal_values(text: str) -> list[str]:
    findings = []
    lower = text.lower()
    for marker, (low, high) in MARKERS.items():
        match = re.search(rf"{marker}\s*[:\-]?\s*(\d+(?:\.\d+)?)", lower)
        if match:
            value = float(match.group(1))
            if value < low or value > high:
                findings.append(f"{marker.upper()} abnormal: {value} (expected {low}-{high})")
    return findings
