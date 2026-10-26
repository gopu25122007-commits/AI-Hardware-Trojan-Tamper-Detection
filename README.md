# AI-Powered Hardware Trojan and Tamper Detection

Educational proof-of-concept for monitoring simulated voltage, current, temperature, and physical tamper events in critical-infrastructure equipment.

> **Status:** Starter prototype using threshold rules and simulated data. It does not yet include a trained AI/ML model, ESP32 firmware, or a live dashboard, and it is not validated for real critical infrastructure.

## Features
- Checks simulated voltage, current, and temperature readings against configurable ranges.
- Flags a physical tamper-switch event.
- Includes sample data and automated unit tests.
- Documents a proposed system architecture.

## Requirements
- Python 3.9 or later
- No third-party packages required

## Setup
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the demo:

   ```bash
   python src/main.py
   ```

4. Run tests:

   ```bash
   python -m unittest discover -s tests -v
   ```

## Project structure
- `src/detector.py` — threshold and tamper-event logic
- `src/main.py` — simulated demo
- `data/sample_readings.csv` — illustrative sample readings
- `tests/test_detector.py` — unit tests
- `docs/ARCHITECTURE.md` — architecture and limitations
- `LICENSE` — MIT license

## Safety and limitations
This project is for education and prototype demonstration only. Values and limits are illustrative, not engineering specifications. Threshold alerts are not proof of a hardware Trojan and may produce false positives or miss threats. Do not connect this prototype to live infrastructure without qualified engineering, security review, and validation.

## Roadmap
1. Integrate a physical tamper switch and calibrated sensors with an ESP32.
2. Record timestamped sensor readings from controlled bench tests.
3. Add a dashboard and secure event logging.
4. Evaluate an anomaly-detection model using suitable labelled datasets.

## License
MIT; see `LICENSE`.
