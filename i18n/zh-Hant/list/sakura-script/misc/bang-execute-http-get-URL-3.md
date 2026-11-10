# `\![execute,http-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類命令

使用[※選項](bang-execute-http-options-URL.note.md)發送 HTTP GET 請求，並將回應存入檔案。<br />
檔案會存放在\[執行中的 ghost 資料夾\]/ghost/master/var 資料夾。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://search.yahoo.co.jp/search,--async=伺か検索,--file=検索結果ファイル.txt,--nodescript,--param=p=SSP 伺か,--timeout=5]YAHOOでの「SSP 伺か」の検索結果ページを、[実行したゴーストのフォルダ]/ghost/master/var/検索結果ファイル.txtに保存する。実行時、オンラインマーカーやダウンロード状況を出さない。5秒応答がなければタイムアウトする。
```
