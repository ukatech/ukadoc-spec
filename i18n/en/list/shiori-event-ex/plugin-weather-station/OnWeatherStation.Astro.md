# OnWeatherStation.Astro

**カテゴリ:** Plugin "Weather Station"

Sends information about the Sun and Moon to all running ghosts. It must be invoked with `\![raiseplugin]`. An additional argument can specify which day's data to send: 0 is today, 1 is tomorrow, and 2 is the day after tomorrow. If no argument is given, today's data is sent.

- **Reference0**: The day that the following information applies to. 0 is today, 1 is tomorrow, and 2 is the day after tomorrow.
- **Reference1**: Sunrise time in 12-hour format, in the form ##:## \*M
- **Reference2**: Sunset time in 12-hour format, in the form ##:## \*M
- **Reference3**: Moonrise time in 12-hour format, in the form ##:## \*M
- **Reference4**: Moonset time in 12-hour format, in the form ##:## \*M
- **Reference5**: Sunrise time in 24-hour format, in the form ##:##
- **Reference6**: Sunset time in 24-hour format, in the form ##:##
- **Reference7**: Moonrise time in 24-hour format, in the form ##:##
- **Reference8**: Moonset time in 24-hour format, in the form ##:##
- **Reference9**: A string representing the lunar phase: one of "New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous", "Last Quarter", or "Waning Crescent".
- **Reference10**: Lunar phase number. The values correspond to the following lunar phases:
  - 0 - New Moon
  - 1 - Waxing Crescent
  - 2 - First Quarter
  - 3 - Waxing Gibbous
  - 4 - Full Moon
  - 5 - Waning Gibbous
  - 6 - Last Quarter
  - 7 - Waning Crescent
- **Reference11**: The illuminated fraction of the Moon, expressed as a percentage.
