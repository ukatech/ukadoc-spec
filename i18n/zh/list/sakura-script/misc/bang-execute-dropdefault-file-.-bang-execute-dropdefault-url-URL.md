# `\![execute,dropdefault,file,ファイルパス,ファイルパス...]` `\![execute,dropdefault,url,URL,種別]`

**カテゴリ:** Uncategorized command

Performs the baseware's default action that was skipped because the ghost responded to a drag-and-drop event.<br />
Use this when the ghost has said something in response to a drop, but you want the baseware to handle what happens next. It can be executed later, such as after an option is selected, not only within the script that responded to the event.

- file……Performs the same action as when the ghost does not respond to [OnFileDrop2](../../shiori-event/file-drop/OnFileDrop2.md) (including OnFileDropEx and OnFileDrop). Images are opened in an image viewer, audio and video in a media player, and archives in an archive viewer. Files that cannot be opened by any of these are ignored (they are not opened with their associated applications).<br />
  For the file paths, you can pass Reference0 of OnFileDrop2 (separated by byte value 1) as-is, or provide multiple paths separated by commas. If a path contains a comma, enclose it in " ". Relative paths are relative to the ghost's folder (ghost/master).<br />
  Since there is no default action for directories when the ghost does not respond, nothing happens if the first item is a directory.<br />
  Installing NARs or SSFs and changing the wallpaper ([OnWallpaperChange](../../shiori-event/file-drop/OnWallpaperChange.md)) are handled before OnFileDrop2, so this tag does not perform those actions.
- url……Performs the same action as when the ghost does not respond to [OnURLQuery](../../shiori-event/url-drop/OnURLQuery.md). Pass Reference3 of OnURLQuery as the type.<br />
  If the type is unknown, nothing happens. If the type is omitted, it is determined again from the Content-Type and file contents (this requires another network request).<br />
  This performs the same action as [`\![execute,install,url]`](bang-execute-install-url-URL.md), but the scope number of subsequent events such as OnURLDropping is the scope that executed this tag.

Events such as [OnPictureViewerOpen](../../shiori-event/file-drop/OnPictureViewerOpen.md), [OnMediaPlayerOpen](../../shiori-event/file-drop/OnMediaPlayerOpen.md), and [OnArchiveViewerOpen](../../shiori-event/file-drop/OnArchiveViewerOpen.md) are also triggered for image viewers and other applications opened by this tag. Reference1 (the scope number) is the scope that executed this tag.

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\0画像を見せてくれるの？\![execute,dropdefault,file,"C:/Users/user/Pictures/photo.png"]OnFileDrop2に応答して喋ったうえで、ドロップされた画像を画像ビューアーで開く。実際にはOnFileDrop2のReference0をそのまま渡す。
```

```sakurascript
\0ダウンロードするね。\![execute,dropdefault,url,http://ssp.shillest.net/ghost/emily4.nar,nar]OnURLQueryに応答して喋ったうえで、本来の処理(この場合はnarのダウンロードとインストール)を続ける。実際にはOnURLQueryのReference0とReference3をそのまま渡す。
```
