"""Run a small simulated sensor demo from the command line."""
import json
from detector import Reading, analyse_reading


def main():
    examples = [
        Reading(5.0, 0.6, 35.0, False),
        Reading(6.2, 2.8, 78.0, True),
    ]
    for index, reading in enumerate(examples, start=1):
        result = analyse_reading(reading)
        print(json.dumps({"sample": index, "reading": reading.__dict__, **result}, indent=2))


if __name__ == "__main__":
    main()
