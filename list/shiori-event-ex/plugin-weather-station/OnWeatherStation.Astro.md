# OnWeatherStation.Astro

**カテゴリ:** プラグイン「Weather Station」

Sends information about the sun and moon to all open ghosts. Must be called with `\![raiseplugin]`. An additional argument can be sent to specify which day's data should be sent. 0 for today, 1 for tomorrow, 2 for the day after tomorrow. If no argument is given, it will default to today.

- **Reference0**: The day the following information is for. 0 for today, 1 for tomorrow, 2 for the day after tomorrow.

- **Reference1**: Sunrise time, given as 12 hour time with the format ##:## \*M

- **Reference2**: Sunset time, given as 12 hour time with the format ##:## \*M

- **Reference3**: Moonrise time, given as 12 hour time with the format ##:## \*M

- **Reference4**: Moonset time, given as 12 hour time with the format ##:## \*M

- **Reference5**: Sunrise time, given as 24 hour time with the format ##:##

- **Reference6**: Sunset time, given as 24 hour time with the format ##:##

- **Reference7**: Moonrise time, given as 24 hour time with the format ##:##

- **Reference8**: Moonset time, given as 24 hour time with the format ##:##

- **Reference9**: Moon phase as a string. Can be "New Moon", "Waxing Crescent". "First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous", "Last Quarter", or "Waning Crescent".

- **Reference10**: Moon phase number. Numbers correspond to the following phases.

  - 0 - New Moon
  - 1 - Waxing Crescent
  - 2 - First Quarter
  - 3 - Waxing Gibbous
  - 4 - Full Moon
  - 5 - Waning Gibbous
  - 6 - Last Quarter
  - 7 - Waning Crescent

- **Reference11**: Moon illumination as a percentage.
