# 補足

## 天気の状況と状況コードの一覧

状況の一覧は[weatherapiのドキュメントページ](https://www.weatherapi.com/docs/)からダウンロードできる。この一覧は他の言語でも提供されているが、プラグインが送る情報は常に英語である。

- **1000**: Sunny（日没後は代わりに"Clear"になる）
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

## UK Defra指数の早見表

| 指数 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 区分 | 低 | 低 | 低 | 中 | 中 | 中 | 高 | 高 | 高 | 非常に高い |
| µgm-3 | 0-11 | 12-23 | 24-35 | 36-41 | 42-47 | 48-53 | 54-58 | 59-64 | 65-70 | 71以上 |

## エラーの理由

- **no_location**: ユーザーが位置情報を追加していない、または削除した。
- **location_invalid**: ユーザーの位置情報が無効で、データを取得できない。
- **api_quota_exceeded**: 月100万回の無料API呼び出しの上限を超えた。
- **api_key_disabled**: プラグインの開発者がAPIキーを無効にした。新しいキーが提供されるプラグインの更新がないか確認すること。
- **api_internal_error**: APIが内部エラーを返した。
- **no_api_response**: APIが応答しなかった、プラグインが使うSAORIが動作に失敗した、またはユーザーがオフラインである。
- **other**: APIが返したその他のエラー。reference1にはAPIが返したエラーメッセージが入る。
