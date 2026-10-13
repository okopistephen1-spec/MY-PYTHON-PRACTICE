# Module 11 — Functions

## Why functions?
Functions package logic under a name so it can be reused, tested, and understood in smaller pieces.

```python
def add(a, b):
    return a + b

answer = add(3, 4)
```

`def` defines a function. `a` and `b` are parameters. `3` and `4` are arguments in this call. `return` sends a result back to the caller.

## print() is not return
`print()` displays a value. `return` provides a value to the code that called the function.

```python
def wrong_add(a, b):
    print(a + b)

def add(a, b):
    return a + b
```
The first function displays a result but returns `None`. The second returns the result.

## Parameters and defaults
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```
A default parameter value is used when that argument is omitted.

## Docstrings
A docstring is a string at the beginning of a function that explains its purpose, parameters, or result.

## Single responsibility
A function is easier to test when it does one clear job. Avoid putting input, calculations, file operations, and lots of printing into one huge function.

## Practice
1. Write `square(number)`.
2. Write `is_even(number)`.
3. Write `calculate_average(numbers)` and decide what an empty list should do.
4. Write `format_greeting(name)` that trims surrounding whitespace.
5. Write a function with a default argument.
6. Create a function that returns a dictionary representing a resource.
7. Explain the difference between printing and returning.
8. Call one function from another.

## Challenge
Refactor a long script into functions for input, calculation, and display. Test the calculation functions separately from user input.


## Completion checklist
- [ ] Define and call functions
- [ ] Distinguish print from return
- [ ] Use parameters and defaults
- [ ] Write clear docstrings

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
