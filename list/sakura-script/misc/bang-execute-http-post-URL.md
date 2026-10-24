# `\![execute,http-post,URL,パラメータ]`

**カテゴリ:** 未分類コマンド

パラメータ付きでhttp post リクエストを行い、レスポンスをファイルに格納する。<br />
ファイルは\[実行したゴーストのフォルダ\]/ghost/master/varフォルダに格納される。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-post,http://jbbs.shitaraba.net/bbs/read.cgi/computer/44300/1432574039/,BBS=44300&KEY=1432574039&DIR=computer&MESSAGE=テストメッセージ]ゴースト回覧板３ｒｄの、テストスレに「テストメッセージ」と本文に入れて送信する。※したらば掲示板がスパム対策を強化したため現在書き込み不可。
```
