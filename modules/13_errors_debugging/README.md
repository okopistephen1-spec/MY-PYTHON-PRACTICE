# Module 13 — Errors, Exceptions, and Debugging

## Common errors
- `SyntaxError`: invalid Python syntax.
- `NameError`: a name is not defined.
- `TypeError`: an operation is incompatible with the types.
- `ValueError`: the type may be appropriate, but the value is invalid for the operation.
- `IndexError`: a sequence index is out of range.
- `KeyError`: a dictionary key is missing.
- `ZeroDivisionError`: division by zero.

## Read a traceback
Start near the bottom for the exception type and message. Read the file name, line number, and the line of code that failed. Then inspect the values and types used on that line.

## try and except
```python
try:
    quantity = int(user_text)
except ValueError:
    print("Please enter a whole number.")
```
Catch the specific exception you expect. A bare `except:` can hide unrelated problems.

## Validate assumptions
If a quantity must be non-negative, check that requirement. If a resource must exist, search for it and handle the not-found case.

## Debugging method
1. Reproduce the problem.
2. Read the complete error.
3. Identify the exact line.
4. Inspect relevant values with `print()` or a debugger.
5. Make one small change.
6. Run the same test again.
7. Add a test to prevent regression.

## Practice
1. Trigger and explain a `NameError`.
2. Trigger and explain a `TypeError`.
3. Convert invalid text to an integer and catch `ValueError`.
4. Write `safe_divide(a, b)` that returns `None` for a zero divisor.
5. Write `parse_quantity(value)` that returns a non-negative integer or `None`.
6. Fix a list-indexing bug where an ID string is used as a list index.
7. Fix a dictionary `KeyError` using a suitable strategy.
8. Explain why catching every exception can make debugging harder.

## Challenge
Given a buggy borrowing function, list its assumptions, test each assumption, and add validation for missing IDs, non-positive quantities, and insufficient stock.


## Completion checklist
- [ ] Recognise common exception types
- [ ] Read a traceback
- [ ] Catch specific expected errors
- [ ] Validate inputs and reproduce bugs

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
