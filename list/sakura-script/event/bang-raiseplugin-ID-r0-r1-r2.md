# `\![raiseplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** イベントコマンド

プラグインに指定したイベントを送信する。<br />
プラグイン名をrandomにするとランダムに選択。<br />
\[SSP 2.9.35\] プラグインの[UUID](../../propertysystem/property-system/general-property/uuid.md)も指定できる。IDまたは名前に一致しなかったときに照合する。<br />
lastinstalledにすると最後にインストールされたプラグインを開始。

**対応:** SSP

## 記述例

```sakurascript
\![raiseplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」に、[実行したゴーストのフォルダ]/ghost/master/stamp.pngの画像とメッセージを登録する。
```
