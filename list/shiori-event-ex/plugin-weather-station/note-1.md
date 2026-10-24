# 補足

## Weather Condition & Code List

A list of conditions can be downloaded from [weatherapi's documentation page](https://www.weatherapi.com/docs/). This list is also available in other languages, but information from the plugin will always be sent in english.

- **1000**: Sunny (If the sun is down, it will be "Clear" instead.)
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

## UK Defra Index reference

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Band | Low | Low | Low | Moderate | Moderate | Moderate | High | High | High | Very High |
| µgm-3 | 0-11 | 12-23 | 24-35 | 36-41 | 42-47 | 48-53 | 54-58 | 59-64 | 65-70 | 71 or more |

## Reason for Error

- **no_location**: The user has not added their location, or has removed it.
- **location_invalid**: The user's location is invalid and data cannot be gathered.
- **api_quota_exceeded**: The 1 million free API calls per month has been exceeded.
- **api_key_disabled**: The API key has been disabled by the plugin developer. Please check if a plugin update is available to provide a new key.
- **api_internal_error**: The API responded with an internal error.
- **no_api_response**: The API did not respond, the SAORI used by the plugin failed to work, or the user is offline.
- **other**: Any other error sent by the API. reference1 will have the error message provided by the API.
