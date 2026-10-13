# Module 15 — Files, Paths, and JSON

## Why files?
Variables usually exist only while a program is running. Files let a program store information between runs.

## Context managers
Use `with open(...)` so Python closes the file even if an error occurs.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Practise Python\n")
```

Common modes:
- `"r"` read
- `"w"` write, replacing existing content
- `"a"` append
- `"x"` create only if the file does not exist

Be careful: `"w"` can overwrite a file.

## Reading
```python
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
```
Use `.readlines()` or iterate over the file when line-by-line processing is useful.

## JSON
JSON can represent strings, numbers, booleans, lists, dictionaries with string keys, and null values.

```python
import json

data = {"name": "Laptop", "available": 7}
with open("inventory.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)
```
To load it, use `json.load(file)`. Handle missing files and malformed JSON when appropriate.

## Paths
The `pathlib` module provides tools for paths:
```python
from pathlib import Path
path = Path("data") / "notes.txt"
```

## Practice
1. Write three lines to a text file.
2. Read a file and count its lines.
3. Append a new note without replacing existing notes.
4. Save a list of dictionaries to JSON and load it again.
5. Handle a missing file gracefully.
6. Explain the difference between write and append mode.
7. Think about why passwords should not be stored as plain text in a practice project.

## Challenge
Save resource inventory data in JSON. On startup, load the file if it exists; otherwise start with an empty list. After a successful borrow or return, save the updated data.


## Completion checklist
- [ ] Use with open
- [ ] Choose correct file modes
- [ ] Read and write JSON
- [ ] Handle file and parsing errors

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
