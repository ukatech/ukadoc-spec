# `\![execute,http-get,URL]`

**カテゴリ:** 未分類コマンド

http get リクエストを行い、レスポンスをファイルに格納する。<br />
ファイルは\[実行したゴーストのフォルダ\]/ghost/master/varフォルダに格納される。

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
\![execute,http-get,http://ssp.shillest.net/ukadoc/manual/list_sakura_script.html]ukadocのさくらスクリプトリスト(このページ)を取得し、varフォルダにlist_sakura_script.htmlを保存する。
```
