# OnWeatherStation.Alerts

**カテゴリ:** プラグイン「Weather Station」

Sends information about weather alerts to all open ghosts. Must be called with `\![raiseplugin]`. Will return nothing if there are no alerts.

- **Reference\***: An array containing information for a weather alert. Some elements may not be filled. Elements are separated by a 1 byte value.

  - \[0\] - Headline
  - \[1\] - Type of alert
  - \[2\] - Severity
  - \[3\] - Urgency
  - \[4\] - Areas covered
  - \[5\] - Category
  - \[6\] - Certainty
  - \[7\] - Event
  - \[8\] - Note
  - \[9\] - Effective time
  - \[10\] - Expires time
  - \[11\] - Description
  - \[12\] - Instructions
