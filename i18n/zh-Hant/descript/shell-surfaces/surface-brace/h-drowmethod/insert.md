# insert,ID

**カテゴリ:** surface brace \> drawing method

將指定 ID（animation\* 中 \* 的編號）的 dressup 群組（interval 為 bind 的動畫）插入該位置。<br />
這是為 dressup 設計的方法，將其用於非 dressup 動畫或元素時，行為未定義。<br />
例如，當某個 dressup A 與其他 dressup B 的位置關係結構為部分在前、部分在後時，透過使用 insert 將 dressup B 插入 dressup A 後方部分的影格與前方部分的影格之間，即可自然呈現前後關係。此時，無論 dressup B 處於顯示或隱藏狀態，都能維持顯示的完整性。<br />
也可以在 insert 目標中執行 insert（巢狀插入）。<br />
不過，這*僅是預先安排 dressup A 與 B 的顯示順序*，並不會強制顯示 dressup B。<br />
是否實際顯示 dressup B，取決於 dressup B 的啟用／停用狀態。

**対応:** Materia / SSP
