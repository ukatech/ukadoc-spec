# OnExecuteFileWatchFailure

**カテゴリ:** Other communication events

Occurs when [`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md) fails or monitoring can no longer continue. In this case, monitoring is stopped.

If an ID starting with On is specified with --async, the event name is that ID followed by Failure.

- **Reference0**: The exact string specified with --async (empty if not specified)
- **Reference1**: The exact string of the specified path
- **Reference2**: Reason for failure<br />
  notauthorized: Attempted to monitor using a script sent from an external source such as SSTP<br />
  invalid: No path was specified<br />
  notfound: The monitored directory (or, for a file, the directory containing that file) does not exist, monitoring cannot be started, or it no longer exists during monitoring<br />
  limit: The number of different directories monitored by SSP as a whole exceeds the limit (63)

**対応:** SSP 2.8.91
