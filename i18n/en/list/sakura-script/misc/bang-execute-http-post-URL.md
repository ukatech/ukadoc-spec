# `\![execute,http-post,URL,パラメータ]`

**カテゴリ:** Unclassified command

Sends an HTTP POST request with parameters and stores the response in a file.<br />
The file is stored in the ghost/master/var folder of the ghost that executed it.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-post,http://jbbs.shitaraba.net/bbs/read.cgi/computer/44300/1432574039/,BBS=44300&KEY=1432574039&DIR=computer&MESSAGE=テストメッセージ]ゴースト回覧板３ｒｄの、テストスレに「テストメッセージ」と本文に入れて送信する。※したらば掲示板がスパム対策を強化したため現在書き込み不可。
```
