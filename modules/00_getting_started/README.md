# Module 00 — Getting Started

## Learning objectives
By the end, you should be able to explain what Python is, create a `.py` file, run it, and distinguish the editor from the terminal.

## What is Python?
Python is a programming language: a set of rules for expressing instructions a computer can execute. Python is commonly used for automation, websites, data work, testing, and AI applications.

A Python program is often stored in a file ending in `.py`. For example, `hello.py`.

## Editor versus terminal
- An **editor** is where you write and save code.
- A **terminal** is where you type commands to run programs and manage files.
- The **Python interpreter** reads and executes Python instructions.

## Your first program
Create `hello.py`:

```python
print("Hello, world!")
print("I am learning Python.")
```

Run it from the folder containing the file:

```bash
python3 hello.py
```

The `print()` function displays information. The text in quotes is a string.

## Read error messages carefully
If the terminal says a file cannot be found, check the current folder and spelling. If it says `python3: command not found`, Python may not be installed or available on your PATH.

## Practice
1. Print your favourite subject.
2. Print three separate lines.
3. Print a small two-line introduction.
4. Intentionally misspell `print` and run the file. Read the error, fix it, and run it again.
5. Create a second file and run it from the terminal.
6. Explain in your own words what happens when you run `python3 hello.py`.

## Challenge
Write a program that prints a four-line study plan. Use four separate `print()` calls. Then rewrite it with a single multiline string and compare the approaches.


## Completion checklist
- [ ] Create and run a .py file
- [ ] Use print()
- [ ] Read and fix a simple syntax error
- [ ] Explain editor vs terminal

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
