# Python Fundamentals — Complete Learning Course 🐍

Welcome to your Python learning journey!

This repository contains a detailed, practice-first Python course for beginners. Learn Python from the fundamentals through functions, data structures, debugging, object-oriented programming, testing, Git, and mini-projects.

This is a complete learning course, not just a collection of exercises. Every module combines explanations, worked examples, practice exercises, and opportunities to test your understanding.

## What You Will Learn

By completing this course, you will learn how to:

- Understand Python syntax and write readable code.
- Work with variables, data types, and operators.
- Receive input and display output.
- Manipulate strings and collections.
- Make decisions using conditional statements.
- Repeat tasks using loops.
- Write reusable functions.
- Handle errors and debug programs.
- Organize code using modules and packages.
- Read and write files and JSON data.
- Understand object-oriented programming.
- Write and run tests.
- Use Git and GitHub to manage your projects.
- Build small projects that combine your skills.

## Getting Started

### Requirements

You need:

- Python 3.10 or newer.
- A code editor such as VS Code.
- A terminal.
- A willingness to practise and learn from mistakes.

### Check Your Python Installation

On Ubuntu or another Linux distribution, open your terminal and run:

```bash
python3 --version
```

You should see your installed Python version.

### Open the Project

Open this repository in VS Code.

You can also navigate to the project directory in your terminal and run:

```bash
code .
```

### Create a Virtual Environment

A virtual environment keeps project dependencies separate from other Python projects.

Create one with:

```bash
python3 -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

If you need to install the testing tool, run:

```bash
python -m pip install pytest
```

You do not need to install additional packages for every module. Install dependencies only when the relevant lesson requires them.

## Course Roadmap

The course is organized into 21 modules.

| Module | Topic |
|---|---|
| 00 | Getting started, setup, editor, and terminal |
| 01 | Syntax, comments, indentation, and errors |
| 02 | Variables, assignment, and naming |
| 03 | Data types and type conversion |
| 04 | Operators and expressions |
| 05 | Input, output, and formatted strings |
| 06 | String operations |
| 07 | Boolean logic and conditional statements |
| 08 | Loops and iteration |
| 09 | Lists |
| 10 | Tuples, sets, and dictionaries |
| 11 | Functions |
| 12 | Scope, parameters, and breaking problems into smaller parts |
| 13 | Errors, exceptions, and debugging |
| 14 | Modules, imports, and packages |
| 15 | Files, paths, and JSON |
| 16 | Comprehensions and useful built-in functions |
| 17 | Object-oriented programming |
| 18 | Testing and code quality |
| 19 | Git and GitHub workflow |
| 20 | Integrated mini-projects |

Explore the `modules/` directory to find the lessons and exercises.

## How to Study Each Module

Follow this process for every lesson:

1. Read the lesson notes carefully.
2. Type the worked examples into your own Python files.
3. Predict the output before running each example.
4. Change some values and predict what will happen.
5. Complete the exercises without immediately looking for answers.
6. Run any provided tests.
7. Debug errors and understand why they occurred.
8. Ask an AI assistant to review your code if necessary.
9. Explain your solution in your own words.
10. Record your progress in `COURSE_TRACKER.md`.
11. Commit your completed work to Git when appropriate.

**Understanding the code is more important than finishing quickly.**

## Running Your Exercises

Each module has a `practice.py` file.

For example, to run the data types practice file from the repository root:

```bash
python3 modules/03_data_types/practice.py
```

The exact filename and path depend on the module you are studying.

Some starter files intentionally contain `pass`, TODO comments, or incomplete functions. These are places where you are expected to write your own code.

## Testing Your Solutions

Some modules provide automated tests.

If a module contains a test file, follow the instructions in that module's README.

For example:

```bash
python -m pytest path/to/test_file.py -q
```

To run all available tests, you can use:

```bash
python -m pytest -q
```

Run the full test suite from the repository root.

Tests may fail while exercises remain incomplete. That is normal. Your goal is to understand the failures and improve your solutions.

**Do not change tests simply to make them pass.** Fix your implementation instead.

## Using AI to Review Your Code

You can use ChatGPT or another AI assistant as a learning partner.

For the best results:

1. Attempt the exercise yourself first.
2. Run your code and inspect the output.
3. Share the exercise instructions and your implementation.
4. Ask the AI to identify mistakes and explain why they occur.
5. Request a hint before requesting a complete solution.
6. Correct one problem at a time.
7. Run your tests again.
8. Explain the final solution in your own words.

See `AI_TUTOR_GUIDE.md` for more guidance.

Remember that AI-generated feedback can be incorrect. Verify suggestions by running your code and reasoning through the results.

## Recommended Learning Rules

- Spend at least 15–25 minutes attempting an exercise before requesting a full solution.
- Do not submit code you cannot explain.
- Test ordinary inputs and edge cases where appropriate.
- Read error messages carefully.
- Learn to distinguish syntax errors, runtime errors, and logic errors.
- Keep your code readable.
- Never upload passwords, API keys, access tokens, or other secrets.
- Use Git to save meaningful milestones.
- Ask questions whenever a concept is unclear.

## Repository Structure

```text
python-fundamentals-complete-course/
├── README.md
├── AI_TUTOR_GUIDE.md
├── COURSE_TRACKER.md
├── GLOSSARY.md
├── solutions_policy.md
└── modules/
    ├── 00_getting_started/
    ├── 01_syntax/
    ├── 02_variables/
    ├── 03_data_types/
    ├── ...
    └── 20_mini_projects/
```

The `modules/` directory contains the course lessons, worked examples, starter files, and exercises.

## Track Your Progress

Use `COURSE_TRACKER.md` to record the modules you have studied and the exercises you have completed.

Do not rush through the course just to mark every module as complete. Make sure you understand the important concepts before moving forward.

## Suggested Study Pace

Spend approximately 4–6 study sessions on each module, adjusting the pace according to its difficulty.

Topics such as functions, collections, debugging, and object-oriented programming may require more practice.

Consistency, curiosity, and patience will help you improve.

## Start Learning

Begin with **Module 00: Getting Started**.

Work through the modules in order, practise consistently, and gradually build your confidence as a Python programmer.

Happy coding! 🚀