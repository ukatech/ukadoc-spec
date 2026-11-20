# balloon,balloon 名稱

**カテゴリ:** descript.txt

此 shell 的預設 balloon 名稱。使用者未明確切換 balloon 時，切換至此 shell 會自動切換至此 balloon。<br />
如果使用者已明確切換 balloon，則以使用者的選擇為優先。如果 ghost 端有 [recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md)（推薦 balloon），也以該設定為優先。<br />
也可寫在 ghost 端的 descript.txt 的 [balloon](../../ghost/recommended-balloon/balloon.md)（預設 balloon）中。若 shell 端有設定，則以 shell 端為優先；若沒有，則使用 ghost 端的值。<br />
僅依照預設值切換不算使用者明確切換。因此，切換至其他 shell 時，會再次依照該 shell 的定義切換。<br />
若指定多個，則使用第一個找到的 balloon（[default.balloon.path](default.balloon.path.md) 的指定優先）。

**既定値:** ghost 的 descript 設定

**対応:** SSP
