import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from detector import Reading, analyse_reading


class DetectorTests(unittest.TestCase):
    def test_normal_reading(self):
        result = analyse_reading(Reading(5.0, 0.5, 30.0, False))
        self.assertEqual(result["status"], "NORMAL")
        self.assertEqual(result["reasons"], [])

    def test_voltage_out_of_range(self):
        result = analyse_reading(Reading(6.0, 0.5, 30.0, False))
        self.assertEqual(result["status"], "ALERT")
        self.assertIn("voltage_out_of_range", result["reasons"])

    def test_tamper_event(self):
        result = analyse_reading(Reading(5.0, 0.5, 30.0, True))
        self.assertIn("physical_tamper_detected", result["reasons"])


if __name__ == "__main__":
    unittest.main()
