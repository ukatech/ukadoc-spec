# `\![execute,http-get,URL]`

**カテゴリ:** 未分類命令

執行 HTTP GET 請求，並將回應存入檔案。<br />
檔案會存放在\[執行中的 ghost 資料夾\]/ghost/master/var 資料夾。

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://ssp.shillest.net/ukadoc/manual/list_sakura_script.html]ukadocのさくらスクリプトリスト(このページ)を取得し、varフォルダにlist_sakura_script.htmlを保存する。
```
