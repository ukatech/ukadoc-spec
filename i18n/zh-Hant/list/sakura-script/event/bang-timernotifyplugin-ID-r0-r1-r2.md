# `\![timernotifyplugin,時間,繰り返すか否か,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

與 timerraiseplugin 相同，差異僅在於即使此通知事件傳回任何值，也不會反映至 SSP。

**対応:** SSP

## 記述例

```sakurascript
\![notifyplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」の登録イベントをnotifyで呼び出す。プラグイン実行で処理は行われるが、ゴースト側への返答は無視される。
```
