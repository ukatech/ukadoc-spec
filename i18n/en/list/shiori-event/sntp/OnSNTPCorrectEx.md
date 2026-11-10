# OnSNTPCorrectEx

**カテゴリ:** Time synchronization events

Occurs when the local time is corrected to match the server time using the [`\6` tag](../../sakura-script/event/6.md).

- **Reference0**: Name of the server to connect to.
- **Reference1**: Server's current time, comma-separated: year,month,day,hour,minute,second,millisecond
- **Reference2**: Local current time, comma-separated: year,month,day,hour,minute,second,millisecond
- **Reference3**: Difference between the server and local times. In seconds, with a fractional part. Positive values mean the local time is behind the server; negative values mean it is ahead of the server.
- **Reference4**: Difference between the server and local times. Integer in milliseconds. The sign follows the same convention as Reference3.

**対応:** SSP 2.5.66
