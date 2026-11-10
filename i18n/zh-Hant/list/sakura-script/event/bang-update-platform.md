# `\![update,platform]`

**カテゴリ:** 事件指令

開始 baseware 的網路更新事件。<br />
若有更新，ghost 會先結束（[OnBasewareUpdating](../../shiori-event/boot-close-change/OnBasewareUpdating.md)，若沒有對應對話則為 [OnClose](../../shiori-event/boot-close-change/OnClose.md)），然後重新啟動（[OnBasewareUpdated](../../shiori-event/boot-close-change/OnBasewareUpdated.md)，若沒有對應對話則為 [OnBoot](../../shiori-event/boot-close-change/OnBoot.md)）。<br />
若沒有更新，只會顯示彈出視窗，不會觸發任何 SHIORI 事件。

**対応:** SSP / CROW

## 記述例

```sakurascript
ベースウェアの更新を実行。\![update,platform]
```
