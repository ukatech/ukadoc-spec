# OnWeatherStation.Weather

**カテゴリ:** Plugin "Weather Station"

Sends information about current weather conditions to all running ghosts. This event occurs every hour, whenever another ghost starts, and when any ghost requests it with `\![raiseplugin]`.

- **Reference0**: Weather condition. See [※below](note-1.md#天気の状況と状況コードの一覧) for a list of possible conditions.
- **Reference1**: File name of the icon representing the weather condition. Use it with the weatherapi [weather icon pack](https://cdn.weatherapi.com/weather.zip).
- **Reference2**: Weather condition code. See [※below](note-1.md#天気の状況と状況コードの一覧) for a list of possible condition codes.
- **Reference3**: Whether it is daytime. 1 if the sun is up, 0 if it has set.
- **Reference4**: Temperature (Fahrenheit).
- **Reference5**: Temperature (Celsius).
- **Reference6**: "Feels like" temperature (Fahrenheit).
- **Reference7**: "Feels like" temperature (Celsius).
- **Reference8**: Humidity (percent).
- **Reference9**: Wind speed (miles per hour).
- **Reference10**: Wind speed (kilometers per hour).
- **Reference11**: Wind direction (16-point compass; for example, NNE means north-northeast).
- **Reference12**: Wind direction (degrees).
- **Reference13**: Gust speed (miles per hour).
- **Reference14**: Gust speed (kilometers per hour).
- **Reference15**: Precipitation (inches).
- **Reference16**: Precipitation (millimeters).
- **Reference17**: Cloud cover (percent).
- **Reference18**: "Will it rain today?" 1 if it will, 0 if it will not. This is the same information as "Will it rain today?" in OnWeatherStation.Forecast.Day.
- **Reference19**: Probability of rain today (percent). This is the same information as the probability of rain in OnWeatherStation.Forecast.Day.
- **Reference20**: "Will it snow today?" 1 if it will, 0 if it will not. This is the same information as "Will it snow today?" in OnWeatherStation.Forecast.Day.
- **Reference21**: Probability of snow today (percent). This is the same information as the probability of snow in OnWeatherStation.Forecast.Day.
- **Reference22**: Visibility (miles).
- **Reference23**: Visibility (kilometers).
- **Reference24**: Pressure (inches).
- **Reference25**: Pressure (millibars).
- **Reference26**: UV index.
- **Reference27**: CO (carbon monoxide). Unit: μg/m3 (micrograms per cubic meter).
- **Reference28**: O3 (ozone). Unit: μg/m3 (micrograms per cubic meter).
- **Reference29**: NO2 (nitrogen dioxide). Unit: μg/m3 (micrograms per cubic meter).
- **Reference30**: SO2 (sulfur dioxide). Unit: μg/m3 (micrograms per cubic meter).
- **Reference31**: PM2.5 (particulate matter smaller than 2.5 microns in diameter). Unit: μg/m3 (micrograms per cubic meter).
- **Reference32**: PM10 (particulate matter smaller than 10 microns in diameter). Unit: μg/m3 (micrograms per cubic meter).
- **Reference33**: US EPA index. 1 is good, 2 is moderate, 3 is unhealthy for sensitive groups, 4 is unhealthy, 5 is very unhealthy, and 6 is hazardous.
- **Reference34**: UK Defra index. See [※below](note-1.md#uk-defra指数の早見表) for details.
- **Reference35**: Unit system selected by the user (Imperial or Metric).
- **Reference36**: Time when the plugin last updated weather data. Number of seconds since EPOCH (1970/1/1 00:00:00).
- **Reference37**: Current version number of the plugin.
- **Reference38**: &lt;Deprecated\>
- **Reference39**: &lt;Deprecated\>
- **Reference40**: &lt;Deprecated\>
- **Reference41**: &lt;Deprecated\>
