# OnWeatherStation.Weather

**カテゴリ:** プラグイン「Weather Station」

Sends information about the current weather conditions to all open ghosts. This event occurs every hour, every time another ghost boots, and any time any ghost requests it with `\![raiseplugin]`.

- **Reference0**: Weather condition. [※See below](note-1.md#補足) for a list of possible weather conditions.
- **Reference1**: Weather condition icon filename. To be used with weatherapi's [weather icon pack](https://cdn.weatherapi.com/weather.zip).
- **Reference2**: Weather condition code. [※See below](note-1.md#補足) for a list of possible weather condition codes.
- **Reference3**: If it is daytime or not. 1 if the sun is up, 0 if the sun is down.
- **Reference4**: Temperature in Fahrenheit.
- **Reference5**: Temperature in Celsius.
- **Reference6**: "Feels like" temperature in Fahrenheit.
- **Reference7**: "Feels like" temperature in Celsius.
- **Reference8**: Humidity as a percentage.
- **Reference9**: Wind speed in miles per hour.
- **Reference10**: Wind speed in kilometers per hour.
- **Reference11**: Wind direction as a 16 point compass. (e.g.: NNE for north/northeast.)
- **Reference12**: Wind direction in degrees.
- **Reference13**: Wind gust speed in miles per hour.
- **Reference14**: Wind gust speed in kilometers per hour.
- **Reference15**: Precipitation in inches.
- **Reference16**: Precipitation in millimeters.
- **Reference17**: Cloud cover as a percentage.
- **Reference18**: "Will it rain today". 1 for yes, 0 for no. Same information as the "Will it rain today" in OnWeatherStation.Forecast.Day.
- **Reference19**: Chance of rain today, as a percentage. Same information as the chance of rain in OnWeatherStation.Forecast.Day.
- **Reference20**: "Will it snow today". 1 for yes, 0 for no. Same information as the "Will it snow today" in OnWeatherStation.Forecast.Day.
- **Reference21**: Chance of snow today, as a percentage. Same information as the chance of snow in OnWeatherStation.Forecast.Day.
- **Reference22**: Visibility in miles.
- **Reference23**: Visibility in kilometers.
- **Reference24**: Pressure in inches.
- **Reference25**: Pressure in millibars.
- **Reference26**: UV index.
- **Reference27**: CO (Carbon Monoxide) in μg/m3 (Micrograms per cubic meter).
- **Reference28**: O3 (Ozone) in μg/m3 (Micrograms per cubic meter).
- **Reference29**: NO2 (Nitrogen Dioxide) in μg/m3 (Micrograms per cubic meter).
- **Reference30**: SO2 (Sulfur Dioxide) in μg/m3 (Micrograms per cubic meter).
- **Reference31**: PM2.5 (Particulate Matter smaller than 2.5 microns in diameter) in μg/m3 (Micrograms per cubic meter).
- **Reference32**: PM10 (Particulate Matter smaller than 10 microns in diameter) in μg/m3 (Micrograms per cubic meter).
- **Reference33**: US EPA index. 1 means Good, 2 means Moderate, 3 means Unhealthy for sensitive group, 4 means Unhealthy, 5 means Very unhealthy, 6 means Hazardous.
- **Reference34**: UK Defra Index. [※See details](note-1.md#weather-condition--code-list) below.
- **Reference35**: The user's choice of units (Imperial or Metric).
- **Reference36**: The time the plugin last updated the weather data, in seconds since EPOCH (1970/1/1 00:00:00).
- **Reference37**: The current version number of the plugin.
- **Reference38**: &lt;Deprecated\>
- **Reference39**: &lt;Deprecated\>
- **Reference40**: &lt;Deprecated\>
- **Reference41**: &lt;Deprecated\>
