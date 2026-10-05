# Task 27 — Discount at Threshold

## Scenario

A customer receives a discount when the order amount reaches a specific threshold.

Discount rule:

- Order amount less than 10,000 → no discount.
- Order amount equal to or greater than 10,000 → discount is applied.

## Boundary test cases

| Order amount | Expected result |
|---:|---|
| 9,999 | No discount |
| 10,000 | Discount applied |
| 10,001 | Discount applied |

## Additional test cases

| Order amount | Expected result |
|---:|---|
| 0 | No discount |
| 5,000 | No discount |
| 15,000 | Discount applied |

## Testing approach

Boundary Value Analysis is used because the most important cases are values around the discount threshold.

The key values are:

- Just below the threshold
- Exactly at the threshold
- Just above the threshold

This helps detect errors in the discount condition.
