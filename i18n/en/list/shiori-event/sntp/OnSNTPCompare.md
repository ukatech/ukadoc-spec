# OnSNTPCompare

**カテゴリ:** Time synchronization events

Occurs when a connection to the server is established. To apply the correction, return a script containing the [`\6` tag](../../sakura-script/event/6.md).

- **Reference0**: Name of the server to connect to.
- **Reference1**: Server's current time, comma-separated: year,month,day,hour,minute,second (if the difference is less than 1 second, this is the same as the local time)
- **Reference2**: Local current time, comma-separated: year,month,day,hour,minute,second
- **Reference3**: Difference between the server and local times. Always a positive integer in seconds.
- **Reference4**: SSP only. Difference between the server and local times. Always a positive integer in milliseconds.

**対応:** Materia / SSP / CROW
