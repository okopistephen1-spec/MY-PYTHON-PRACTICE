# Exercise: Summarize Inventory

Summarize an inventory.

Implement `summarize_inventory(resources)` returning a dictionary with `total_units`, `available_units`, and `borrowed_units`. Each resource has integer `total` and `available` fields. borrowed_units is total minus available, summed across all resources.

## How to check
Run the matching test file with pytest. Your tests should pass when the function meets the requirements.
