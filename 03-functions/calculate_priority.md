# Exercise: Calculate Priority

Calculate a support ticket priority.

`calculate_priority(urgency, affected_users)` should return `critical` when urgency is high and affected_users is at least 10. Return `high` when urgency is high OR affected_users is at least 10. Return `medium` when urgency is medium. Otherwise return `low`. Urgency should be case-insensitive.

## How to check
Run the matching test file with pytest. Your tests should pass when the function meets the requirements.
