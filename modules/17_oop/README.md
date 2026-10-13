# Module 17 — Object-Oriented Programming

## What is an object?
An object combines data and behaviour. A class describes how objects of a particular kind are created and what they can do.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}."
```

`Student` is a class. `student = Student("Ada")` creates an instance. `self` refers to the particular instance. `__init__` initialises a new object.

## Attributes and methods
`student.name` accesses an attribute. `student.greet()` calls a method.

## Encapsulation and validation
Keep related operations together when that makes the design clearer. For example, a `Resource` object could store its total quantity and available quantity and provide a method to borrow items after checking stock.

## Inheritance
A class can inherit from another class, but inheritance should represent a meaningful “is a” relationship. Do not use it simply to avoid writing a few lines of code.

## Practice
1. Create a `Book` class with `title` and `author`.
2. Add a method that returns a formatted description.
3. Create two objects and show that their attributes are separate.
4. Create a `Resource` class with `total` and `available`.
5. Add a `borrow(quantity)` method that rejects invalid or unavailable quantities.
6. Add a `return_items(quantity)` method and test boundary cases.
7. Explain the purpose of `self` and `__init__`.

## Challenge
Refactor a procedural resource tracker into `Resource` and `Inventory` classes. Keep the design small and test methods independently before building a user interface.


## Completion checklist
- [ ] Define a class and instantiate objects
- [ ] Explain self and __init__
- [ ] Create attributes and methods
- [ ] Validate state-changing operations

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
