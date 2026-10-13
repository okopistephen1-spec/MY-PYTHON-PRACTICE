# AI Tutor and Code Marking Guide

Use these prompts with ChatGPT, Claude, Gemini, GitHub Copilot Chat, or another AI assistant. Different tools may give different feedback, so verify advice by running your code.

## 1. Ask for one hint

> I am learning Python fundamentals. I am working on this exercise:
> [paste the exercise]
> I have tried:
> [paste my attempt]
> Give me ONE hint that helps me think through the next step. Do not write the complete solution. Explain the relevant concept in beginner-friendly language.

## 2. Ask an AI to mark your work

> Act as a fair, patient Python instructor. Mark my attempt using the exercise requirements below.
>
> Exercise: [paste the exact instructions]
>
> My code:
> [paste code]
>
> Test output:
> [paste output]
>
> Give a score out of 10 using these criteria:
> - Correctness: 4 points
> - Handling edge cases: 2 points
> - Readability and naming: 2 points
> - Following instructions: 2 points
>
> Identify actual bugs separately from optional style improvements. Explain each issue, suggest test cases, and give hints before revealing a complete solution. Do not assume code works unless the tests or reasoning support that conclusion. Wait for my next attempt before providing a full solution.

## 3. Ask AI to explain an error

> Explain this Python error to a beginner. Tell me what the error message means, what line likely caused it, and how to investigate it. Do not rewrite the entire program. Give me a small debugging step to try.
>
> Code: [paste relevant code]
> Error: [paste the full traceback]

## 4. Ask for a code review after tests pass

> Review this Python code for correctness, edge cases, clarity, naming, and unnecessary complexity. Separate required fixes from optional improvements. Explain why each suggestion matters. Do not replace my whole solution.
>
> Requirements: [paste]
> Code: [paste]
> Tests run and results: [paste]

## 5. Ask AI to generate extra practice

> Create 5 new Python practice questions on [topic], progressing from easy to challenging. Do not show solutions initially. After I submit my attempts, mark each one and explain my mistakes. Include edge cases and make sure the questions are solvable using only the concepts I have learned.

## 6. Ask two AIs to review the same code

1. Give both tools the exact same instructions, code, and test output.
2. Compare the bugs they identify.
3. Ask each to justify claims with a specific line or example.
4. Test the claims yourself.
5. Prefer verified reasoning over confidence or a numerical score.

## 7. Avoid copying without learning

If an AI gives you a solution:
- Close or hide it.
- Rebuild the solution yourself from the requirements.
- Explain each line in your own words.
- Create a test case that was not in the original prompt.

AI can produce incorrect explanations or tests. Your own understanding and executed tests are essential.
