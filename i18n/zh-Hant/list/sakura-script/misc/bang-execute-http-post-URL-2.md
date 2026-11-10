# `\![execute,http-post,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類命令

使用[※選項](bang-execute-http-options-URL.note.md)執行 HTTP POST 請求，並將回應儲存為檔案。<br />
檔案會儲存在\[執行中的 ghost 資料夾\]/ghost/master/var 資料夾。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-post,http://jbbs.shitaraba.net/bbs/read.cgi/computer/44300/1432574039/,--async=書き込みテスト,--param=BBS=44300&KEY=1432574039&DIR=computer&MESSAGE=テストメッセージ]ゴースト回覧板３ｒｄの、テストスレに「テストメッセージ」と本文に入れて送信する。5秒応答がなければタイムアウトする。※したらば掲示板がスパム対策を強化したため現在書き込み不可。
```
