# OnWeatherStation.Forecast.Hourly

**カテゴリ:** プラグイン「Weather Station」

Sends information about the hour-by-hour forecast for a day to all open ghosts. Must be called with `\![raiseplugin]`. An additional argument can be sent to specify which day's data should be sent. 0 for today, 1 for tomorrow, 2 for the day after tomorrow. If no argument is given, it will default to today.

- **Reference0～23**: A comma separated array containing forecast information. The number of the reference corresponds to the number of the hour the data is for, in 24 hour time (e.g.: reference0 is for 00:00/12AM, reference14 is for 14:00/2PM).

  - \[0\] - Date and time the information is for.
  - \[1\] - "Is it daytime". 1 if the sun is up, 0 if the sun is down.
  - \[2\] - Temperature in Fahrenheit.
  - \[3\] - Temperature in Celsius.
  - \[4\] - "Feels like" temperature in Fahrenheit.
  - \[5\] - "Feels like" temperature in Celsius.
  - \[6\] - Humidity as a percentage.
  - \[7\] - Wind speed in miles per hour.
  - \[8\] - Wind speed in kilometers per hour.
  - \[9\] - Wind direction as a 16 point compass (e.g.: NNW for north/northwest).
  - \[10\] - Wind direction in degrees.
  - \[11\] - Wind gusts in miles per hour.
  - \[12\] - Wind gusts in kilometers per hour.
  - \[13\] - Precipitation in inches.
  - \[14\] - Precipitation in millimeters.
  - \[15\] - Cloud cover as a percentage.
  - \[16\] - "Will it rain", 1 if yes, 0 if no.
  - \[17\] - Chance of rain as a percentage.
  - \[18\] - "Will it snow", 1 if yes, 0 if no.
  - \[19\] - Chance of snow as a percentage.
  - \[20\] - Visibility in miles.
  - \[21\] - Visibility in kilometers.
  - \[22\] - Wind chill in Fahrenheit.
  - \[23\] - Wind chill in Celsius.
  - \[24\] - Heat index in Fahrenheit.
  - \[25\] - Heat index in Celsius.
  - \[26\] - Dew point in Fahrenheit.
  - \[27\] - Dew point in Celsius.
  - \[28\] - Pressure in inches.
  - \[29\] - Pressure in millibars.
  - \[30\] - UV index.

- **Reference24**: The day the preceding information is for. 0 for today, 1 for tomorrow, 2 for the day after tomorrow.
