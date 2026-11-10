# OnWeatherStation.Forecast.Hourly

**カテゴリ:** Plugin "Weather Station"

Sends information about the hourly forecast for one day to all running ghosts. It must be invoked with `\![raiseplugin]`. An additional argument can specify which day's data to send: 0 is today, 1 is tomorrow, and 2 is the day after tomorrow. If no argument is given, today's data is sent.

- **Reference0～23**: A comma-separated array containing forecast information. The Reference number corresponds to the hour (in 24-hour format) that the data applies to (for example, reference0 is 00:00/12 AM, and reference14 is 14:00/2 PM).
  - \[0\] - The date and time that the information applies to.
  - \[1\] - "Is it daytime?" 1 if the Sun is up, 0 if it has set.
  - \[2\] - Temperature (Fahrenheit).
  - \[3\] - Temperature (Celsius).
  - \[4\] - "Feels like" temperature (Fahrenheit).
  - \[5\] - "Feels like" temperature (Celsius).
  - \[6\] - Humidity (percent).
  - \[7\] - Wind speed (miles per hour).
  - \[8\] - Wind speed (kilometers per hour).
  - \[9\] - Wind direction (16-point compass; for example, NNW is north-northwest).
  - \[10\] - Wind direction (degrees).
  - \[11\] - Gust speed (miles per hour).
  - \[12\] - Gust speed (kilometers per hour).
  - \[13\] - Precipitation (inches).
  - \[14\] - Precipitation (millimeters).
  - \[15\] - Cloud cover (percent).
  - \[16\] - "Will it rain?" 1 if yes, 0 if no.
  - \[17\] - Probability of rain (percent).
  - \[18\] - "Will it snow?" 1 if yes, 0 if no.
  - \[19\] - Probability of snow (percent).
  - \[20\] - Visibility (miles).
  - \[21\] - Visibility (kilometers).
  - \[22\] - Wind chill (Fahrenheit).
  - \[23\] - Wind chill (Celsius).
  - \[24\] - Heat index (Fahrenheit).
  - \[25\] - Heat index (Celsius).
  - \[26\] - Dew point (Fahrenheit).
  - \[27\] - Dew point (Celsius).
  - \[28\] - Pressure (inches).
  - \[29\] - Pressure (millibars).
  - \[30\] - UV index.
- **Reference24**: The day to which the preceding information applies. 0 is today, 1 is tomorrow, and 2 is the day after tomorrow.
