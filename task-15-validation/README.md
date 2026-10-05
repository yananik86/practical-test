# Task 15 — Form Validation

## Description

The form accepts email and date of birth.

## Frontend validation

The frontend checks:

- Email is required.
- Email must contain a valid format.
- Date of birth is required.
- Date of birth cannot be in the future.

## Backend validation

The server validates the data again because frontend validation can be bypassed.

## Error messages

Examples:

- "Введите email"
- "Введите корректный email"
- "Введите дату рождения"
- "Дата рождения не может быть в будущем"

## API

POST /register

Example request:

{
  "email": "test@example.com",
  "birthDate": "2006-12-27"
}

Successful response:

{
  "message": "Регистрация прошла успешно",
  "email": "test@example.com",
  "birthDate": "2006-12-27"
}
