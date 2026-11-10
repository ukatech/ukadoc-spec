# `\![update,platform]`

**カテゴリ:** 事件命令

开始更新baseware的网络更新事件。<br />
如果有更新，ghost会先结束（[OnBasewareUpdating](../../shiori-event/boot-close-change/OnBasewareUpdating.md)，如果没有对话则为[OnClose](../../shiori-event/boot-close-change/OnClose.md)），然后重新启动（[OnBasewareUpdated](../../shiori-event/boot-close-change/OnBasewareUpdated.md)，如果没有对话则为[OnBoot](../../shiori-event/boot-close-change/OnBoot.md)）。<br />
如果没有更新，则只会显示弹窗，不会触发任何SHIORI事件。

**対応:** SSP / CROW

## 記述例

```sakurascript
ベースウェアの更新を実行。\![update,platform]
```
