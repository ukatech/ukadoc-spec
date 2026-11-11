# OnWeatherStation.Astro

**カテゴリ:** plugin「Weather Station」

將太陽與月亮的相關資訊傳送給所有執行中的 ghost。必須使用`\![raiseplugin]`呼叫。可透過額外引數指定要傳送哪一天的資料。0為今天，1為明天，2為後天。未提供引數時預設為今天。

- **Reference0**: 以下資訊所對應的日期。0為今天，1為明天，2為後天。
- **Reference1**: 日出時間。採12小時制，格式為##:## \*M
- **Reference2**: 日落時間。採12小時制，格式為##:## \*M
- **Reference3**: 月出時間。採12小時制，格式為##:## \*M
- **Reference4**: 月落時間。採12小時制，格式為##:## \*M
- **Reference5**: 日出時間。採24小時制，格式為##:##
- **Reference6**: 日落時間。採24小時制，格式為##:##
- **Reference7**: 月出時間。採24小時制，格式為##:##
- **Reference8**: 月落時間。採24小時制，格式為##:##
- **Reference9**: 表示月相的字串。為"New Moon"、"Waxing Crescent"、"First Quarter"、"Waxing Gibbous"、"Full Moon"、"Waning Gibbous"、"Last Quarter"、"Waning Crescent"其中之一。
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
