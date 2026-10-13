import unittest
from practice import classify_number, calculate_priority

class ConditionTests(unittest.TestCase):
    def test_number(self):
        self.assertEqual(classify_number(3), "positive")
        self.assertEqual(classify_number(-1), "negative")
        self.assertEqual(classify_number(0), "zero")

    def test_priority(self):
        self.assertEqual(calculate_priority("high", 10), "critical")
        self.assertEqual(calculate_priority("HIGH", 2), "high")
        self.assertEqual(calculate_priority("low", 10), "high")
        self.assertEqual(calculate_priority("medium", 2), "medium")
        self.assertEqual(calculate_priority("low", 2), "low")

if __name__ == "__main__":
    unittest.main()
