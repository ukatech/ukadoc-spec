# OnWeatherStation.Astro

**カテゴリ:** plugin“Weather Station”

向所有正在运行的 ghost 发送有关太阳和月亮的信息。必须通过 `\![raiseplugin]` 调用。可以通过额外参数指定发送哪一天的数据。0 表示今天，1 表示明天，2 表示后天。未指定参数时默认为今天。

- **Reference0**: 以下信息所针对的日期。0 表示今天，1 表示明天，2 表示后天。
- **Reference1**: 日出时间。采用 12 小时制，格式为 ##:## \*M
- **Reference2**: 日落时间。采用 12 小时制，格式为 ##:## \*M
- **Reference3**: 月出时间。采用 12 小时制，格式为 ##:## \*M
- **Reference4**: 月落时间。采用 12 小时制，格式为 ##:## \*M
- **Reference5**: 日出时间。采用 24 小时制，格式为 ##:##
- **Reference6**: 日落时间。采用 24 小时制，格式为 ##:##
- **Reference7**: 月出时间。采用 24 小时制，格式为 ##:##
- **Reference8**: 月落时间。采用 24 小时制，格式为 ##:##
- **Reference9**: 表示月相的字符串。取值为 "New Moon"、"Waxing Crescent"、"First Quarter"、"Waxing Gibbous"、"Full Moon"、"Waning Gibbous"、"Last Quarter"、"Waning Crescent" 中的一个。
- **Reference10**: 月相编号。数值与以下月相对应。
  - 0 - New Moon
  - 1 - Waxing Crescent
  - 2 - First Quarter
  - 3 - Waxing Gibbous
  - 4 - Full Moon
  - 5 - Waning Gibbous
  - 6 - Last Quarter
  - 7 - Waning Crescent
- **Reference11**: 月面照明比例，以百分比表示。
