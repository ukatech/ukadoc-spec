# balloon,balloon 名稱

**カテゴリ:** descript.txt

此 shell 的預設 balloon 名稱。切換至此 shell 時，此 balloon 會成為使用候選項目。<br />
切換目標 balloon 依下列順序決定，越上面的項目優先。

1. 若使用者在使用此 shell 期間曾切換 balloon，則使用該 balloon
2. ghost 側的 [recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md)（推薦 balloon）
3. 此 shell 的預設 balloon（本項目）
4. ghost 側的 [balloon](../../ghost/recommended-balloon/balloon.md)（預設 balloon）

若都未指定，切換 shell 時 balloon 不會改變。<br />
若依第 2～4 項決定的 balloon 與目前使用的 balloon 不同，則會切換至該 balloon。<br />
第 1 項的歷程會依各 shell 分別保留。除了透過選單等方式切換，使用 `\![change,balloon,...]` 切換也會記入歷程。僅依預設或推薦設定自動切換不會記入歷程，重新載入 balloon 或重設設定也不會新增歷程（重設設定會清除歷程）。<br />
若指定多個，則使用第一個找到的 balloon（[default.balloon.path](default.balloon.path.md) 的指定優先）。

**既定値:** ghost 的 descript 設定

**対応:** SSP
