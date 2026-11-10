# currentghost.seriko.sticky-window

**カテゴリ:** 屬性系統

目前[`\![set,sticky-window,～]`](../../sakura-script/surface/bang-set-sticky-window-ID-ID.md)的設定狀態。<br />
以逗號分隔群組內的 scope ID，並以分號分隔各群組。<br />
例如，若分別將 scope 0 和 1、scope 2 和 3 貼合，則會是 `0,1;2,3`。<br />
若沒有任何設定，則沒有值。<br />
*\[SET有效\]*

寫入時會以相同格式**完全取代目前的設定**。請注意，這與 Sakura Script 標籤逐一新增群組的方式不同。<br />
寫入空字串會解除所有貼合設定。<br />
元素少於 2 個的群組，以及包含已用於其他群組之 scope ID 的群組，都會被忽略。

**対応:** SSP 2.8.78
