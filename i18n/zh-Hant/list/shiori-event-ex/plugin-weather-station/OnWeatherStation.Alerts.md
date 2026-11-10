# OnWeatherStation.Alerts

**カテゴリ:** Plugin "Weather Station"

Sends weather alert information to all running ghosts. Must be invoked with `\![raiseplugin]`. Returns nothing if there are no alerts.

- **Reference\***: An array containing information for one weather alert. Some elements may be empty. Elements are separated by byte value 1.

  - \[0\] - Headline
  - \[1\] - Alert type
  - \[2\] - Severity
  - \[3\] - Urgency
  - \[4\] - Affected area
  - \[5\] - Category
  - \[6\] - Certainty
  - \[7\] - Event
  - \[8\] - Note
  - \[9\] - Effective time
  - \[10\] - Expiration time
  - \[11\] - Description
  - \[12\] - Instructions
