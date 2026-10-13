# Module 05 — Input, Output, and Formatting

## Output with print()
`print()` displays values. It can display several values separated by spaces:

```python
name = "Ada"
score = 95
print(name, score)
```

## Input with input()
`input()` displays a prompt and returns the entered text as a string.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

If you expect a number, convert it:
```python
age = int(input("Enter your age: "))
```
This can fail if the user types non-numeric text. You will learn safe validation in the exception-handling module.

## F-strings
Put `f` before the opening quote and place expressions inside braces.

```python
price = 1250
quantity = 3
print(f"Total: {price * quantity}")
```

For decimal formatting, `f"{value:.2f}"` displays two digits after the decimal point.

## Practice
1. Ask the user for a name and greet them.
2. Ask for two integers and print their sum.
3. Ask for length and width and display the area.
4. Display a receipt with item name, quantity, unit price, and total.
5. Format a floating-point price to two decimal places.
6. Explain why `"10" + "5"` differs from `10 + 5`.
7. Consider what should happen if a user enters `abc` when asked for a number.

## Challenge
Make a command-line ticket priority intake: ask for urgency and affected users, convert the user count to an integer, then display a formatted summary. Handle invalid input in a later revision.


## Completion checklist
- [ ] Use input() and print()
- [ ] Convert numeric input
- [ ] Use f-strings
- [ ] Format decimal values

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
