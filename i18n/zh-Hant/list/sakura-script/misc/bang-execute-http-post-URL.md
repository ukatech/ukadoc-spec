# `\![execute,http-post,URL,パラメータ]`

**カテゴリ:** 未分類命令

執行帶有參數的 HTTP POST 請求，並將回應儲存為檔案。<br />
檔案會儲存在\[執行中的 ghost 資料夾\]/ghost/master/var 資料夾。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-post,http://jbbs.shitaraba.net/bbs/read.cgi/computer/44300/1432574039/,BBS=44300&KEY=1432574039&DIR=computer&MESSAGE=テストメッセージ]ゴースト回覧板３ｒｄの、テストスレに「テストメッセージ」と本文に入れて送信する。※したらば掲示板がスパム対策を強化したため現在書き込み不可。
```
