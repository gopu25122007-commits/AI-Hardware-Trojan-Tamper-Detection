"""Simple demo anomaly and tamper detector for simulated sensor readings.

This is an educational proof of concept, not a validated hardware Trojan detector.
"""
from dataclasses import dataclass


@dataclass
class Reading:
    voltage: float
    current: float
    temperature: float
    tamper: bool = False


def analyse_reading(reading: Reading) -> dict:
    """Flag threshold deviations and a physical tamper sensor event."""
    reasons = []
    if not 4.5 <= reading.voltage <= 5.5:
        reasons.append("voltage_out_of_range")
    if not 0.0 <= reading.current <= 2.0:
        reasons.append("current_out_of_range")
    if not 10.0 <= reading.temperature <= 70.0:
        reasons.append("temperature_out_of_range")
    if reading.tamper:
        reasons.append("physical_tamper_detected")
    return {
        "status": "ALERT" if reasons else "NORMAL",
        "reasons": reasons,
        "note": "Threshold-based demo only; not proof of a hardware Trojan."
    }
