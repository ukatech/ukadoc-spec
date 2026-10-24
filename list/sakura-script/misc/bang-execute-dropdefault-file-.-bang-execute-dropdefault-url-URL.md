# `\![execute,dropdefault,file,ファイルパス,ファイルパス...]` `\![execute,dropdefault,url,URL,種別]`

**カテゴリ:** 未分類コマンド

ドラッグ＆ドロップのイベントにゴーストが応答したことで行われなかった、本体の既定の処理を行う。<br />
ドロップを受けて何か喋ったうえで、続きは本体に任せたい場合に使う。イベントに応答したスクリプトの中だけでなく、選択肢を選んだ後など、後から実行してもよい。

- file……[OnFileDrop2](../../shiori-event/file-drop/OnFileDrop2.md)(OnFileDropEx・OnFileDropなどを含む)に応答しなかった場合と同じ処理を行う。画像は画像ビューアー、音声・動画はメディアプレーヤー、書庫はアーカイブビューアーで開く。いずれでも開けないファイルには何もしない(関連付けられたアプリケーションでは開かない)。<br />
  ファイルパスには、OnFileDrop2のReference0(byte値1区切り)をそのまま渡してもよいし、カンマで区切って複数並べてもよい。パスにカンマが含まれる場合は " " で囲むこと。相対パスはゴーストのフォルダ(ghost/master)基準。<br />
  ディレクトリには、ゴーストが応答しなかった場合の処理が元々無いため、先頭がディレクトリの場合は何もしない。<br />
  narやSSFのインストール、壁紙の変更([OnWallpaperChange](../../shiori-event/file-drop/OnWallpaperChange.md))はOnFileDrop2より前に処理されるため、このタグでは行わない。
- url……[OnURLQuery](../../shiori-event/url-drop/OnURLQuery.md)に応答しなかった場合と同じ処理を行う。種別にはOnURLQueryのReference3をそのまま渡す。<br />
  種別がunknownの場合は何もしない。種別を省略した場合はContent-Typeとファイルの中身から判別し直す(判別のための通信がもう一度発生する)。<br />
  [`\![execute,install,url]`](bang-execute-install-url-URL.md)と同じ処理だが、その後に発生するOnURLDroppingなどのイベントのスコープ番号は、このタグを実行したスコープになる。

このタグで開いた画像ビューアーなどについても、[OnPictureViewerOpen](../../shiori-event/file-drop/OnPictureViewerOpen.md)・[OnMediaPlayerOpen](../../shiori-event/file-drop/OnMediaPlayerOpen.md)・[OnArchiveViewerOpen](../../shiori-event/file-drop/OnArchiveViewerOpen.md)は発生する。Reference1(スコープ番号)は、このタグを実行したスコープになる。

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\0画像を見せてくれるの？\![execute,dropdefault,file,"C:/Users/user/Pictures/photo.png"]OnFileDrop2に応答して喋ったうえで、ドロップされた画像を画像ビューアーで開く。実際にはOnFileDrop2のReference0をそのまま渡す。
```

```sakurascript
\0ダウンロードするね。\![execute,dropdefault,url,http://ssp.shillest.net/ghost/emily4.nar,nar]OnURLQueryに応答して喋ったうえで、本来の処理(この場合はnarのダウンロードとインストール)を続ける。実際にはOnURLQueryのReference0とReference3をそのまま渡す。
```
