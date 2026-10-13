# Module 04 — Operators and Expressions

## Arithmetic operators
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` true division
- `//` floor division
- `%` remainder
- `**` exponentiation

```python
print(2 ** 3)  # 8
print(17 % 5)  # 2
```

The remainder operator is useful for checking evenness: `number % 2 == 0`.

## Comparison operators
`==`, `!=`, `<`, `<=`, `>`, `>=` compare values and produce booleans.

Do not confuse `=` (assign a value) with `==` (compare two values).

## Logical operators
- `and`: both conditions must be true
- `or`: at least one condition must be true
- `not`: reverses a boolean result

```python
age = 16
has_permission = True
print(age >= 13 and has_permission)
```

## Assignment shortcuts
`score += 1` means `score = score + 1`. Similar forms include `-=`, `*=`, and `/=`.

## Operator precedence
Python follows precedence rules, but parentheses make complex expressions clearer.

```python
result = (2 + 3) * 4
```

## Practice
1. Calculate the area and perimeter of a rectangle.
2. Given a number, return its quotient and remainder when divided by 3.
3. Check whether a number is even.
4. Write an expression that is true when a score is at least 50 and attendance is at least 75.
5. Predict `True or False and False`; then use parentheses to show your intended logic.
6. Compare two values and print whether they are equal.
7. Write a simple discount condition using `and` and `or`.

## Challenge
A ticket is critical if urgency is `"high"` and at least 10 users are affected. It is high if urgency is high or at least 10 users are affected. Write the Boolean expressions before writing the full function.


## Completion checklist
- [ ] Use arithmetic operators correctly
- [ ] Compare values with == and >
- [ ] Combine conditions with and/or/not
- [ ] Use parentheses to make logic clear

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
