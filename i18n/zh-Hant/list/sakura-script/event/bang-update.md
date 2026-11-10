# `\![update,更新対象(,オプション,オプション...)]`

**カテゴリ:** Event command

Start a network update event for the specified update targets.<br />
ghost, shell, and balloon can be specified. To update multiple targets at once, separate them with 「+」.<br />
Setting the update target to all has the same effect as `\![updatebymyself]`.<br />
Unlike `\![updatebymyself]`, `\![update,ghost+shell+balloon]` forces an update regardless of the SSP settings.<br />
When updating anything other than ghost, if an update is available, events such as the SHIORI event [OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md), in which OnUpdate is changed to OnUpdateOther, are sent. After all updates are complete, [OnUpdateResult](../../shiori-event/network-update/OnUpdateResult.md) occurs to summarize the results.<br />
Options are supported only by SSP. See [Update options](note-1.md#補足).

**対応:** SSP

## 記述例

```sakurascript
シェルの更新を実行。\![update,shell]
```
