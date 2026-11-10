# 補充說明

## 天氣狀況與狀況代碼一覽

狀況一覽可從[weatherapi 文件頁面](https://www.weatherapi.com/docs/)下載。此一覽也提供其他語言版本，但外掛傳送的資訊一律為英文。

- **1000**: Sunny（日落後會改為"Clear"）
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

## UK Defra 指數速查表

| 指數 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 區分 | 低 | 低 | 低 | 中 | 中 | 中 | 高 | 高 | 高 | 非常高 |
| µgm-3 | 0-11 | 12-23 | 24-35 | 36-41 | 42-47 | 48-53 | 54-58 | 59-64 | 65-70 | 71以上 |

## 錯誤原因

- **no_location**: 使用者尚未新增位置資訊，或已將其刪除。
- **location_invalid**: 使用者的位置資訊無效，無法取得資料。
- **api_quota_exceeded**: 超過每月100萬次免費 API 呼叫的上限。
- **api_key_disabled**: 外掛開發者已停用 API 金鑰。請確認外掛是否有提供新金鑰的更新。
- **api_internal_error**: API 傳回內部錯誤。
- **no_api_response**: API 沒有回應、外掛使用的 SAORI 執行失敗，或使用者目前離線。
- **other**: API 傳回的其他錯誤。reference1會包含 API 傳回的錯誤訊息。
