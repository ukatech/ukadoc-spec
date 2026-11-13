# `\![notifyplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** Event commands

This is the same as raiseplugin, except that any value returned by the notification event is not reflected in SSP. A UUID can also be specified, as with raiseplugin.

**対応:** SSP

## 記述例

```sakurascript
\![notifyplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」の登録イベントをnotifyで呼び出す。プラグイン実行で処理は行われるが、ゴースト側への返答は無視される。
```
