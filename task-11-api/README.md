# Task 11 — Tasks API

## Description

REST API for managing a list of tasks.

## Requirements

The API should support:

- Creating a task
- Viewing tasks
- Updating task status
- Deleting a task
- Pagination
- Error handling

## Endpoints

POST /tasks — create a task

GET /tasks — get the list of tasks

PATCH /tasks/{id} — update task status

DELETE /tasks/{id} — delete a task

## Pagination

GET /tasks?page=1&limit=10

## Error codes

400 — Bad Request

404 — Not Found

409 — Conflict

500 — Internal Server Error
