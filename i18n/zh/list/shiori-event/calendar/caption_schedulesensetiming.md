# Schedule sensor update timing and events

- **Manual update**: When you select a sensor from the calendar menu and update it. All of Begin→Complete (or Failure) occur.
- **Periodic check**: When SSP automatically checks all sensors every 30 minutes. Only [OnSchedulesenseFailure](OnSchedulesenseFailure.md) occurs.<br />
  If Begin/Complete for every sensor were sent periodically, ghosts would talk too much, so only errors are reported.
