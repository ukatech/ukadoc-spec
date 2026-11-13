# `\![notifyplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

与 raiseplugin 相同，唯一区别是此通知事件即使返回值，也不会反映到 SSP 中。同样可以指定 UUID。

**対応:** SSP

## 記述例

```sakurascript
\![notifyplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」の登録イベントをnotifyで呼び出す。プラグイン実行で処理は行われるが、ゴースト側への返答は無視される。
```
