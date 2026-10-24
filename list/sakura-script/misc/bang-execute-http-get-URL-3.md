# `\![execute,http-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

[※オプション](notes_executehttp.md)付きでhttp get リクエストを行い、レスポンスをファイルに格納する。<br />
ファイルは\[実行したゴーストのフォルダ\]/ghost/master/varフォルダに格納される。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://search.yahoo.co.jp/search,--async=伺か検索,--file=検索結果ファイル.txt,--nodescript,--param=p=SSP 伺か,--timeout=5]YAHOOでの「SSP 伺か」の検索結果ページを、[実行したゴーストのフォルダ]/ghost/master/var/検索結果ファイル.txtに保存する。実行時、オンラインマーカーやダウンロード状況を出さない。5秒応答がなければタイムアウトする。
```
