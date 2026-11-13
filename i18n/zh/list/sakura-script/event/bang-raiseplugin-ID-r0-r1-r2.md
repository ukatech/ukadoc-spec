# `\![raiseplugin,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

向 plugin 发送指定的事件。<br />
将 plugin 名称设为 random 时，随机选择。<br />
\[SSP 2.9.35\] 也可以指定 plugin 的 [UUID](../../propertysystem/property-system/general-property/uuid.md)。当 ID 或名称不匹配时进行匹配。<br />
设为 lastinstalled 时，启动最后安装的 plugin。

**対応:** SSP

## 記述例

```sakurascript
\![raiseplugin,スタンプ帳,OnStampAdd,[実行したゴーストのフォルダ]/ghost/master/stamp.png,マイスタンプ,スタンプを押したよ。よろしくね。]プラグイン「スタンプ帳」に、[実行したゴーストのフォルダ]/ghost/master/stamp.pngの画像とメッセージを登録する。
```
