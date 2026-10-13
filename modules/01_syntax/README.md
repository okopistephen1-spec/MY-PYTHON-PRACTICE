# Module 01 — Syntax, Comments, Indentation, and Errors

## Learning objectives
- Recognise statements, expressions, and comments.
- Use indentation to define code blocks.
- Distinguish syntax errors from logic errors.

## Statements and expressions
A **statement** tells Python to do something. `score = 7` is an assignment statement. An **expression** produces a value: `3 + 4` evaluates to `7`.

```python
score = 7
print(score + 2)
```

## Comments
A comment begins with `#`. Python ignores the comment text when executing the program.

```python
# This is a comment explaining the next line.
age = 16
```

Use comments to explain why something is done, not to repeat obvious code.

## Indentation
Python uses indentation to show which statements belong to a block.

```python
if True:
    print("Inside the block")
print("Outside the block")
```

The usual convention is four spaces per indentation level. Be consistent.

## Three kinds of problems
- **Syntax error:** Python cannot parse the code, such as a missing closing parenthesis.
- **Runtime error:** the code starts but fails during execution, such as dividing by zero.
- **Logic error:** the code runs but produces the wrong result.

## Practice
1. Write three assignment statements and three print statements.
2. Add comments that explain the purpose of your program.
3. Fix a missing quote, a missing parenthesis, and an indentation mistake in separate experiments.
4. Write code that runs without errors but prints the wrong answer. Explain why it is a logic error.
5. Describe the difference between `=` and `==` (you will study `==` in the operators module).

## Challenge
Create a small “study receipt” program. Print a heading, a divider, three subjects, and a final line. Use comments to separate sections.


## Completion checklist
- [ ] Explain syntax vs runtime vs logic errors
- [ ] Use comments appropriately
- [ ] Use four-space indentation
- [ ] Fix a deliberate syntax error

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
