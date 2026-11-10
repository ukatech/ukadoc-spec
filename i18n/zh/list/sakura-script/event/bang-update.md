# `\![update,更新対象(,オプション,オプション...)]`

**カテゴリ:** 事件命令

开始指定更新对象的网络更新事件。<br />
可以指定ghost、shell、balloon；需要同时更新时，可用「+」分隔指定。<br />
将更新对象指定为all时，与`\![updatebymyself]`含义相同。<br />
指定`\![update,ghost+shell+balloon]`时，与`\![updatebymyself]`不同，无论SSP本体设置如何，都会强制执行更新。<br />
更新ghost以外的对象时，如果有更新，会通知SHIORI事件[OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md)等事件组，其中OnUpdate会变为OnUpdateOther；全部更新完成后，会触发[OnUpdateResult](../../shiori-event/network-update/OnUpdateResult.md)汇总结果。<br />
选项仅限SSP。[更新选项指定](note-1.md#補足)请参阅。

**対応:** SSP

## 記述例

```sakurascript
シェルの更新を実行。\![update,shell]
```
