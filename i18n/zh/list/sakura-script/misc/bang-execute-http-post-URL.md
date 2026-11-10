# `\![execute,http-post,URL,パラメータ]`

**カテゴリ:** 未分类命令

发送带参数的 http post 请求，并将响应保存到文件中。<br />
文件保存在\[执行该命令的 ghost 文件夹\]/ghost/master/var 文件夹中。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![execute,http-post,http://jbbs.shitaraba.net/bbs/read.cgi/computer/44300/1432574039/,BBS=44300&KEY=1432574039&DIR=computer&MESSAGE=テストメッセージ]ゴースト回覧板３ｒｄの、テストスレに「テストメッセージ」と本文に入れて送信する。※したらば掲示板がスパム対策を強化したため現在書き込み不可。
```
