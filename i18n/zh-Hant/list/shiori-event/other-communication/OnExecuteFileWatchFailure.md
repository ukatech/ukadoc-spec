# OnExecuteFileWatchFailure

**カテゴリ:** Other communication events

Occurs when [`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md) fails or monitoring can no longer continue. In this case, monitoring is stopped.

If an ID beginning with On is specified with --async, the event name is that ID followed by Failure.

- **Reference0**: The exact string specified with --async (empty if none)
- **Reference1**: The exact string of the specified path
- **Reference2**: Reason for failure<br />
  notauthorized: Attempted to monitor using a script sent from outside, such as via SSTP<br />
  invalid: No path was specified<br />
  notfound: The directory being monitored (or, for a file, the directory containing it) does not exist, monitoring cannot be started, or it disappeared during monitoring<br />
  limit: The number of types of directories monitored across SSP exceeds the limit (63)

**対応:** SSP 2.8.91
