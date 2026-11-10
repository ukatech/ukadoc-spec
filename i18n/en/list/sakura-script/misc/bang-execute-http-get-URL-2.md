# `\![execute,http-get,URL,パラメータ]`

**カテゴリ:** Uncategorized command

Performs an HTTP GET request with parameters and stores the response in a file.<br />
The file is stored in the \[folder of the ghost that executed it\]/ghost/master/var folder.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://search.yahoo.co.jp/search,p=SSP 伺か]YAHOOでの「SSP 伺か」の検索結果ページを、そのまま保存する。
```
