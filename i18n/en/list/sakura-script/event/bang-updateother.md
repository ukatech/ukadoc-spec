# `\![updateother,更新対象/オプション群,...]`

**カテゴリ:** Event command

Starts a network update event for update targets with arbitrary names. Targets that are not running can also be specified.<br />
Any number of the following options can be added.<br />
--balloon=balloon name<br />
--shell=shell name<br />
--plugin=plugin name<br />
--headline=headline name<br />
--language=language resource name<br />
If an update is available, SHIORI events such as [OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md) are sent, along with the event group in which OnUpdate is changed to OnUpdateOther. After all updates are complete, [OnUpdateResultEx](../../shiori-event/network-update/OnUpdateResultEx.md) is sent as a summary of the results.<br />
Options specified with --option= are supported only by SSP. See [Specifying update options](note-1.md#補足).

**対応:** SSP

## 記述例

```sakurascript
プラグイン「共有変数プラグイン」「うかてん」の更新を実行。\![updateother,--plugin=共有変数プラグイン,--plugin=うかてん]
```
