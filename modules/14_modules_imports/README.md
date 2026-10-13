# Module 14 — Modules, Imports, and Packages

## What is a module?
A module is a Python file. If `weather_service.py` contains functions, another file can import them.

```python
import math
print(math.sqrt(25))
```

You can import a module or selected names:
```python
from math import sqrt
print(sqrt(25))
```

Using `import module_name` makes it clear where a name came from. Avoid wildcard imports in beginner projects because they can make names confusing.

## Your own module
Suppose `helpers.py` contains:
```python
def double(number):
    return number * 2
```
A nearby Python file can use:
```python
import helpers
print(helpers.double(4))
```

The module file must be discoverable by Python, usually because it is in the same project folder or installed as a package.

## The main guard
```python
def main():
    print("Run the program")

if __name__ == "__main__":
    main()
```
This runs `main()` when the file is executed directly, but not merely when it is imported.

## Packages and pip
A package is a way of organising related modules. `pip` installs third-party packages into your Python environment. The Python standard library, such as `math`, does not usually need separate installation.

## Practice
1. Import `math` and use `sqrt`, `ceil`, and `floor`.
2. Create `greetings.py` with a greeting function and import it from another file.
3. Explain the difference between executing and importing a file.
4. Add a main guard to a small script.
5. Investigate `ModuleNotFoundError` and check spelling and file location.
6. Explain why `return "import weather_service"` is different from executing an import statement.

## Challenge
Split a small inventory project into `inventory.py` (functions) and `main.py` (user interaction). Keep calculations separate from display logic.


## Completion checklist
- [ ] Import standard-library modules
- [ ] Create and import a local module
- [ ] Use the main guard
- [ ] Understand ModuleNotFoundError

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
