# Module 10 — Tuples, Sets, and Dictionaries

## Tuples
Tuples are ordered collections that cannot be reassigned item-by-item after creation.

```python
coordinates = (7.18, 8.14)
hours, minutes = (2, 15)
```
Tuples are useful for fixed groups of related values.

## Sets
Sets store unique hashable values. They are useful for removing duplicates and checking membership.

```python
topics = {"loops", "functions", "loops"}
print(topics)  # one copy of each value; display order is not guaranteed
```

Sets support union (`|`), intersection (`&`), and difference (`-`).

## Dictionaries
A dictionary maps keys to values.

```python
resource = {"id": "R001", "name": "Laptop", "available": 7}
print(resource["name"])
resource["available"] = 6
```

Use `.get(key)` if a key might be absent and you want a default rather than a `KeyError`.

- `dictionary.keys()` gives keys
- `dictionary.values()` gives values
- `dictionary.items()` gives key-value pairs

Dictionary keys must be hashable. Strings are common keys.

## A common list/dictionary mistake
If `resources` is a list of dictionaries, `resources[0]` accesses the first item by integer index. It does not mean `resources["R001"]`. Search for the dictionary whose `"id"` value matches.

## Practice
1. Pack hours and minutes into a tuple and unpack them.
2. Remove duplicate words using a set.
3. Count how often each word occurs using a dictionary.
4. Look up a resource by ID in a list of dictionaries.
5. Use `.get()` for a missing key.
6. Calculate total, available, and borrowed units from resource records.
7. Find common items in two sets.
8. Explain when a tuple is more suitable than a list.

## Challenge
Build an inventory summary containing total units, available units, borrowed units, and low-stock resource names. Test an empty inventory and a resource with zero available units.


## Completion checklist
- [ ] Explain tuple/list differences
- [ ] Use sets for uniqueness
- [ ] Read and update dictionaries
- [ ] Search a list of dictionaries correctly

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
