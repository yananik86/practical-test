# Task 26 — Registration Form Tests

## Test cases

### 1. Required fields

Input:
- Name: empty
- Email: empty
- Password: empty

Expected result:
- Validation error is displayed.
- Registration is not completed.

### 2. Invalid email

Input:
- Name: Test User
- Email: test@
- Password: Password123

Expected result:
- Error message about invalid email.
- Registration is not completed.

### 3. Occupied email

Input:
- Name: Test User
- Email: existing@example.com
- Password: Password123

Expected result:
- Error message: "Email is already registered."
- Registration is not completed.

### 4. Successful registration

Input:
- Name: Test User
- Email: new@example.com
- Password: Password123

Expected result:
- Registration is successful.
- User account is created.

## Test types

- Unit testing — validation of individual fields.
- Integration testing — interaction between form and backend.
- UI testing — checking the registration form from the user's perspective.
