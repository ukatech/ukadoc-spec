# OnWeatherStation.Weather

**カテゴリ:** plugin「Weather Station」

將目前天氣狀況的資訊傳送給所有執行中的 ghost。此事件每小時發生一次，也會在其他 ghost 啟動時，以及任何 ghost 使用 `\![raiseplugin]` 要求時發生。

- **Reference0**: 天氣狀況。可能的狀況清單請參閱[※下方](note-1.md#天気の状況と状況コードの一覧)。
- **Reference1**: 天氣狀況圖示的檔案名稱。與 weatherapi 的[天氣圖示套件](https://cdn.weatherapi.com/weather.zip)搭配使用。
- **Reference2**: 天氣狀況代碼。可能的狀況代碼清單請參閱[※下方](note-1.md#天気の状況と状況コードの一覧)。
- **Reference3**: 是否為白天。太陽已升起為 1，已落下為 0。
- **Reference4**: 氣溫（華氏）。
- **Reference5**: 氣溫（攝氏）。
- **Reference6**: 「體感」溫度（華氏）。
- **Reference7**: 「體感」溫度（攝氏）。
- **Reference8**: 濕度（百分比）。
- **Reference9**: 風速（英里每小時）。
- **Reference10**: 風速（公里每小時）。
- **Reference11**: 風向（16 方位；例如 NNE 表示北北東）。
- **Reference12**: 風向（度）。
- **Reference13**: 陣風風速（英里每小時）。
- **Reference14**: 陣風風速（公里每小時）。
- **Reference15**: 降水量（英吋）。
- **Reference16**: 降水量（毫米）。
- **Reference17**: 雲量（百分比）。
- **Reference18**: 「今天是否下雨」。會下雨為 1，不會下雨為 0。與 OnWeatherStation.Forecast.Day 的「今天是否下雨」資訊相同。
- **Reference19**: 今日降雨機率（百分比）。與 OnWeatherStation.Forecast.Day 的降雨機率資訊相同。
- **Reference20**: 「今天是否下雪」。會下雪為 1，不會下雪為 0。與 OnWeatherStation.Forecast.Day 的「今天是否下雪」資訊相同。
- **Reference21**: 今日降雪機率（百分比）。與 OnWeatherStation.Forecast.Day 的降雪機率資訊相同。
- **Reference22**: 能見度（英里）。
- **Reference23**: 能見度（公里）。
- **Reference24**: 氣壓（英吋）。
- **Reference25**: 氣壓（毫巴）。
- **Reference26**: UV 指數。
- **Reference27**: CO（一氧化碳）。單位為 μg/m3（每立方公尺微克數）。
- **Reference28**: O3（臭氧）。單位為 μg/m3（每立方公尺微克數）。
- **Reference29**: NO2（二氧化氮）。單位為 μg/m3（每立方公尺微克數）。
- **Reference30**: SO2（二氧化硫）。單位為 μg/m3（每立方公尺微克數）。
- **Reference31**: PM2.5（直徑小於 2.5 微米的懸浮微粒）。單位為 μg/m3（每立方公尺微克數）。
- **Reference32**: PM10（直徑小於 10 微米的懸浮微粒）。單位為 μg/m3（每立方公尺微克數）。
- **Reference33**: US EPA 指數。1 表示良好，2 表示普通，3 表示對敏感族群不健康，4 表示不健康，5 表示非常不健康，6 表示危險。
- **Reference34**: UK Defra 指數。詳情請參閱[※下方](note-1.md#uk-defra指数の早見表)。
- **Reference35**: 使用者選擇的單位系統（Imperial 或 Metric）。
- **Reference36**: plugin 最後更新天氣資料的時間，以 EPOCH（1970/1/1 00:00:00）起算的秒數表示。
- **Reference37**: plugin 目前的版本號碼。
- **Reference38**: &lt;Deprecated\>
- **Reference39**: &lt;Deprecated\>
- **Reference40**: &lt;Deprecated\>
- **Reference41**: &lt;Deprecated\>
