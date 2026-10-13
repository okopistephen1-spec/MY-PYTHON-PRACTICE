import unittest
from practice import square, calculate_average, format_greeting

class FunctionTests(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(-3), 9)

    def test_average(self):
        self.assertEqual(calculate_average([2, 4, 6]), 4)
        self.assertIsNone(calculate_average([]))

    def test_greeting(self):
        self.assertEqual(format_greeting(" Ada "), "Hello, Ada!")

if __name__ == "__main__":
    unittest.main()
