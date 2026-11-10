# `\![raiseplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Send the specified event to a plugin.<br />
Set the plugin name to random to select one at random.<br />
Set it to lastinstalled to start the last-installed plugin.

**対応:** SSP

## 記述例

```sakurascript
\![raiseplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」に、[実行したゴーストのフォルダ]/ghost/master/stamp.pngの画像とメッセージを登録する。
```
