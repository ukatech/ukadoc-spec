# OnExecuteFileWatchChange

**カテゴリ:** Other communication events

Occurs when a file or directory monitored by [`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md) changes.

If an ID beginning with On is specified with --async, that ID becomes the event name.

Since writes to a file may occur many times in a short period, the event waits for the time specified by --debounce (500 milliseconds if omitted) after changes stop, then fires once for all of them. If writes occur with longer intervals, or if changes continue for three times the specified duration after the first change, a single save may cause the event to fire multiple times.

- **Reference0**: The exact string specified with --async (empty if not specified)
- **Reference1**: The exact string of the specified path
- **Reference2**: Type of change<br />
  For a file: modified (updated), created, deleted<br />
  For a directory: changed (a file or directory directly inside it was created, deleted, renamed, or updated), deleted (the directory itself no longer exists)
- **Reference3**: Full path of the monitored file or directory

**対応:** SSP 2.8.91
