# `\![execute,http-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

发送带有[※选项](bang-execute-http-options-URL.note.md)的 http get 请求，并将响应保存到文件中。<br />
文件保存在\[执行该命令的 ghost 文件夹\]/ghost/master/var 文件夹中。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://search.yahoo.co.jp/search,--async=伺か検索,--file=検索結果ファイル.txt,--nodescript,--param=p=SSP 伺か,--timeout=5]YAHOOでの「SSP 伺か」の検索結果ページを、[実行したゴーストのフォルダ]/ghost/master/var/検索結果ファイル.txtに保存する。実行時、オンラインマーカーやダウンロード状況を出さない。5秒応答がなければタイムアウトする。
```
