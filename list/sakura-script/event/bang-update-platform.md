# `\![update,platform]`

**カテゴリ:** イベントコマンド

本体ネットワーク更新イベントを開始する。<br />
更新があった場合、ゴーストは一旦終了([OnBasewareUpdating](../../shiori-event/boot-close-change/OnBasewareUpdating.md)、トークがなければ[OnClose](../../shiori-event/boot-close-change/OnClose.md))して再度起動する([OnBasewareUpdated](../../shiori-event/boot-close-change/OnBasewareUpdated.md)、トークがなければ[OnBoot](../../shiori-event/boot-close-change/OnBoot.md))。<br />
更新が無い場合は、ポップアップが表示されるだけでSHIORIイベントは何も発生しない。

**対応:** SSP / CROW

## 記述例

```sakurascript
ベースウェアの更新を実行。\![update,platform]
```
