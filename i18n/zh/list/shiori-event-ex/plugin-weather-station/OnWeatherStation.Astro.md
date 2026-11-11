# OnWeatherStation.Astro

**カテゴリ:** plugin“Weather Station”

向所有运行中的ghost发送有关太阳和月亮的信息。必须使用`\![raiseplugin]`调用。可以通过额外参数指定发送哪一天的数据。0表示今天，1表示明天，2表示后天。未指定参数时默认为今天。

- **Reference0**: 以下信息所对应的日期。0表示今天，1表示明天，2表示后天。
- **Reference1**: 日出时间。采用12小时制，格式为##:## \*M
- **Reference2**: 日落时间。采用12小时制，格式为##:## \*M
- **Reference3**: 月出时间。采用12小时制，格式为##:## \*M
- **Reference4**: 月落时间。采用12小时制，格式为##:## \*M
- **Reference5**: 日出时间。采用24小时制，格式为##:##
- **Reference6**: 日落时间。采用24小时制，格式为##:##
- **Reference7**: 月出时间。采用24小时制，格式为##:##
- **Reference8**: 月落时间。采用24小时制，格式为##:##
- **Reference9**: 表示月相的字符串。取"New Moon"、"Waxing Crescent"、"First Quarter"、"Waxing Gibbous"、"Full Moon"、"Waning Gibbous"、"Last Quarter"或"Waning Crescent"。
- **Reference10**: 月相编号。数值对应以下月相。
  - 0 - New Moon
  - 1 - Waxing Crescent
  - 2 - First Quarter
  - 3 - Waxing Gibbous
  - 4 - Full Moon
  - 5 - Waning Gibbous
  - 6 - Last Quarter
  - 7 - Waning Crescent
- **Reference11**: 月面照明比例，以百分比表示。
