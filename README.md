# Python Fundamentals — Complete Learning Course

A detailed, practice-first Python course for beginners. Learn a topic, read worked examples, predict what code will do, complete exercises, run tests, and use an AI assistant to review your own work.

**This is a course, not just an exercise list.** Every module includes:
- Lesson notes with explanations and examples
- Common mistakes and debugging advice
- Practice tasks from easy to challenging
- A starter Python file with TODOs
- An exercise checklist
- A suggested review prompt

## Recommended study method

For each lesson:

1. Read the explanation slowly.
2. Type the examples into your own Python file. Do not only copy and paste.
3. Before running each example, predict its output.
4. Change one value and predict the new output.
5. Complete the practice tasks without looking for a full solution.
6. Run the tests, if included.
7. Ask an AI for a hint or review using `AI_TUTOR_GUIDE.md`.
8. Explain the solution aloud or write a short explanation in your own words.
9. Record your progress in `COURSE_TRACKER.md`.
10. Commit your work to Git when you finish a module.

## Prerequisites

No previous programming experience is required. You need:
- A computer
- Python 3.10 or newer
- A code editor such as VS Code
- A terminal
- Patience to practise regularly

On Ubuntu/Linux, check Python with:

```bash
python3 --version
```

Run a file with:

```bash
python3 hello.py
```

## Course map

| Module | Topic |
|---|---|
| 00 | Setup, editor, terminal, and first program |
| 01 | Syntax, comments, indentation, and errors |
| 02 | Variables, assignment, and naming |
| 03 | Data types and type conversion |
| 04 | Operators and expressions |
| 05 | Input, output, and formatted strings |
| 06 | String operations |
| 07 | Boolean logic and conditions |
| 08 | Loops and iteration |
| 09 | Lists |
| 10 | Tuples, sets, and dictionaries |
| 11 | Functions |
| 12 | Scope, parameters, and decomposition |
| 13 | Errors, exceptions, and debugging |
| 14 | Modules, imports, and packages |
| 15 | Files, paths, and JSON |
| 16 | Comprehensions and useful built-ins |
| 17 | Object-oriented programming |
| 18 | Testing and code quality |
| 19 | Git and GitHub workflow |
| 20 | Integrated mini-projects |

## Running your work

Each module has its own `practice.py`. Open a terminal in the repository root and run a file like this:

```bash
python3 modules/03_data_types/practice.py
```

Files containing TODOs are intentionally incomplete. Your job is to fill them in. Some modules include test files. Run them using the command shown in that module's README.

## Rules for learning well

- Do not change tests just to make them pass.
- Do not submit code you cannot explain.
- Try at least 15–25 minutes before requesting a hint.
- Ask for a hint before asking for a complete answer.
- Treat AI output as advice, not as unquestionable truth.
- Never upload passwords, API keys, tokens, or private data.
- If you are stuck, write down what you expected, what happened, and the exact error.

## Repository layout

```text
python-fundamentals-complete-course/
├── README.md
├── COURSE_TRACKER.md
├── AI_TUTOR_GUIDE.md
├── GLOSSARY.md
├── modules/
│   ├── 00_getting_started/
│   ├── 01_syntax/
│   ├── ...
│   └── 20_mini_projects/
└── solutions_policy.md
```

**Suggested pace:** 4–6 study sessions per module. Some topics, especially functions, collections, and object-oriented programming, may need longer. Understanding matters more than speed.
