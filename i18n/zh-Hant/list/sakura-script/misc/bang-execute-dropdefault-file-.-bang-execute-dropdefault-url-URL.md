# `\![execute,dropdefault,file,ファイルパス,ファイルパス...]` `\![execute,dropdefault,url,URL,種別]`

**カテゴリ:** 未分類コマンド

ghost 回應拖放事件後，執行原本未執行的 baseware 預設處理。<br />
適用於希望在接收檔案後先說些話，再將後續處理交給 baseware 的情況。不只能在回應事件的 script 中使用，也可以在選擇選項後等較晚的時機執行。

- file……執行與未回應[OnFileDrop2](../../shiori-event/file-drop/OnFileDrop2.md)（包含 OnFileDropEx、OnFileDrop 等）時相同的處理。圖片會以圖片檢視器開啟，音訊與影片會以媒體播放器開啟，壓縮檔會以封存檔檢視器開啟。無法以任何一種方式開啟的檔案不會進行任何處理（不會以關聯的應用程式開啟）。<br />
  檔案路徑可以直接傳入 OnFileDrop2 的 Reference0（以 byte 值 1 分隔），也可以用逗號分隔並列出多個路徑。路徑包含逗號時，請以 " " 括住。相對路徑以 ghost 資料夾（ghost/master）為基準。<br />
  由於原本在未回應的情況下不會對目錄進行處理，因此若開頭是目錄，則不會進行任何處理。<br />
  nar 或 SSF 的安裝，以及桌布變更（[OnWallpaperChange](../../shiori-event/file-drop/OnWallpaperChange.md)）會在 OnFileDrop2 之前處理，因此不會由此標籤執行。
- url……執行與未回應[OnURLQuery](../../shiori-event/url-drop/OnURLQuery.md)時相同的處理。種類直接傳入 OnURLQuery 的 Reference3。<br />
  種類為 unknown 時不會進行任何處理。省略種類時，會根據 Content-Type 和檔案內容重新判別（判別時會再次進行通訊）。<br />
  處理方式與[`\![execute,install,url]`](bang-execute-install-url-URL.md)相同，但之後發生的 OnURLDropping 等事件，其 scope 編號會是執行此標籤的 scope。

使用此標籤開啟圖片檢視器等時，也會發生[OnPictureViewerOpen](../../shiori-event/file-drop/OnPictureViewerOpen.md)、[OnMediaPlayerOpen](../../shiori-event/file-drop/OnMediaPlayerOpen.md)、[OnArchiveViewerOpen](../../shiori-event/file-drop/OnArchiveViewerOpen.md)。Reference1（scope 編號）會是執行此標籤的 scope。

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\0画像を見せてくれるの？\![execute,dropdefault,file,"C:/Users/user/Pictures/photo.png"]OnFileDrop2に応答して喋ったうえで、ドロップされた画像を画像ビューアーで開く。実際にはOnFileDrop2のReference0をそのまま渡す。
```

```sakurascript
\0ダウンロードするね。\![execute,dropdefault,url,http://ssp.shillest.net/ghost/emily4.nar,nar]OnURLQueryに応答して喋ったうえで、本来の処理(この場合はnarのダウンロードとインストール)を続ける。実際にはOnURLQueryのReference0とReference3をそのまま渡す。
```
