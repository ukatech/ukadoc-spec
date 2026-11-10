# `\![update,platform]`

**カテゴリ:** Event command

Start a baseware network update event.<br />
If an update is available, the ghost exits first ([OnBasewareUpdating](../../shiori-event/boot-close-change/OnBasewareUpdating.md), or [OnClose](../../shiori-event/boot-close-change/OnClose.md) if there is no talk) and then starts again ([OnBasewareUpdated](../../shiori-event/boot-close-change/OnBasewareUpdated.md), or [OnBoot](../../shiori-event/boot-close-change/OnBoot.md) if there is no talk).<br />
If there is no update, only a popup is displayed and no SHIORI event occurs.

**対応:** SSP / CROW

## 記述例

```sakurascript
ベースウェアの更新を実行。\![update,platform]
```
