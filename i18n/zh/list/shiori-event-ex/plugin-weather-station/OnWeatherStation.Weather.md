# OnWeatherStation.Weather

**カテゴリ:** 插件「Weather Station」

将当前天气状况相关信息发送给所有正在运行的 ghost。此事件每小时触发一次、每当其他 ghost 启动时触发，或在任一 ghost 使用 `\![raiseplugin]` 请求时触发。

- **Reference0**: 天气状况。可能的状况列表请参见[※下方](note-1.md#天気の状況と状況コードの一覧)。
- **Reference1**: 表示天气状况的图标文件名。与 weatherapi 的[天气图标包](https://cdn.weatherapi.com/weather.zip)配合使用。
- **Reference2**: 天气状况代码。可能的状况代码列表请参见[※下方](note-1.md#天気の状況と状況コードの一覧)。
- **Reference3**: 是否为白天。太阳升起时为1，落下时为0。
- **Reference4**: 气温（华氏）。
- **Reference5**: 气温（摄氏）。
- **Reference6**: 「体感」温度（华氏）。
- **Reference7**: 「体感」温度（摄氏）。
- **Reference8**: 湿度（百分比）。
- **Reference9**: 风速（英里/小时）。
- **Reference10**: 风速（千米/小时）。
- **Reference11**: 风向（16方位。例如：NNE表示北东北）。
- **Reference12**: 风向（度）。
- **Reference13**: 阵风风速（英里/小时）。
- **Reference14**: 阵风风速（千米/小时）。
- **Reference15**: 降水量（英寸）。
- **Reference16**: 降水量（毫米）。
- **Reference17**: 云量（百分比）。
- **Reference18**: 「今天是否会下雨」。下雨时为1，不下雨时为0。与OnWeatherStation.Forecast.Day的「今天是否会下雨」信息相同。
- **Reference19**: 今天的降雨概率（百分比）。与OnWeatherStation.Forecast.Day的降雨概率信息相同。
- **Reference20**: 「今天是否会下雪」。下雪时为1，不下雪时为0。与OnWeatherStation.Forecast.Day的「今天是否会下雪」信息相同。
- **Reference21**: 今天的降雪概率（百分比）。与OnWeatherStation.Forecast.Day的降雪概率信息相同。
- **Reference22**: 能见度（英里）。
- **Reference23**: 能见度（千米）。
- **Reference24**: 气压（英寸）。
- **Reference25**: 气压（毫巴）。
- **Reference26**: UV指数。
- **Reference27**: CO（一氧化碳）。单位为μg/m3（每立方米的微克数）。
- **Reference28**: O3（臭氧）。单位为μg/m3（每立方米的微克数）。
- **Reference29**: NO2（二氧化氮）。单位为μg/m3（每立方米的微克数）。
- **Reference30**: SO2（二氧化硫）。单位为μg/m3（每立方米的微克数）。
- **Reference31**: PM2.5（直径小于2.5微米的颗粒物）。单位为μg/m3（每立方米的微克数）。
- **Reference32**: PM10（直径小于10微米的颗粒物）。单位为μg/m3（每立方米的微克数）。
- **Reference33**: US EPA指数。1为良好，2为中等，3为对敏感人群不健康，4为不健康，5为非常不健康，6为危险。
- **Reference34**: UK Defra指数。详情请参见[※下方](note-1.md#uk-defra指数の早見表)。
- **Reference35**: 用户选择的单位制（Imperial或Metric）。
- **Reference36**: 插件上次更新天气数据的时间。表示为从EPOCH（1970/1/1 00:00:00）起经过的秒数。
- **Reference37**: 插件当前的版本号。
- **Reference38**: &lt;Deprecated\>
- **Reference39**: &lt;Deprecated\>
- **Reference40**: &lt;Deprecated\>
- **Reference41**: &lt;Deprecated\>
