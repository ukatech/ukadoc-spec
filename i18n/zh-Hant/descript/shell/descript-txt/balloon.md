# balloon,balloon 名稱

**カテゴリ:** descript.txt

此 shell 的標準 balloon 名稱。切換至此 shell 時，此 balloon 是使用候選之一。<br />
切換後使用的 balloon 依下列順序決定，越上面的項目優先級越高。

1. 使用此 shell 期間，若使用者曾切換 balloon，則使用該 balloon
2. ghost 側的 [recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md)（推薦 balloon）
3. 此 shell 的標準 balloon（本項目）
4. ghost 側的 [balloon](../../ghost/recommended-balloon/balloon.md)（標準 balloon）

若以上皆未指定，切換 shell 時 balloon 不會改變。<br />
若依第 2〜4 項決定的 balloon 與目前使用的 balloon 不同，則會切換至該 balloon。<br />
第 1 項的紀錄會依各 shell 分別保留。除了透過選單等方式切換，透過 `\![change,balloon,...]` 切換也會留下紀錄。僅依標準或推薦設定自動切換不會留下紀錄，重新載入 balloon 或重設設定也不會新增紀錄（重設設定會清除紀錄）。<br />
若填寫多個，則使用第一個找到的 balloon（優先使用 [default.balloon.path](default.balloon.path.md) 的指定）。

**既定値:** ghost 的 descript 設定

**対応:** SSP
