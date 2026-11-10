# `\![execute,http-post,URL,オプション,オプション,オプション...]`

**カテゴリ:** Uncategorized command

Make an HTTP POST request with [※options](bang-execute-http-options-URL.note.md) and store the response in a file.<br />
The file is stored in the \[folder of the ghost that executed the command\]/ghost/master/var folder.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-post,http://jbbs.shitaraba.net/bbs/read.cgi/computer/44300/1432574039/,--async=書き込みテスト,--param=BBS=44300&KEY=1432574039&DIR=computer&MESSAGE=テストメッセージ]ゴースト回覧板３ｒｄの、テストスレに「テストメッセージ」と本文に入れて送信する。5秒応答がなければタイムアウトする。※したらば掲示板がスパム対策を強化したため現在書き込み不可。
```
