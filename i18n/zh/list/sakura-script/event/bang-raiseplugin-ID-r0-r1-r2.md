# `\![raiseplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Sends the specified event to a plugin.<br />
Setting the plugin name to random selects one at random.<br />
Setting it to lastinstalled starts the last plugin installed.

**対応:** SSP

## 記述例

```sakurascript
\![raiseplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」に、[実行したゴーストのフォルダ]/ghost/master/stamp.pngの画像とメッセージを登録する。
```
