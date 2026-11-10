# `\![execute,dropdefault,file,ファイルパス,ファイルパス...]` `\![execute,dropdefault,url,URL,種別]`

**カテゴリ:** Uncategorized command

Perform the baseware's default action, which would not have run because the ghost responded to a drag-and-drop event.<br />
Use this when you want to say something in response to a drop and then let the baseware handle what comes next. It can be run later, such as after a choice is selected, not only within the script that responded to the event.

- file……Perform the same action as when there was no response to [OnFileDrop2](../../shiori-event/file-drop/OnFileDrop2.md) (including OnFileDropEx and OnFileDrop). Open images with an image viewer, audio and video with a media player, and archives with an archive viewer. Do nothing with files that cannot be opened by any of these (they are not opened with their associated applications).<br />
  For the file paths, you may pass the OnFileDrop2 Reference0 (separated by byte value 1) as-is, or list multiple paths separated by commas. If a path contains a comma, enclose it in " ". Relative paths are based on the ghost's folder (ghost/master).<br />
  Since there is no default action for directories when the ghost does not respond, do nothing if the first item is a directory.<br />
  Installing nar or SSF, and changing the wallpaper ([OnWallpaperChange](../../shiori-event/file-drop/OnWallpaperChange.md)), are handled before OnFileDrop2, so this tag does not perform these actions.
- url……Perform the same action as when there was no response to [OnURLQuery](../../shiori-event/url-drop/OnURLQuery.md). Pass the OnURLQuery Reference3 as the type.<br />
  Do nothing if the type is unknown. If the type is omitted, determine it again from the Content-Type and the file contents (this causes another network request for the determination).<br />
  This performs the same action as [`\![execute,install,url]`](bang-execute-install-url-URL.md), but the scope number for events such as OnURLDropping that occur afterward is the scope that executed this tag.

[OnPictureViewerOpen](../../shiori-event/file-drop/OnPictureViewerOpen.md), [OnMediaPlayerOpen](../../shiori-event/file-drop/OnMediaPlayerOpen.md), and [OnArchiveViewerOpen](../../shiori-event/file-drop/OnArchiveViewerOpen.md) also occur for image viewers and other applications opened by this tag. Reference1 (scope number) is the scope that executed this tag.

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\0画像を見せてくれるの？\![execute,dropdefault,file,"C:/Users/user/Pictures/photo.png"]OnFileDrop2に応答して喋ったうえで、ドロップされた画像を画像ビューアーで開く。実際にはOnFileDrop2のReference0をそのまま渡す。
```

```sakurascript
\0ダウンロードするね。\![execute,dropdefault,url,http://ssp.shillest.net/ghost/emily4.nar,nar]OnURLQueryに応答して喋ったうえで、本来の処理(この場合はnarのダウンロードとインストール)を続ける。実際にはOnURLQueryのReference0とReference3をそのまま渡す。
```
