# OnSNTPCorrectEx

**カテゴリ:** Clock synchronization event

Occurs when the local time is corrected to match the server time using the [`\6` tag](../../sakura-script/event/6.md).

Also occurs when the OS clock is not actually corrected, such as when automatic time synchronization is enabled in the OS and the difference is small (within 60 seconds) (SSP 2.9.40 and later). Reference5 indicates whether the clock was corrected.

- **Reference0**: Name of the server connected to.
- **Reference1**: Current server time, comma-separated: year, month, day, hour, minute, second, millisecond.
- **Reference2**: Current local time, comma-separated: year, month, day, hour, minute, second, millisecond.
- **Reference3**: Difference between server and local time, in seconds with a fractional part. A positive value means the local time is behind the server time; a negative value means it is ahead.
- **Reference4**: Difference between server and local time, as an integer in milliseconds. The sign has the same meaning as in Reference3.
- **Reference5**: SSP only. Whether the OS clock was actually corrected (SSP 2.9.40 and later). 1 if corrected, 0 if not. When automatic time synchronization is enabled in the OS and the difference is within 60 seconds, correction is left to the OS.

**対応:** SSP 2.5.66
