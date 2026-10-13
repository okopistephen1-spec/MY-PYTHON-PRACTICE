# Module 12 — Scope, Parameters, and Decomposition

## Scope
Scope describes where a name can be accessed. Names created inside a function are normally local to that function.

```python
def example():
    message = "inside"
    return message
```
Trying to use `message` outside the function will usually raise `NameError`, because it is local.

Avoid relying on global variables for ordinary function inputs. Pass the values a function needs as parameters and return results.

## Parameters versus arguments
In `def greet(name):`, `name` is a parameter. In `greet("Ada")`, `"Ada"` is an argument.

## Decomposition
Decomposition means splitting a larger task into smaller tasks. For an inventory program, you might create:
- `find_resource()`
- `borrow_resource()`
- `return_resource()`
- `inventory_summary()`

Each function can be tested independently.

## Mutable default argument warning
Avoid defaults such as `def add_item(item, items=[]):`. That same list can be reused across calls. Prefer `None` and create a new list inside the function when needed.

## Practice
1. Write a function that receives all needed values through parameters.
2. Create two functions: one calculates a subtotal, another formats a receipt.
3. Demonstrate why a local variable cannot normally be accessed outside its function.
4. Split a ticket-priority script into input, calculation, and display functions.
5. Explain why global variables can make tests and debugging harder.
6. Rewrite a mutable-list default argument safely.

## Challenge
Plan a resource borrowing program as a set of small functions. For each function, write its inputs, output, and responsibilities before implementing it.


## Completion checklist
- [ ] Explain local scope
- [ ] Pass dependencies through parameters
- [ ] Break large tasks into functions
- [ ] Avoid mutable default arguments

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
