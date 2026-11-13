# `\![raiseplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

向 plugin 傳送指定的事件。<br />
將 plugin 名稱設為 random 時，隨機選擇。<br />
\[SSP 2.9.35\] 也可指定 plugin 的 [UUID](../../propertysystem/property-system/general-property/uuid.md)。當 ID 或名稱不符合時會進行比對。<br />
設為 lastinstalled 時，啟動最後安裝的 plugin。

**対応:** SSP

## 記述例

```sakurascript
\![raiseplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」に、[実行したゴーストのフォルダ]/ghost/master/stamp.pngの画像とメッセージを登録する。
```
