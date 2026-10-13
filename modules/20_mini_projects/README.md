# Module 20 — Integrated Mini-Projects

These projects combine topics from earlier modules. Do them in order and write requirements before coding. You do not need to use classes in every project; choose the simplest design that meets the requirements.

## Project 1: Grade Calculator
Requirements:
- Accept a list of scores.
- Validate that scores are in a chosen range.
- Calculate the average.
- Return a grade category using documented boundaries.
- Show a clear summary.
- Test empty input and boundary scores.

Extensions: accept multiple students and find the class average.

## Project 2: Command-Line Quiz
Requirements:
- Store questions and correct answers in a suitable collection.
- Ask questions one at a time.
- Count correct answers.
- Display the final score.
- Normalise answers where appropriate.
- Keep question data separate from the quiz logic.

Extensions: shuffle questions, track incorrect answers, and save a result to JSON.

## Project 3: Resource Borrowing Tracker
Requirements:
- Store resource ID, name, total quantity, and available quantity.
- Find a resource by ID.
- Borrow a positive quantity only when sufficient stock exists.
- Return a positive quantity without exceeding the total.
- Report total, available, borrowed, and low-stock units.
- Handle unknown IDs and invalid input.
- Test every important rule.

Extensions: save data in JSON; add a command-line menu; later refactor into classes.

## Project 4: Personal Expense Tracker
Requirements:
- Record description, category, and amount.
- List all expenses.
- Calculate total expenses.
- Calculate totals by category.
- Reject invalid or negative amounts according to your stated rules.
- Save and load records from JSON.

Extensions: filter by category and display the largest expense.

## Project 5: Ticket Priority Manager
Requirements:
- Accept ticket urgency and affected-user count.
- Calculate priority using a clearly documented rule.
- Store tickets in a list of dictionaries.
- Search tickets by ID.
- Display a summary by priority.
- Test boundary values and invalid data.

Extensions: add ticket status, assign a ticket to a person, and save records to a file.

## How to approach any project
1. Write requirements in plain English.
2. Identify inputs, outputs, and rules.
3. Write 5–10 test cases before implementing everything.
4. Design small functions.
5. Implement one function at a time.
6. Run tests after each change.
7. Ask AI to review your code without immediately rewriting it.
8. Update the README with installation and usage instructions.
9. Commit your finished project to Git.
10. Write a short retrospective: what worked, what failed, and what you would improve.

## Final challenge
Choose one project and make it your own. Add one useful feature that was not listed, explain the feature in the README, and add tests for it.


## Completion checklist
- [ ] Complete at least two mini-projects
- [ ] Write a README with run instructions
- [ ] Include tests and edge cases
- [ ] Explain design decisions

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
