# Modules, Imports, and Packages — Worked Examples

Use these examples to understand the style of solution expected. Type each example into Python and change the values.

## Example 1: A tiny function

```python
def double(number):
    return number * 2

print(double(4))
```

Reasoning:
1. `def` defines a function.
2. `number` receives the argument `4`.
3. `number * 2` evaluates to `8`.
4. `return` sends `8` back to the caller.
5. `print()` displays that returned value.

## Example 2: Work through the steps

Before running a program, make a small trace table with columns for the variable values and output. Update the table after each statement. This helps you see how Python executes code rather than guessing.

## Example 3: Test a boundary

For any rule with a threshold, test the value just below it, exactly at it, and just above it. For a threshold of 10, test 9, 10, and 11. This is a reliable habit for conditions, loops, validation, and inventory rules.

## Your task
Write two additional examples from this module. For each one, include:
- The code
- The expected output
- A plain-English explanation
- One changed input and its new expected output
