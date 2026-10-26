# Architecture (prototype concept)

```text
Voltage / Current / Temperature Sensors + Physical Tamper Switch
                              |
                              v
                      ESP32 / Sensor Node
                              |
                     Serial or secure link
                              |
                              v
                Data Validation / Preprocessing
                              |
                              v
                 Threshold + Anomaly Analysis
                              |
                              v
                 Alert Log / Dashboard (planned)
```

## Current implementation
- A Python threshold-based detector for simulated sensor readings.
- A sample CSV and unit tests.

## Planned extensions
- ESP32 firmware and calibrated sensors.
- A dashboard and timestamped event log.
- An ML model trained and evaluated on suitable, labelled data.

**Limitation:** External sensor readings alone cannot reliably prove the presence of a hardware Trojan. Real infrastructure deployment requires domain validation, threat modelling, secure communications, and extensive testing.
