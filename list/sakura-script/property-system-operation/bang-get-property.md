# `\![get,property,イベント名,プロパティ名,プロパティ名,...]`

**カテゴリ:** プロパティシステム操作コマンド

プロパティシステムの値の取得。<br />
イベント名で指定したイベントが発生し、そのreference0以降にひとつずつプロパティシステムの値が入る。<br />
※プロパティシステムの詳細は[プロパティシステム](../../propertysystem/index.md)のページ参照。

**対応:** SSP / CROW

## 記述例

```sakurascript
このスクリプトの再生後、SHIORIイベント「SSPからバルーン情報取得」が通知される。Reference0に現在使用中のバルーンの、本体側の表示可能な幅(ピクセル数)、Reference1にその高さが入っている。\![get,property,SSPからバルーン情報取得,currentghost.balloon.scope(0).validwidth.initial,currentghost.balloon.scope(0).validheight.initial]
```
