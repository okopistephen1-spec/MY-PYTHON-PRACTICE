import unittest
from practice import describe_value, minutes_to_hours

class DataTypeTests(unittest.TestCase):
    def test_describe_value(self):
        self.assertEqual(describe_value(4), {"value": 4, "type": "int", "text": "4"})
        self.assertEqual(describe_value("hi"), {"value": "hi", "type": "str", "text": "hi"})

    def test_minutes(self):
        self.assertEqual(minutes_to_hours(135), (2, 15))
        self.assertEqual(minutes_to_hours(60), (1, 0))
        self.assertEqual(minutes_to_hours(0), (0, 0))

if __name__ == "__main__":
    unittest.main()
