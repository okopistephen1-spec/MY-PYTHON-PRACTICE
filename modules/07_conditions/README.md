# Module 07 — Boolean Logic and Conditions

## Why conditions matter
Programs often need to make decisions. An `if` statement runs its block only when the condition is truthy.

```python
score = 72
if score >= 50:
    print("Pass")
else:
    print("Try again")
```

## if, elif, else
Use `elif` when checking another mutually exclusive case.

```python
if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"
```

Order matters. If an earlier condition catches too many cases, later branches may never run.

## Combining conditions
```python
if urgency == "high" and affected_users >= 10:
    priority = "critical"
```
Normalise text with `.lower()` when uppercase/lowercase should not matter.

## Truthiness
Empty strings, zero, empty collections, and `None` are false-like in conditions. Non-empty strings and non-zero numbers are generally true-like. Prefer explicit comparisons when they make the intent clearer.

## Practice
1. Check whether a number is positive, negative, or zero.
2. Classify a score into grade bands.
3. Check whether a number is within an inclusive range.
4. Implement ticket priority rules: critical, high, medium, low.
5. Check whether a username is empty after trimming whitespace.
6. Test boundary values such as 49/50 and 59/60.
7. Explain why the order of `if` and `elif` branches matters.

## Challenge
Write `calculate_priority(urgency, affected_users)`. Test mixed-case urgency, exactly 10 users, and a low urgency with fewer than 10 users. Decide how to handle negative user counts and document your decision.


## Completion checklist
- [ ] Write if/elif/else branches
- [ ] Combine conditions
- [ ] Test boundary values
- [ ] Explain branch ordering

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
