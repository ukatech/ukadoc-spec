# OnWeatherStation.Forecast.Day

**カテゴリ:** Plugin "Weather Station"

Sends information about the full-day forecast to all running ghosts. It must be invoked with `\![raiseplugin]`. An additional argument can specify which day's data to send: 0 is today, 1 is tomorrow, and 2 is the day after tomorrow. If no argument is given, today's data is sent.

- **Reference0**: The day that the following information applies to. 0 is today, 1 is tomorrow, and 2 is the day after tomorrow.
- **Reference1**: The day's maximum temperature (Fahrenheit).
- **Reference2**: The day's maximum temperature (Celsius).
- **Reference3**: The day's minimum temperature (Fahrenheit).
- **Reference4**: The day's minimum temperature (Celsius).
- **Reference5**: The day's average temperature (Fahrenheit).
- **Reference6**: The day's average temperature (Celsius).
- **Reference7**: The day's average humidity (percent).
- **Reference8**: The day's maximum wind speed (mph).
- **Reference9**: The day's maximum wind speed (kph).
- **Reference10**: The day's total precipitation (inches).
- **Reference11**: The day's total precipitation (millimeters).
- **Reference12**: "Will it rain on this day?" 1 if yes, 0 if no.
- **Reference13**: Probability of rain on this day (percent).
- **Reference14**: "Will it snow on this day?" 1 if yes, 0 if no.
- **Reference15**: Probability of snow on this day (percent).
- **Reference16**: The day's average visibility (miles).
- **Reference17**: The day's average visibility (kilometers).
