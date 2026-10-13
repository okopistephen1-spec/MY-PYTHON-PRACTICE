# Module 06 — String Operations

## Strings
A string is a sequence of characters. Strings can use single or double quotes:

```python
language = "Python"
```

Strings are immutable: methods create new strings rather than changing the original string in place.

## Indexing and slicing
Indexes start at zero.

```python
word = "Python"
print(word[0])    # P
print(word[-1])   # n
print(word[1:4])  # yth
```
The end of a slice is excluded. Slicing beyond the string's end is often safe; indexing a missing position raises `IndexError`.

## Useful methods
- `.lower()` and `.upper()`
- `.strip()` removes whitespace at both ends
- `.replace(old, new)`
- `.split(separator)` creates a list
- `.join(items)` joins strings
- `.startswith(prefix)` and `.endswith(suffix)`

```python
username = "  Ada  ".strip().lower()
```

## Membership
`"py" in "python"` is `True`; membership is case-sensitive.

## Practice
1. Print the first and last characters of a word.
2. Extract the first three characters from a string.
3. Clean `"  Hello Python  "` using `strip()`.
4. Convert a name to lowercase, then create a title-case version.
5. Count how many times a chosen letter appears.
6. Split a comma-separated string into items and strip each item.
7. Check whether an email-like string ends with a chosen domain. This is only string practice, not full email validation.
8. Write a function that returns `"Hello, NAME!"`, trimming spaces around the name.

## Challenge
Create a simple username normaliser: trim spaces, convert to lowercase, and replace internal spaces with underscores. Test empty strings and names with multiple spaces.


## Completion checklist
- [ ] Use indexes and slices
- [ ] Explain why strings are immutable
- [ ] Use strip/lower/split/join
- [ ] Handle empty strings and case differences

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
