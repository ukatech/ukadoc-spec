# Schedule sensor update timing and events

- **Manual update**: When a sensor is selected from the calendar menu to update. Both Begin and Complete (or Failure) occur.
- **Periodic check**: When SSP automatically checks all sensors every 30 minutes. Only [OnSchedulesenseFailure](OnSchedulesenseFailure.md) occurs.<br />
  If Begin/Complete for all sensors were sent periodically, ghosts would speak too much, so only errors are reported.
