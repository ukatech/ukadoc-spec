# OnWeatherStation.Weather

**カテゴリ:** 外掛程式「Weather Station」

將目前氣象狀況的資訊傳送給所有正在執行的鬼。此事件每小時發生一次、每當其他鬼啟動時發生，或在任一鬼透過`\![raiseplugin]`要求時發生。

- **Reference0**: 天氣狀況。可能的狀況一覽請參閱[※下方](note-1.md#天気の状況と状況コードの一覧)。
- **Reference1**: 表示天氣狀況的圖示檔名。與 weatherapi 的[天氣圖示套件](https://cdn.weatherapi.com/weather.zip)搭配使用。
- **Reference2**: 天氣狀況代碼。可能的狀況代碼一覽請參閱[※下方](note-1.md#天気の状況と状況コードの一覧)。
- **Reference3**: 是否為白天。太陽升起時為1，落下時為0。
- **Reference4**: 氣溫（華氏）。
- **Reference5**: 氣溫（攝氏）。
- **Reference6**: 「體感」溫度（華氏）。
- **Reference7**: 「體感」溫度（攝氏）。
- **Reference8**: 濕度（百分比）。
- **Reference9**: 風速（英里／小時）。
- **Reference10**: 風速（公里／小時）。
- **Reference11**: 風向（16方位。例如：NNE為北北東）。
- **Reference12**: 風向（度）。
- **Reference13**: 陣風風速（英里／小時）。
- **Reference14**: 陣風風速（公里／小時）。
- **Reference15**: 降水量（英吋）。
- **Reference16**: 降水量（毫米）。
- **Reference17**: 雲量（百分比）。
- **Reference18**: 「今天是否會下雨」。會下雨時為1，不會下雨時為0。與OnWeatherStation.Forecast.Day的「今天是否會下雨」資訊相同。
- **Reference19**: 今天下雨的機率（百分比）。與OnWeatherStation.Forecast.Day的下雨機率資訊相同。
- **Reference20**: 「今天是否會下雪」。會下雪時為1，不會下雪時為0。與OnWeatherStation.Forecast.Day的「今天是否會下雪」資訊相同。
- **Reference21**: 今天下雪的機率（百分比）。與OnWeatherStation.Forecast.Day的下雪機率資訊相同。
- **Reference22**: 能見度（英里）。
- **Reference23**: 能見度（公里）。
- **Reference24**: 氣壓（英吋）。
- **Reference25**: 氣壓（毫巴）。
- **Reference26**: UV指數。
- **Reference27**: CO（一氧化碳）。單位為μg/m3（每立方公尺的微克數）。
- **Reference28**: O3（臭氧）。單位為μg/m3（每立方公尺的微克數）。
- **Reference29**: NO2（二氧化氮）。單位為μg/m3（每立方公尺的微克數）。
- **Reference30**: SO2（二氧化硫）。單位為μg/m3（每立方公尺的微克數）。
- **Reference31**: PM2.5（直徑小於2.5微米的懸浮微粒）。單位為μg/m3（每立方公尺的微克數）。
- **Reference32**: PM10（直徑小於10微米的懸浮微粒）。單位為μg/m3（每立方公尺的微克數）。
- **Reference33**: 美國EPA指數。1為良好、2為普通、3為對敏感族群不健康、4為不健康、5為非常不健康、6為危險。
- **Reference34**: 英國Defra指數。詳細資訊請參閱[※下方](note-1.md#uk-defra指数の早見表)。
- **Reference35**: 使用者選擇的單位系統（Imperial或Metric）。
- **Reference36**: 外掛程式上次更新天氣資料的時間。自EPOCH（1970/1/1 00:00:00）起算的秒數。
- **Reference37**: 外掛程式目前的版本號。
- **Reference38**: &lt;Deprecated\>
- **Reference39**: &lt;Deprecated\>
- **Reference40**: &lt;Deprecated\>
- **Reference41**: &lt;Deprecated\>
