# `\![execute,dropdefault,file,ファイルパス,ファイルパス...]` `\![execute,dropdefault,url,URL,種別]`

**カテゴリ:** Uncategorized commands

Perform the baseware's default action that was skipped because the ghost responded to a drag-and-drop event.<br />
Use this when you want to say something in response to a drop and then leave the rest to the baseware. It can be executed later, such as after an option has been selected, not only within the script that responded to the event.

- file……Perform the same action as when there was no response to [OnFileDrop2](../../shiori-event/file-drop/OnFileDrop2.md) (including OnFileDropEx and OnFileDrop). Open images with an image viewer, audio and video with a media player, and archives with an archive viewer. Do nothing with files that cannot be opened by any of these (they are not opened with the associated application).<br />
  For the file paths, you can pass Reference0 of OnFileDrop2 (separated by byte value 1) as is, or list multiple paths separated by commas. If a path contains a comma, enclose it in " ". Relative paths are resolved from the ghost's folder (ghost/master).<br />
  Since there was originally no action for directories when the ghost did not respond, do nothing if the first item is a directory.<br />
  Installing nar and SSF files and changing the wallpaper ([OnWallpaperChange](../../shiori-event/file-drop/OnWallpaperChange.md)) are handled before OnFileDrop2, so this tag does not perform those actions.
- url……Perform the same action as when there was no response to [OnURLQuery](../../shiori-event/url-drop/OnURLQuery.md). Pass Reference3 of OnURLQuery as the type.<br />
  Do nothing if the type is unknown. If the type is omitted, determine it again from the Content-Type and file contents (this causes another network request for identification).<br />
  This performs the same action as [`\![execute,install,url]`](bang-execute-install-url-URL.md), but the scope number of events such as OnURLDropping that occur afterward is the scope that executed this tag.

Events [OnPictureViewerOpen](../../shiori-event/file-drop/OnPictureViewerOpen.md), [OnMediaPlayerOpen](../../shiori-event/file-drop/OnMediaPlayerOpen.md), and [OnArchiveViewerOpen](../../shiori-event/file-drop/OnArchiveViewerOpen.md) also occur for image viewers and other applications opened with this tag. Reference1 (scope number) is the scope that executed this tag.

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\0画像を見せてくれるの？\![execute,dropdefault,file,"C:/Users/user/Pictures/photo.png"]OnFileDrop2に応答して喋ったうえで、ドロップされた画像を画像ビューアーで開く。実際にはOnFileDrop2のReference0をそのまま渡す。
```

```sakurascript
\0ダウンロードするね。\![execute,dropdefault,url,http://ssp.shillest.net/ghost/emily4.nar,nar]OnURLQueryに応答して喋ったうえで、本来の処理(この場合はnarのダウンロードとインストール)を続ける。実際にはOnURLQueryのReference0とReference3をそのまま渡す。
```
