# OnSNTPCorrect

**カテゴリ:** Clock synchronization event

Occurs when the local time is corrected to match the server time using the [`\6` tag](../../sakura-script/event/6.md).

Also occurs when the OS clock is not actually corrected, such as when automatic time synchronization is enabled in the OS and the difference is small (within 60 seconds) (SSP 2.9.40 and later). Reference5 indicates whether the clock was corrected.

- **Reference0**: Name of the server connected to.
- **Reference1**: Current server time, comma-separated: year, month, day, hour, minute, second (same as local time if the difference is less than 1 second).
- **Reference2**: Current local time, comma-separated: year, month, day, hour, minute, second.
- **Reference3**: Difference between server and local time, as an integer in seconds. A positive value means the local time is behind; a negative value means it is ahead.
- **Reference4**: SSP only. Difference between server and local time, as an integer in milliseconds.
- **Reference5**: SSP only. Whether the OS clock was actually corrected (SSP 2.9.40 and later). 1 if corrected, 0 if not. When automatic time synchronization is enabled in the OS and the difference is within 60 seconds, correction is left to the OS.

**対応:** Materia / SSP / CROW
