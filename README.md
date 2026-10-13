# Python Practice Lab 🐍

A beginner-friendly Python exercise repository. Work through the exercises in order, test your solutions, track your progress, and use AI as a code reviewer—not as a replacement for your own thinking.

## Start here

1. Open this folder in VS Code.
2. Make sure Python 3 is installed.
3. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Install the test tool:
   ```bash
   python -m pip install pytest
   ```
5. Open an exercise file and replace `pass` / `NotImplementedError` with your own solution.
6. Run the tests for that exercise. Example:
   ```bash
   python -m pytest 01-basics/test_basics.py -q
   ```
7. When you're happy with your solution, update `PROGRESS.md` and commit your work to Git.

> Tests are expected to fail until you implement the exercises. That is normal.

## Learning path

| Folder | Main skills |
|---|---|
| `01-basics` | strings, numbers, operators |
| `02-control-flow` | conditions and loops |
| `03-functions` | functions, parameters, return values |
| `04-data-structures` | lists and dictionaries |
| `05-debugging` | validation and exceptions |
| `06-mini-projects` | combining skills in a small program |

Each exercise includes an instruction file, a starter Python file, tests, and hints. Do not open `hints.md` until you've made a genuine attempt.

## AI marking workflow

1. Try the exercise first.
2. Run its tests.
3. If you are stuck, share the exercise description and your own code with an AI assistant.
4. Ask for feedback and hints before asking for a full solution.
5. Apply one correction at a time, then rerun the tests.

See [`AI_MARKING_PROMPT.md`](AI_MARKING_PROMPT.md) for a reusable marking prompt.

## Test everything

From the repository root:
```bash
python -m pytest -q
```
Some tests will fail while exercises are unfinished. As you solve them, the number of passing tests should increase.

## Suggested rules for yourself

- Spend at least 15–25 minutes trying before asking AI for a full answer.
- Explain your solution in your own words.
- Test normal inputs, boundary cases, and invalid inputs when appropriate.
- Don't paste API keys, passwords, or private information into public repositories or AI chats.
- AI can be wrong. Use tests and your own reasoning to verify feedback.

## Folder structure

```text
python-practice/
├── README.md
├── PROGRESS.md
├── AI_MARKING_PROMPT.md
├── .gitignore
├── requirements.txt
├── 01-basics/
├── 02-control-flow/
├── 03-functions/
├── 04-data-structures/
├── 05-debugging/
└── 06-mini-projects/
```
