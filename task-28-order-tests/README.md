# Task 28 — Order API Tests

## Order creation flow

When a customer creates an order, the system should:

1. Receive the order request.
2. Check product availability.
3. Create the order in the database.
4. Return the order number.

## Success scenario

### Request

```json
{
  "productId": 101,
  "quantity": 2
}
