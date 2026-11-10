# OnWeatherStation.Forecast.Day

**カテゴリ:** 外掛程式「Weather Station」

將一整天預報的相關資訊傳送給所有正在執行的 ghost。必須使用 `\![raiseplugin]` 呼叫。可透過額外引數指定要傳送哪一天的資料。0 代表今天，1 代表明天，2 代表後天。未指定引數時，預設為今天。

- **Reference0**: 以下資訊所對應的日期。0 代表今天，1 代表明天，2 代表後天。
- **Reference1**: 當日最高氣溫（華氏）。
- **Reference2**: 當日最高氣溫（攝氏）。
- **Reference3**: 當日最低氣溫（華氏）。
- **Reference4**: 當日最低氣溫（攝氏）。
- **Reference5**: 當日平均氣溫（華氏）。
- **Reference6**: 當日平均氣溫（攝氏）。
- **Reference7**: 當日平均濕度（百分比）。
- **Reference8**: 當日最大風速（mph）。
- **Reference9**: 當日最大風速（kph）。
- **Reference10**: 當日總降水量（英吋）。
- **Reference11**: 當日總降水量（毫米）。
- **Reference12**:「當天是否會下雨」。會下雨時為 1，不會下雨時為 0。
- **Reference13**: 當天下雨的機率（百分比）。
- **Reference14**:「當天是否會下雪」。會下雪時為 1，不會下雪時為 0。
- **Reference15**: 當天下雪的機率（百分比）。
- **Reference16**: 當日平均能見度（英里）。
- **Reference17**: 當日平均能見度（公里）。
