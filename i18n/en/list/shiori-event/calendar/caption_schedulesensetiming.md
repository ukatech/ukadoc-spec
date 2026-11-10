# Schedule Sensor Update Timing and Events

- **Manual update**: Updating a sensor selected from the calendar menu. Begin and then Complete (or Failure) occur for all sensors.
- **Periodic check**: SSP automatically cycles through all sensors every 30 minutes. Only [OnSchedulesenseFailure](OnSchedulesenseFailure.md) occurs.<br />
  If Begin/Complete events for all sensors were sent periodically, ghosts would talk too much, so only errors are reported.
