# `\![updateother,更新対象/オプション群,...]`

**カテゴリ:** 事件命令

启动针对任意名称的更新目标的网络更新事件。也可以指定未启动的目标。<br />
以下指定可以添加任意数量。<br />
--balloon=气球名称<br />
--shell=壳名称<br />
--plugin=插件名称<br />
--headline=标题名称<br />
--language=语言资源名称<br />
如果有更新，将通知 SHIORI 事件[OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md)等将 OnUpdate 改为 OnUpdateOther 的事件群，全部更新结束后会触发[OnUpdateResultEx](../../shiori-event/network-update/OnUpdateResultEx.md)以汇总结果。<br />
只能在 SSP 中通过 --option=指定选项。请参阅[更新选项指定](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
プラグイン「共有変数プラグイン」「うかてん」の更新を実行。\![updateother,--plugin=共有変数プラグイン,--plugin=うかてん]
```
