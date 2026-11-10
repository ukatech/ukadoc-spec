# `\![execute,http-get,URL,パラメータ]`

**カテゴリ:** Uncategorized command

Send an http get request with parameters and store the response in a file.<br />
The file is stored in the /ghost/master/var folder under the \[folder of the executing ghost\].

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://search.yahoo.co.jp/search,p=SSP 伺か]YAHOOでの「SSP 伺か」の検索結果ページを、そのまま保存する。
```
