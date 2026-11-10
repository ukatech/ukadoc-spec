# OnWeatherStation.Error

**カテゴリ:** Plugin "Weather Station"

Sends error information to all running ghosts. If an error occurs, this event is sent instead of the event described above.

- **Reference0**: Error message. See [below](note-1.md#エラーの理由) for possible error messages.
- **Reference1**: A more detailed error message provided by weatherapi.com. *This error message does not match the weatherapi online documentation, so it must not be used to identify errors.*
- **Reference2**: Error code documented by weatherapi.com.
- **Reference3**: The time when the plugin last attempted to update weather data, in seconds since EPOCH (1970/1/1 00:00:00).
- **Reference4**: The plugin's current version number.
- **Reference5**: 1 if a plugin update is available, or 0 otherwise. Always 0 if the user is offline.
