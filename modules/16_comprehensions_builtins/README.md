# Module 16 — Comprehensions and Built-ins

## List comprehensions
A list comprehension creates a new list from an iterable.

```python
squares = [number * number for number in range(1, 6)]
```

A condition can filter values:
```python
evens = [number for number in range(10) if number % 2 == 0]
```

Use a normal loop when the comprehension becomes difficult to read.

## Dictionary and set comprehensions
```python
square_map = {n: n * n for n in range(1, 4)}
unique_lengths = {len(word) for word in ["cat", "dog", "elephant"]}
```

## Useful built-ins
- `len(items)` count items
- `sum(numbers)` add numbers
- `min(items)` / `max(items)` smallest/largest
- `sorted(items)` return a new sorted list
- `enumerate(items)` provide index and item
- `zip(a, b)` pair items from iterables
- `any(conditions)` true if at least one item is true
- `all(conditions)` true if every item is true

## Practice
1. Create a list of squares from 1 through 10.
2. Filter only positive values from a list.
3. Create a dictionary mapping words to their lengths.
4. Use `enumerate()` to print numbered subjects.
5. Use `zip()` to combine names and scores.
6. Explain the difference between `sort()` and `sorted()`.
7. Use `any()` to check whether a resource is low stock.
8. Rewrite a simple loop as a comprehension, then decide which version is clearer.

## Challenge
Given a list of resource dictionaries, create a list of names for resources with stock, a dictionary of available quantities, and a Boolean indicating whether all resources have non-negative stock.


## Completion checklist
- [ ] Write list comprehensions
- [ ] Use dictionary/set comprehensions
- [ ] Know common built-ins
- [ ] Choose readability over cleverness

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
