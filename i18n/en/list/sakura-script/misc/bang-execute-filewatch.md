# `\![execute,filewatch,パス,オプション...]`

**カテゴリ:** Uncategorized command

Start monitoring the specified file or directory, and notify via [OnExecuteFileWatchChange](../../shiori-event/other-communication/OnExecuteFileWatchChange.md) each time it changes. If monitoring cannot be started, or if the monitored directory disappears while being monitored, [OnExecuteFileWatchFailure](../../shiori-event/other-communication/OnExecuteFileWatchFailure.md) is raised and monitoring ends. This cannot be run from scripts sent externally, such as via SSTP.<br />
The parameters are as follows.

- Path……The file or directory to monitor. Relative paths are interpreted as relative to ghost/master/.
- --async=event or identifier……If a string beginning with On is specified, that event is raised instead of the event described below.
- --debounce=milliseconds……Wait for this duration after changes stop being reported, and notify if no further changes occur during that time. If changes continue, keep waiting, so a sequence of changes during writing is combined into a single notification. However, even if changes do not stop, notify once three times the specified duration has elapsed since the first change. Defaults to 500. If 0 is specified, notify immediately.

When a file is specified, updates, creation, and deletion are reported. A file that does not yet exist can also be specified; its creation will be reported. However, the directory containing the file must exist.<br />
When a directory is specified, only creation, deletion, renaming, and updating of files and directories immediately within it are reported. The changed file is not identified, and changes inside subdirectories are not reported. The directory must exist when monitoring starts (a path that does not exist is monitored as a file).<br />
Specifying the same path again replaces the previous specification. All monitoring is stopped when the ghost exits.

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,filewatch,config.json,--async=OnConfigChanged]ghost/master/config.jsonが変化するたびに、OnConfigChangedイベントが起きる。
```
