# 补充说明

## 天气状况及状况代码列表

可以从 [weatherapi 的文档页面](https://www.weatherapi.com/docs/)下载状况列表。该列表也提供其他语言版本，但 plugin 发送的信息始终为英语。

- **1000**: Sunny（日落后改为 "Clear"）
- **1003**: Partly cloudy
- **1006**: Cloudy
- **1009**: Overcast
- **1030**: Mist
- **1063**: Patchy rain possible
- **1066**: Patchy snow possible
- **1069**: Patchy sleet possible
- **1072**: Patchy freezing drizzle possible
- **1087**: Thundery outbreaks possible
- **1114**: Blowing snow
- **1117**: Blizzard
- **1135**: Fog
- **1147**: Freezing fog
- **1150**: Patchy light drizzle
- **1153**: Light drizzle
- **1168**: Freezing drizzle
- **1171**: Heavy freezing drizzle
- **1180**: Patchy light rain
- **1183**: Light rain
- **1186**: Moderate rain at times
- **1189**: Moderate rain
- **1192**: Heavy rain at times
- **1195**: Heavy rain
- **1198**: Light freezing rain
- **1201**: Moderate or heavy freezing rain
- **1204**: Light sleet
- **1207**: Moderate or heavy sleet
- **1210**: Patchy light snow
- **1213**: Light snow
- **1216**: Patchy moderate snow
- **1219**: Moderate snow
- **1222**: Patchy heavy snow
- **1225**: Heavy snow
- **1237**: Ice pellets
- **1240**: Light rain shower
- **1243**: Moderate or heavy rain shower
- **1246**: Torrential rain shower
- **1249**: Light sleet showers
- **1252**: Moderate or heavy sleet showers
- **1255**: Light snow showers
- **1258**: Moderate or heavy snow showers
- **1261**: Light showers of ice pellets
- **1264**: Moderate or heavy showers of ice pellets
- **1273**: Patchy light rain with thunder
- **1276**: Moderate or heavy rain with thunder
- **1279**: Patchy light snow with thunder
- **1282**: Moderate or heavy snow with thunder

## UK Defra 指数速查表

| 指数 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 等级 | 低 | 低 | 低 | 中 | 中 | 中 | 高 | 高 | 高 | 极高 |
| µgm-3 | 0-11 | 12-23 | 24-35 | 36-41 | 42-47 | 48-53 | 54-58 | 59-64 | 65-70 | 71以上 |

## 错误原因

- **no_location**: 用户尚未添加位置信息，或已将其删除。
- **location_invalid**: 用户的位置信息无效，无法获取数据。
- **api_quota_exceeded**: 已超过每月 100 万次免费 API 调用的上限。
- **api_key_disabled**: plugin 开发者已禁用 API 密钥。请检查是否有提供新密钥的 plugin 更新。
- **api_internal_error**: API 返回了内部错误。
- **no_api_response**: API 未响应、plugin 使用的 SAORI 运行失败，或用户处于离线状态。
- **other**: API 返回的其他错误。reference1 包含 API 返回的错误消息。
