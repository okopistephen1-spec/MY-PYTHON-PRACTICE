# Module 02 — Variables and Assignment

## Learning objectives
Understand variable assignment, naming rules, reassignment, and naming style.

## What is a variable?
A variable is a name that refers to a value. In `score = 12`, Python binds the name `score` to the integer value `12`.

```python
score = 12
score = score + 3
print(score)  # 15
```

The second line calculates the old value plus three, then assigns the result back to `score`.

## Naming rules
Names may contain letters, digits, and underscores, but cannot begin with a digit. Names are case-sensitive: `score` and `Score` are different names. Python keywords such as `if` and `for` cannot be used as variable names.

Prefer descriptive `snake_case` names:
```python
student_name = "Ada"
number_of_books = 4
```

Avoid unclear names such as `x1` when a meaningful name is possible.

## Multiple assignment
```python
name, age = "Ada", 17
```
This assigns one value to each name. Use it when the relationship is clear.

## Common mistakes
- Using a name before assigning a value.
- Misspelling a name (`total_score` versus `total_socre`).
- Confusing `=` (assignment) with `==` (comparison).
- Naming a variable `list`, `str`, or `sum`, which hides a useful built-in name.

## Practice
1. Store a name, age, and favourite subject in variables and print them.
2. Create `price` and `quantity`; calculate `total_cost`.
3. Start with `points = 0`, add 5, then subtract 2. Print the final value.
4. Swap two variables using multiple assignment.
5. Rename unclear variables to meaningful `snake_case` names.
6. Predict the output of:
   `count = 2; count = count * 3; count = count + 1`.

## Challenge
Create a simple shopping receipt using variables for two item prices and quantities. Calculate the subtotal. Do not hard-code the final subtotal.


## Completion checklist
- [ ] Use descriptive variable names
- [ ] Explain reassignment
- [ ] Calculate a value using variables
- [ ] Avoid shadowing built-in names

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
