# Notes

## List of weather conditions and condition codes

The list of conditions can be downloaded from the [weatherapi documentation page](https://www.weatherapi.com/docs/). This list is also available in other languages, but the information sent by the plugin is always in English.

- **1000**: Sunny (after sunset, this changes to "Clear")
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

## Quick reference table for the UK Defra index

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Category | Low | Low | Low | Medium | Medium | Medium | High | High | High | Very high |
| µgm-3 | 0-11 | 12-23 | 24-35 | 36-41 | 42-47 | 48-53 | 54-58 | 59-64 | 65-70 | 71 or more |

## Error reasons

- **no_location**: The user has not added location information, or has removed it.
- **location_invalid**: The user's location information is invalid, so data cannot be retrieved.
- **api_quota_exceeded**: The free API call limit of 1 million per month has been exceeded.
- **api_key_disabled**: The plugin developer has disabled the API key. Check whether a plugin update providing a new key is available.
- **api_internal_error**: The API returned an internal error.
- **no_api_response**: The API did not respond, the SAORI used by the plugin failed to run, or the user is offline.
- **other**: Another error returned by the API. reference1 contains the error message returned by the API.
