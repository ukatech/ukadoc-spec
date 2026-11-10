# `\![update,更新対象(,オプション,オプション...)]`

**カテゴリ:** Event command

Starts a network update event for the specified update targets.<br />
ghost, shell, and balloon can be specified. To update multiple targets at once, separate them with "+".<br />
Setting the update target to all is equivalent to `\![updatebymyself]`.<br />
When `\![update,ghost+shell+balloon]` is specified, unlike `\![updatebymyself]`, the update is forced regardless of the SSP settings.<br />
When updating anything other than ghost, if an update is available, SHIORI events such as [OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md) are sent, along with the event group in which OnUpdate is changed to OnUpdateOther. After all updates are complete, [OnUpdateResult](../../shiori-event/network-update/OnUpdateResult.md) is sent as a summary of the results.<br />
Options are supported only by SSP. See [Specifying update options](note-1.md#補足).

**対応:** SSP

## 記述例

```sakurascript
シェルの更新を実行。\![update,shell]
```
