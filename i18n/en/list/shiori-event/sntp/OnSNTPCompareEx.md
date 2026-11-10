# OnSNTPCompareEx

**カテゴリ:** Time synchronization events

Occurs when a connection to the server is established. To apply the correction, return a script containing the [`\6` tag](../../sakura-script/event/6.md).

- **Reference0**: Name of the server to connect to.
- **Reference1**: Server's current time, comma-separated: year,month,day,hour,minute,second,millisecond
- **Reference2**: Local current time, comma-separated: year,month,day,hour,minute,second,millisecond
- **Reference3**: Difference between the server and local times. In seconds, with a fractional part. Positive values mean the local clock is behind; negative values mean it is ahead.
- **Reference4**: Difference between the server and local times. Integer in milliseconds.

**対応:** SSP 2.5.66
