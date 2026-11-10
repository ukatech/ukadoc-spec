# `\j[ID]`

**カテゴリ:** 開啟命令

跳轉至 ID。<br />
若為 http://～，則會跳轉至 URL。<br />
若為 file:///～，則會以 OS 關聯的副檔名執行檔案。檔案名稱除了可使用絕對路徑，也可使用相對於\[執行中的 ghost 資料夾\]/ghost/master 的路徑。<br />
※僅 SSP 支援 mailto:～，可建立寄給該收件者的新郵件。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\j[http://ssp.shillest.net/]ばぐとら研究所をブラウザを立ち上げて表示する。
```

```sakurascript
\j[file:///descript.txt][実行したゴーストのフォルダ]/ghost/masterフォルダにあるdescript.txtを開く。
```
