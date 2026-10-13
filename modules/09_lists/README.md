# Module 09 — Lists

## What is a list?
A list stores an ordered collection of values and can be changed after creation.

```python
subjects = ["English", "Biology", "Chemistry"]
subjects.append("Physics")
```

Lists can contain repeated values and different types, although one consistent type often makes data easier to work with.

## Indexing and slicing
```python
print(subjects[0])
print(subjects[-1])
print(subjects[1:3])
```
Accessing a missing index raises `IndexError`.

## Common methods
- `.append(item)` adds one item
- `.extend(items)` adds each item from an iterable
- `.insert(index, item)` inserts at a position
- `.remove(value)` removes the first matching value
- `.pop(index)` removes and returns an item
- `.sort()` sorts the list in place
- `.reverse()` reverses the list in place

`remove()` uses a value; `pop()` uses an index and returns the removed item.

## Mutation and iteration
Changing a list while iterating over that same list can cause items to be skipped. A safer pattern is a list comprehension or a new list:

```python
available = [item for item in resources if item["available"] > 0]
```

## Copying
`second = first` makes both names refer to the same list. `second = first.copy()` creates a shallow copy.

## Practice
1. Create a list of five subjects and print each one.
2. Add an item, insert an item, and remove an item.
3. Find the sum and average of a numeric list.
4. Return a new list containing only positive numbers.
5. Remove duplicates while preserving order (try a loop).
6. Explain the difference between `append()` and `extend()`.
7. Demonstrate the difference between assignment and `.copy()`.
8. Explain why removing items during iteration can skip elements.

## Challenge
Create a resource list with dictionaries. Search for an ID, update the available quantity after a borrow, and return a new list of resources that are currently available.


## Completion checklist
- [ ] Index and slice lists
- [ ] Choose the right list method
- [ ] Explain mutation and copying
- [ ] Avoid mutation-during-iteration bugs

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
