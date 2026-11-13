# uuid

**カテゴリ:** 屬性系統 \> 通用屬性名稱

對象的 UUID。SSP 依照 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 的程序，僅使用本機資訊計算，不會存取網路。

1. 選擇 `uuidvalue`。
   - 如果有 metainfo 資料夾，則使用其 URL。使用 descript.txt 的 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 值；若沒有，則使用從 [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) 推導出的 URL（預設分支視為 `master`）。
   - 若沒有，則使用 descript.txt 的 [homeurl](../../../../descript/ghost/descript-txt/homeurl.md)（不進行 URL 轉換）。與 `homeurl` 屬性不同，不使用從 var.txt 或 SHIORI 取得的值。這是為了不使用網路或其他行程，並確保值不會隨時間改變。
   - 若仍沒有，則使用名稱（`name`）。
2. 若 descript.txt 中有 [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md)，則將其內容附加在 `uuidvalue` 後面。
3. 將 `uuidvalue` 轉為 UTF-8（末尾不加入換行），計算 MD5，再將所得二進位資料轉為 base64。

例如，從 `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` 產生的 UUID 是 `R5dVNluBvKjtQqjP0dAuoA==`。

由於不會讀取 metainfo 資料夾，因此不會反映透過 `jump_to.txt` 指定的遷移位置或過去的 UUID。<br />
當 `uuidvalue` 為空（也沒有名稱）時，取得會失敗。

在 [ghostlist](../ghostlist.md)、[balloonlist](../balloonlist.md)、[activeghostlist](../activeghostlist.md) 的括號內，可以用此 UUID 代替名稱。也可用於指定 SSTP 的目標（[ReceiverGhostUUID](../../../../spec/sstp/req_res.md)、[IfGhost](../../../../spec/sstp/method_send.md)）。

接受 ghost、balloon、shell、plugin 名稱的 Sakura Script（`\![change,ghost,...]`、`\![call,ghost,...]`、`\![change,shell,...]`、`\![change,balloon,...]`、`\![raiseother,...]`、`\![notifyother,...]`、`\![raiseplugin,...]`、`\![notifyplugin,...]`、`\![timerraiseother,...]`、`\![timernotifyother,...]`、`\![timerraiseplugin,...]`、`\![timernotifyplugin,...]`）及啟動選項 `--ghost`，也可以用 UUID 代替名稱。當名稱等項目不匹配時，只會比對符合 UUID 格式（22 個 base64 字元加上 `==`）的值。

在屬性系統中，除了 `ghostlist`、`balloonlist`、`activeghostlist`、`pluginlist`，也可以寫在 `history.ghost`、`history.balloon`、`history.plugin` 和 `rateofuselist` 的括號內。歷史紀錄與使用統計在內部是以名稱或路徑記錄，並非以 UUID 記錄（儲存格式不變）。以 UUID 查詢時，會先對應至已安裝的 ghost 等項目，再查詢其紀錄。

ghost 的 descript.txt 中的 `balloon`、`recommended.balloon`，以及 balloon 的 descript.txt 中的 `recommended.ghost`，也可以用 UUID 代替名稱。

plugin 同時具有 descript.txt 的 `id`（由 plugin 自行決定的 GUID，仍如以往作為 ID 進行比對）和此 `uuid`。兩者不同，`id` 不會被 `uuid` 取代。

**対応:** SSP 2.9.35
