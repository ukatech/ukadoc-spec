# サーフェス ID,名稱

**カテゴリ:** surfacetable.txt

為 surface ID 指定識別用名稱。<br />
通常記載於群組內。<br />
群組內第一個寫入的項目，會視為該群組的標準 surface（例如 scope,0 時為 0，scope,1 時為 10）。<br />
若名稱設為「\_\_parts」，表示該 surface 主要用作動畫或 dressup 等的零件（在 SSP 的サーフィステスト中會視為未指定名稱）。<br />
省略名稱即可明確表示名稱未定義。在 SSP 的サーフィステスト中，只有[特定 surface](../../shell-surfaces/surface-brace/caption_standarddef.md)會在未指定時套用初始值，因此可用此設定取消這些 surface 的指定。

**既定値:** 無作用／在 SSP 的サーフィステスト中，只有特定 surface 會套用[標準 surface 定義](../../shell-surfaces/surface-brace/caption_standarddef.md)。

**対応:** SSP
