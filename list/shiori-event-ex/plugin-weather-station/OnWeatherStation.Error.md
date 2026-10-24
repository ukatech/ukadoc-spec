# OnWeatherStation.Error

**カテゴリ:** プラグイン「Weather Station」

Sends error information to all open ghosts. This event is sent in place of the previous events if there is an error of any kind.

- **Reference0**: The error message. [※See below](note-1.md#uk-defra-index-reference) for possible error messages.
- **Reference1**: A more descriptive error message, provided by weatherapi.com. *These error messages do not match the online documentation for weatherapi and should not be used for identifying errors.*
- **Reference2**: The error code, as listed on weatherapi.com's documentation.
- **Reference3**: The time the plugin last attempted to update the weather data, in seconds since EPOCH (1970/1/1 00:00:00).
- **Reference4**: The current version number of the plugin.
- **Reference5**: 1 if there is a plugin update available, 0 otherwise. If the user is offline, this will always be 0.
