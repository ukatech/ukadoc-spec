# `\![update,更新対象(,オプション,オプション...)]`

**カテゴリ:** 事件指令

開始指定更新對象的網路更新事件。<br />
可指定 ghost、shell、balloon；若要同時更新多個對象，可用「+」連接指定。<br />
將更新對象指定為 all 時，與 `\![updatebymyself]` 相同。<br />
指定 `\![update,ghost+shell+balloon]` 時，與 `\![updatebymyself]` 不同，無論 SSP 本體設定為何，都會強制執行更新。<br />
更新 ghost 以外的對象時，若有更新，會通知 SHIORI 事件 [OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md) 等將 OnUpdate 改為 OnUpdateOther 的事件；全部更新完成後，會觸發 [OnUpdateResult](../../shiori-event/network-update/OnUpdateResult.md) 彙整結果。<br />
只有 SSP 支援指定選項。請參閱[更新選項設定](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
シェルの更新を実行。\![update,shell]
```
