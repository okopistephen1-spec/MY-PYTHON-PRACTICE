# Module 03 — Data Types and Type Conversion

## Learning objectives
Recognise common built-in types, inspect a value's type, and convert between compatible types.

## Core types
- `int`: whole numbers, such as `8` or `-2`
- `float`: numbers with a fractional component, such as `3.5` or `5.0`
- `str`: text, such as `"Python"`
- `bool`: `True` or `False`
- `NoneType`: the type of `None`, used to represent the absence of a value

```python
print(type(10))       # <class 'int'>
print(type(10 / 2))   # <class 'float'>
print(10 // 2)        # 5
```

In Python 3, `/` performs true division and returns a float, even when the answer is mathematically a whole number. `//` performs floor division.

## Type conversion
```python
age_text = "17"
age = int(age_text)
height = float("1.72")
message = str(17)
```
`int("hello")` raises `ValueError`, because the text does not represent an integer.

## Values and types are different
`"5"` is text; `5` is an integer. They look similar when printed, but Python treats them differently.

## Practice
1. Print the type of an integer, a float, a string, a boolean, and `None`.
2. Convert `"42"` to an integer and add 8.
3. Convert `"3.5"` to a float and multiply it by 2.
4. Explain why `input()` usually gives you a string, even if the user types `10`.
5. Predict the types of `7 / 2`, `7 // 2`, `7 % 2`, and `float(4)`.
6. Experiment with `int("3.9")` and explain the error.
7. Write a function that receives a numeric string and returns the integer plus one. Decide what should happen if the string is invalid.

## Challenge
Build a unit converter that converts a number of minutes into whole hours and remaining minutes. Decide what type its result should use.


## Completion checklist
- [ ] Identify int, float, str, bool, and None
- [ ] Explain / versus //
- [ ] Convert compatible types
- [ ] Recognise ValueError from invalid conversion

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
