# `\![execute,http-get,URL,パラメータ]`

**カテゴリ:** 未分類命令

發送附帶參數的 HTTP GET 請求，並將回應存入檔案。<br />
檔案會存放在\[執行中的 ghost 資料夾\]/ghost/master/var 資料夾。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://search.yahoo.co.jp/search,p=SSP 伺か]YAHOOでの「SSP 伺か」の検索結果ページを、そのまま保存する。
```
