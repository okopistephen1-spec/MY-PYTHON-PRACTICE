# Exercise: Borrow Resource

Borrow resources safely.

Implement `borrow_resource(resource, quantity)`. `resource` is a dictionary with `total` and `available` counts. If quantity is not positive, return False. If quantity exceeds available, return False. Otherwise subtract quantity from `available` and return True. Do not allow available to become negative.

## How to check
Run the matching test file with pytest. Your tests should pass when the function meets the requirements.
