# `\![execute,compressarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** 未分類指令

壓縮 ZIP 檔案。建議使用完整路徑指定。若指定相對路徑，則會解讀為相對於 ghost/master/ 的路徑。<br />
選項如下。

- --event=事件識別子……指定事件識別子後，會在繼續執行 Sakura Script 的同時進行壓縮，完成後便會觸發事件。若識別子以 On 開頭，則會觸發該識別子的事件；否則會觸發 OnCompressArchiveComplete 或 OnCompressArchiveFailure。省略時，會停止執行指令碼，直到處理完成。
- --password=密碼……使用指定的密碼啟用 AES 加密 ZIP。

關於執行後事件的規格，請參閱 [OnCompressArchiveComplete](../../shiori-event/other/OnCompressArchiveComplete.md)・[OnCompressArchiveFailure](../../shiori-event/other/OnCompressArchiveFailure.md)。<br />
目錄名稱請指定資料夾。\[SSP 2.9.33\] 若指定的不是資料夾（例如檔案路徑），則不會進行壓縮並會失敗（若有附加 `--event=`，失敗事件（OnCompressArchiveFailure，或在識別子後加上 `Failure` 的事件）的 `Reference1` 會是 `invalid parameter`）。<br />
基於安全考量，壓縮目的地限制為 SSP 管理下的資料夾（ghost 資料夾、balloon 資料夾等「資料夾」設定所指定的位置）之下。<br />
此外，此限制可能會視情況加強，因此最好將範圍限制在存放 ghost 自身資料的資料夾之下。

**対応:** SSP 選項指定功能自 2.7.23 起支援

## 記述例

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、Emily/Phase4.5のフォルダをtest.zipに圧縮してghostフォルダに置く。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnCompressComplete]非同期で圧縮を実行し、完了時にOnCompressCompleteイベントが発生する。
```
