# uuid

**カテゴリ:** 屬性系統 \> 通用屬性名稱

目標的 UUID。SSP 依照 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 的步驟，僅以本機資訊計算，不會存取網路。

1. 選擇 `uuidvalue`。
   - 若有 metainfo 資料夾，則使用其 URL：descript.txt 的 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 值；若沒有，則使用從 [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) 推導出的 URL（預設分支視為 `master`）。
   - 若沒有，則使用 homeurl。解析方式與 `homeurl` 屬性相同（依序為 descript.txt、var.txt、SHIORI），不轉換 URL。
   - 若仍沒有，則使用名稱（`name`）。
2. 若 descript.txt 中有 [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md)，則將其內容附加至 `uuidvalue` 後方。
3. 將 `uuidvalue` 轉為 UTF-8（末尾不附加換行），計算 MD5，再將得到的二進位資料轉為 base64。

例如，從 `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` 產生的 UUID 為 `R5dVNluBvKjtQqjP0dAuoA==`。

由於不會讀取 metainfo 資料夾，因此不會反映 `jump_to.txt` 指定的搬遷或過去的 UUID。<br />
若 `uuidvalue` 為空（也沒有名稱），則取得失敗。

**対応:** SSP 2.9.35
