# Module 08 — Loops and Iteration

## for loops
A `for` loop visits items in an iterable.

```python
for subject in ["English", "Biology", "Chemistry"]:
    print(subject)
```

`range(stop)` produces integers starting at zero and ending before `stop`. `range(1, 6)` produces 1 through 5.

## while loops
A `while` loop repeats as long as its condition remains true.

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

If the condition never becomes false, you may create an infinite loop. Make sure the loop progresses toward stopping.

## break and continue
- `break` exits the nearest loop.
- `continue` skips the rest of the current iteration and moves to the next one.

Use these when they make the logic clearer; don't add them unnecessarily.

## Accumulators and counters
An accumulator stores a running total. A counter records how many matching items have been seen.

```python
total = 0
for number in [2, 4, 6]:
    total += number
```

## Practice
1. Print numbers 1 through 20.
2. Sum all positive numbers in a list.
3. Count vowels in a string.
4. Print a multiplication table.
5. Find the largest number without using `max()`.
6. Count how many values are even.
7. Use a `while` loop to count down from 5 to 1.
8. Skip negative values with `continue`.
9. Explain how an accidental infinite loop can happen.

## Challenge
Ask for numbers until the user types `done`, then display the sum and count. First write the loop using sample data, then add user input and validation.


## Completion checklist
- [ ] Use for and while
- [ ] Use range correctly
- [ ] Build counters and accumulators
- [ ] Avoid accidental infinite loops

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
