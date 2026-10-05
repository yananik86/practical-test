# Task 29 — Shared Authentication Library Tests

## Scenario

A shared authentication library is used by both Web and Mobile applications.

The library has been changed.

The goal is to check that the changes do not cause side effects or break existing functionality.

## Test areas

### 1. Login

Check that users can log in successfully with valid credentials.

Expected result:
- User is authenticated.
- Authentication token is created.

### 2. Invalid credentials

Check login with an incorrect password.

Expected result:
- Login is rejected.
- Appropriate error is returned.

### 3. Token validation

Check that a valid authentication token is accepted.

Expected result:
- User remains authenticated.

### 4. Expired token

Check authentication with an expired token.

Expected result:
- Access is denied.
- User must authenticate again.

### 5. Web application

Run the authentication regression tests for Web.

Check:
- Login
- Logout
- Token handling
- Protected pages

### 6. Mobile application

Run the authentication regression tests for Mobile.

Check:
- Login
- Logout
- Token handling
- Protected screens

## Regression testing

A regression suite should be executed after changing the shared authentication library.

The regression suite must verify that existing Web and Mobile authentication functionality still works.

## Possible side effects

The tests should detect:

- Login failures
- Incorrect token handling
- Unexpected logout
- Access to protected resources being denied incorrectly
- Different authentication behavior between Web and Mobile

## Conclusion

Testing both platforms is necessary because they use the same authentication library.

The main goal is to ensure that the library update does not break existing functionality.
