# OnWeatherStation.Astro

**カテゴリ:** plugin「Weather Station」

向所有執行中的 ghost 傳送太陽與月亮的資訊。必須透過 `\![raiseplugin]` 呼叫。可用額外的引數指定傳送哪一天的資料。0 表示今天，1 表示明天，2 表示後天。若未指定引數，預設為今天。

- **Reference0**: 以下資訊所對應的日期。0 表示今天，1 表示明天，2 表示後天。
- **Reference1**: 日出時間。採 12 小時制，格式為 ##:## \*M
- **Reference2**: 日落時間。採 12 小時制，格式為 ##:## \*M
- **Reference3**: 月出時間。採 12 小時制，格式為 ##:## \*M
- **Reference4**: 月落時間。採 12 小時制，格式為 ##:## \*M
- **Reference5**: 日出時間。採 24 小時制，格式為 ##:##
- **Reference6**: 日落時間。採 24 小時制，格式為 ##:##
- **Reference7**: 月出時間。採 24 小時制，格式為 ##:##
- **Reference8**: 月落時間。採 24 小時制，格式為 ##:##
- **Reference9**: 表示月相的字串。為 "New Moon"、"Waxing Crescent"、"First Quarter"、"Waxing Gibbous"、"Full Moon"、"Waning Gibbous"、"Last Quarter"、"Waning Crescent" 其中之一。
- **Reference10**: 月相編號。數值對應以下月相。
  - 0 - New Moon
  - 1 - Waxing Crescent
  - 2 - First Quarter
  - 3 - Waxing Gibbous
  - 4 - Full Moon
  - 5 - Waning Gibbous
  - 6 - Last Quarter
  - 7 - Waning Crescent
- **Reference11**: 月球照明比例，以百分比表示。
