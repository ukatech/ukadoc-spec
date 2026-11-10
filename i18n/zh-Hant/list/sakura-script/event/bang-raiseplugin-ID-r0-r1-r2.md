# `\![raiseplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

傳送指定的事件給 plugin。<br />
將 plugin 名稱設為 random，即可隨機選擇。<br />
設為 lastinstalled，則會啟動最後安裝的 plugin。

**対応:** SSP

## 記述例

```sakurascript
\![raiseplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」に、[実行したゴーストのフォルダ]/ghost/master/stamp.pngの画像とメッセージを登録する。
```
