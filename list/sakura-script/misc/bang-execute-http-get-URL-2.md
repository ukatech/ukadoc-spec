# `\![execute,http-get,URL,パラメータ]`

**カテゴリ:** 未分類コマンド

パラメータ付きでhttp get リクエストを行い、レスポンスをファイルに格納する。<br />
ファイルは\[実行したゴーストのフォルダ\]/ghost/master/varフォルダに格納される。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://search.yahoo.co.jp/search,p=SSP 伺か]YAHOOでの「SSP 伺か」の検索結果ページを、そのまま保存する。
```
