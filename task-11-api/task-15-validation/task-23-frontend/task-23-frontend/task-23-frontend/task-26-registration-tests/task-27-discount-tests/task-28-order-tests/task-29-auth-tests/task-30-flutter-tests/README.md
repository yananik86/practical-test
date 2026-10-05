# Task 30 — Flutter Screen Testing

## Screen states

The Flutter screen should support the following states:

- Loading
- Error
- Empty
- List with data

## 1. Loading state

When the screen is opened and data is being loaded:

Expected result:
- Loading indicator is displayed.
- User cannot see outdated data.

## 2. Error state

If the API request fails:

Expected result:
- Error message is displayed.
- Retry button is available.

## 3. Empty state

If the API returns an empty list:

Expected result:
- Empty state message is displayed.
- The screen does not show an empty or broken list.

## 4. List state

If the API returns tasks:

Expected result:
- Tasks are displayed correctly.
- User can interact with the list.

## Screen rotation

Test the screen after changing device orientation.

Expected result:
- The screen does not lose its state unexpectedly.
- Data remains available or is restored correctly.
- No UI errors occur.

## Returning to the page

Open the task list, navigate to another screen and return.

Expected result:
- The screen works correctly.
- Data is not displayed incorrectly.
- The application does not crash.

## Automated testing

The following cases should be automated:

- Loading state
- Error state
- Empty state
- Successful list loading
- Retry action
- Navigation

## Manual testing

The following cases can be checked manually:

- Screen rotation
- Visual layout
- Returning to the screen
- Different screen sizes

## Test strategy

Automation is used for repeatable functional scenarios.

Manual testing is used for visual and device-specific behavior.

The combination of automated and manual testing provides better coverage.
