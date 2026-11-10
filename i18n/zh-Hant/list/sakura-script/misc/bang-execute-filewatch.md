# `\![execute,filewatch,パス,オプション...]`

**カテゴリ:** Uncategorized command

Starts monitoring the specified file or directory and reports each change through [OnExecuteFileWatchChange](../../shiori-event/other-communication/OnExecuteFileWatchChange.md). If monitoring cannot be started, or if the monitored directory disappears while monitoring, [OnExecuteFileWatchFailure](../../shiori-event/other-communication/OnExecuteFileWatchFailure.md) is reported and monitoring ends. This cannot be executed with scripts sent from external sources such as SSTP.<br />
The parameters are as follows.

- Path……The file or directory to monitor. Relative paths are interpreted as paths relative to ghost/master/.
- --async=event or identifier……If a string beginning with On is specified, that event is triggered instead of the event described below.
- --debounce=milliseconds……Wait for this length of time after changes stop being reported, and report the change if no further change occurs during that time. If changes continue, keep waiting, so consecutive changes during writing are combined into a single notification. However, even if changes do not stop, a notification is sent when three times the specified duration has elapsed since the first change. Defaults to 500. If 0 is specified, notify without waiting.

If a file is specified, updates, creation, and deletion are reported. A file that does not yet exist can also be specified; its creation will be reported. However, the directory containing that file must exist.<br />
If a directory is specified, only creation, deletion, renaming, and updates of files and directories directly within it are reported. The changed file is not identified, and changes inside subdirectories are not reported. To monitor a path as a directory, that directory must exist when executed (a nonexistent path is monitored as a file).<br />
Specifying the same path again replaces the previous specification. All monitoring is stopped when the ghost exits.

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,filewatch,config.json,--async=OnConfigChanged]ghost/master/config.jsonが変化するたびに、OnConfigChangedイベントが起きる。
```
