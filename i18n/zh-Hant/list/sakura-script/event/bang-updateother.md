# `\![updateother,更新対象/オプション群,...]`

**カテゴリ:** 事件指令

開始任意名稱之更新對象的網路更新事件。也可以指定未執行中的對象。<br />
以下項目可任意新增多個。<br />
--balloon=balloon 名稱<br />
--shell=shell 名稱<br />
--plugin=plugin 名稱<br />
--headline=標題名稱<br />
--language=語言資源名稱<br />
若有更新，會通知 SHIORI 事件 [OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md) 等將 OnUpdate 改為 OnUpdateOther 的事件；全部更新完成後，會觸發 [OnUpdateResultEx](../../shiori-event/network-update/OnUpdateResultEx.md) 彙整結果。<br />
只有 SSP 支援使用 --option= 指定選項。請參閱[更新選項設定](note-1.md#補足)。

**対応:** SSP

## 記述例

```sakurascript
プラグイン「共有変数プラグイン」「うかてん」の更新を実行。\![updateother,--plugin=共有変数プラグイン,--plugin=うかてん]
```
