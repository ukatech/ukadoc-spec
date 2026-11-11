# OnWeatherStation.Weather

**カテゴリ:** plugin“Weather Station”

向所有运行中的 ghost 发送当前天气状况的信息。此事件每小时发生一次，也会在其他 ghost 启动时以及任意 ghost 通过 `\![raiseplugin]` 请求时发生。

- **Reference0**: 天气状况。可能的状况列表参见[※下文](note-1.md#天気の状況と状況コードの一覧)。
- **Reference1**: 天气状况图标的文件名。与 weatherapi 的[天气图标包](https://cdn.weatherapi.com/weather.zip)配合使用。
- **Reference2**: 天气状况代码。可能的状况代码列表参见[※下文](note-1.md#天気の状況と状況コードの一覧)。
- **Reference3**: 是否为白天。太阳升起时为 1，落下时为 0。
- **Reference4**: 气温（华氏度）。
- **Reference5**: 气温（摄氏度）。
- **Reference6**: “体感”温度（华氏度）。
- **Reference7**: “体感”温度（摄氏度）。
- **Reference8**: 湿度（百分比）。
- **Reference9**: 风速（英里每小时）。
- **Reference10**: 风速（千米每小时）。
- **Reference11**: 风向（16 方位。例：NNE 表示北东北）。
- **Reference12**: 风向（度）。
- **Reference13**: 阵风风速（英里每小时）。
- **Reference14**: 阵风风速（千米每小时）。
- **Reference15**: 降水量（英寸）。
- **Reference16**: 降水量（毫米）。
- **Reference17**: 云量（百分比）。
- **Reference18**: “今天是否会下雨”。会则为 1，不会则为 0。与 OnWeatherStation.Forecast.Day 中的“今天是否会下雨”信息相同。
- **Reference19**: 今天下雨的概率（百分比）。与 OnWeatherStation.Forecast.Day 中的下雨概率信息相同。
- **Reference20**: “今天是否会下雪”。会则为 1，不会则为 0。与 OnWeatherStation.Forecast.Day 中的“今天是否会下雪”信息相同。
- **Reference21**: 今天下雪的概率（百分比）。与 OnWeatherStation.Forecast.Day 中的下雪概率信息相同。
- **Reference22**: 能见度（英里）。
- **Reference23**: 能见度（千米）。
- **Reference24**: 气压（英寸）。
- **Reference25**: 气压（毫巴）。
- **Reference26**: UV 指数。
- **Reference27**: CO（一氧化碳）。单位为 μg/m3（每立方米微克）。
- **Reference28**: O3（臭氧）。单位为 μg/m3（每立方米微克）。
- **Reference29**: NO2（二氧化氮）。单位为 μg/m3（每立方米微克）。
- **Reference30**: SO2（二氧化硫）。单位为 μg/m3（每立方米微克）。
- **Reference31**: PM2.5（直径小于 2.5 微米的颗粒物）。单位为 μg/m3（每立方米微克）。
- **Reference32**: PM10（直径小于 10 微米的颗粒物）。单位为 μg/m3（每立方米微克）。
- **Reference33**: US EPA 指数。1 表示良好，2 表示中等，3 表示对敏感人群不健康，4 表示不健康，5 表示非常不健康，6 表示危险。
- **Reference34**: UK Defra 指数。详情参见[※下文](note-1.md#uk-defra指数の早見表)。
- **Reference35**: 用户选择的单位制（Imperial 或 Metric）。
- **Reference36**: plugin 上次更新天气数据的时间。以自 EPOCH（1970/1/1 00:00:00）起经过的秒数表示。
- **Reference37**: plugin 的当前版本号。
- **Reference38**: &lt;已弃用\>
- **Reference39**: &lt;已弃用\>
- **Reference40**: &lt;已弃用\>
- **Reference41**: &lt;已弃用\>
