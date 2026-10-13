# Module 18 — Testing and Code Quality

## Why test?
A program that works for one example may fail for another. Tests check expected behaviour repeatedly, making regressions easier to catch.

## Assertions
```python
assert 2 + 2 == 4
```
An assertion fails when the condition is false. For larger projects, use a test framework.

## unittest
```python
import unittest

def square(n):
    return n * n

class SquareTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square(3), 9)

if __name__ == "__main__":
    unittest.main()
```

Useful assertions include `assertEqual`, `assertTrue`, `assertFalse`, `assertIsNone`, and `assertRaises`.

## Test categories
- Normal cases
- Boundary cases
- Empty input
- Invalid input
- Missing records
- Large or unusual values
- State changes, such as borrowing then returning an item

## Testable design
Functions that accept inputs and return results are often easier to test than functions that directly ask for input and print everything. Keep interaction separate from business logic.

## Practice
1. Write tests for a function that checks even numbers.
2. Test a function with empty lists and one-item lists.
3. Test ticket priority at exactly 10 affected users.
4. Test that borrowing more than available stock does not reduce stock.
5. Test that returning items cannot increase availability beyond total stock.
6. Write a test that expects a particular exception.
7. Read a failing test and use the failure message to debug.

## Challenge
Write a test suite for an inventory tracker before adding new features. Include successful borrowing, insufficient stock, unknown IDs, invalid quantities, and a complete return.


## Completion checklist
- [ ] Write unit tests
- [ ] Test normal and edge cases
- [ ] Interpret assertion failures
- [ ] Separate logic from user interaction

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
