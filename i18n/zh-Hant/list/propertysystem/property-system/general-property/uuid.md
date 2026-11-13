# uuid

**カテゴリ:** 屬性系統 \> 通用屬性名稱

目標的 UUID。SSP 依照 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 的程序，僅根據本機資訊計算。不會存取網路。

1. 選擇 `uuidvalue`。
   - 如果有 metainfo 資料夾，則使用其 URL。使用 descript.txt 的 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 值；若沒有，則使用從 [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) 推導出的 URL（預設分支視為 `master`）。
   - 若沒有，則使用 descript.txt 的 [homeurl](../../../../descript/ghost/descript-txt/homeurl.md)（不轉換 URL）。與 `homeurl` 屬性不同，此處不使用從 var.txt 或 SHIORI 取得的值，目的是不使用網路或其他程序，並確保值不會隨時間改變。
   - 若連此項也沒有，則使用名稱（`name`）。
2. 如果 descript.txt 中有 [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md)，將其內容附加至 `uuidvalue` 後面。
3. 將 `uuidvalue` 轉為 UTF-8（不在結尾加入換行），計算 MD5，再將所得的二進位資料轉為 base64。

例如，從 `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` 產生的 UUID 為 `R5dVNluBvKjtQqjP0dAuoA==`。

由於不會讀取 metainfo 資料夾，因此不會反映透過 `jump_to.txt` 進行的移轉或過去的 UUID。<br />
當 `uuidvalue` 為空（也沒有名稱）時，取得會失敗。

**対応:** SSP 2.9.35
