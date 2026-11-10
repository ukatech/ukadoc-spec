# `\![execute,extractarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** 未分類命令

解壓縮 ZIP 檔案。建議使用完整路徑指定。若指定相對路徑，則會解讀為相對於 ghost/master/ 的路徑。<br />
選項如下。

- --event=事件識別子……指定事件識別子後，會在繼續執行 Sakura Script 的同時進行解壓縮，完成後觸發事件。若識別子以 On 開頭，則會觸發該識別子的事件；否則會觸發 OnExtractArchiveComplete 或 OnExtractArchiveFailure。省略時，會停止執行腳本，直到處理完成。
- --password=パスワード……使用指定的密碼展開，不會詢問密碼。

關於執行後事件的規格，請參閱 [OnExtractArchiveComplete](../../shiori-event/other/OnExtractArchiveComplete.md)・[OnExtractArchiveFailure](../../shiori-event/other/OnExtractArchiveFailure.md)。<br />
基於安全考量，解壓縮目的地僅限 SSP 管理的資料夾（ghost 資料夾、balloon 資料夾等由「資料夾」設定指定的位置）之下。<br />
此外，此限制可能會視情況加強，因此最好將解壓縮範圍限制在放置 ghost 本身資料的資料夾之下。

**対応:** SSP 選項指定支援 2.7.23 以上版本

## 記述例

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、test.zipをemily4フォルダに解凍する。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnExtractComplete]非同期で解凍を実行し、完了時にOnExtractCompleteイベントが発生する。
```
