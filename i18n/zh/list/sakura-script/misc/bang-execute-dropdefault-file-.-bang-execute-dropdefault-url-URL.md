# `\![execute,dropdefault,file,ファイルパス,ファイルパス...]` `\![execute,dropdefault,url,URL,種別]`

**カテゴリ:** 未分類命令

执行由于 ghost 响应拖放事件而未执行的 baseware 默认处理。<br />
适用于接收拖放内容并说了些什么之后，希望将后续处理交给 baseware 的情况。既可以在响应事件的脚本中使用，也可以在之后执行，例如选择选项之后。

- file……执行与未响应[OnFileDrop2](../../shiori-event/file-drop/OnFileDrop2.md)（包括 OnFileDropEx、OnFileDrop 等）时相同的处理。图像会由图像查看器打开，音频和视频会由媒体播放器打开，压缩包会由归档查看器打开。无法由这些程序打开的文件不会进行任何处理（不会通过关联的应用程序打开）。<br />
  文件路径可以直接传入 OnFileDrop2 的 Reference0（以字节值 1 分隔），也可以用逗号分隔并列出多个路径。路径中含有逗号时，需用 " " 括起来。相对路径以 ghost 文件夹（ghost/master）为基准。<br />
  由于原本就没有 ghost 未响应目录时的处理，因此如果第一个路径是目录，则不进行任何处理。<br />
  nar 或 SSF 的安装、壁纸更改（[OnWallpaperChange](../../shiori-event/file-drop/OnWallpaperChange.md)）会在 OnFileDrop2 之前处理，因此此标签不会执行这些操作。
- url……执行与未响应[OnURLQuery](../../shiori-event/url-drop/OnURLQuery.md)时相同的处理。种类直接传入 OnURLQuery 的 Reference3。<br />
  种类为 unknown 时不进行任何处理。省略种类时，会根据 Content-Type 和文件内容重新判断（为进行判断会再次通信）。<br />
  此标签执行的处理与 [`\![execute,install,url]`](bang-execute-install-url-URL.md) 相同，但之后发生的 OnURLDropping 等事件的 scope 编号将是执行此标签的 scope。

通过此标签打开图像查看器等时，也会触发 [OnPictureViewerOpen](../../shiori-event/file-drop/OnPictureViewerOpen.md)、[OnMediaPlayerOpen](../../shiori-event/file-drop/OnMediaPlayerOpen.md) 和 [OnArchiveViewerOpen](../../shiori-event/file-drop/OnArchiveViewerOpen.md)。Reference1（scope 编号）将是执行此标签的 scope。

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\0画像を見せてくれるの？\![execute,dropdefault,file,"C:/Users/user/Pictures/photo.png"]OnFileDrop2に応答して喋ったうえで、ドロップされた画像を画像ビューアーで開く。実際にはOnFileDrop2のReference0をそのまま渡す。
```

```sakurascript
\0ダウンロードするね。\![execute,dropdefault,url,http://ssp.shillest.net/ghost/emily4.nar,nar]OnURLQueryに応答して喋ったうえで、本来の処理(この場合はnarのダウンロードとインストール)を続ける。実際にはOnURLQueryのReference0とReference3をそのまま渡す。
```
