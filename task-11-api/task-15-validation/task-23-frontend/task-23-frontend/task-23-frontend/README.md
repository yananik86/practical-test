# Task 23 — Frontend List States

## Implemented states

The frontend supports the following states:

- Loading
- Empty list
- Error
- Partial data
- Retry

## Loading

While data is loading, the user sees the "Загрузка..." message.

## Empty state

If there are no tasks, the user sees "Список пуст".

## Error state

If the server returns an error, the user can retry the request.

## Retry

The Retry button allows the user to repeat the request.

## Preventing stale data

Each request receives a unique request ID.

If an older request finishes after a newer request, its result is ignored.

This prevents stale data from replacing the latest filtered data.
