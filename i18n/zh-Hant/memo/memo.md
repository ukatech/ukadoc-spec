# 備忘

## baseware 功能比較

| 功能一覽 | MATERIA | SSP | CROW | ninix-kagari |
| --- | --- | --- | --- | --- |
| 主控台 | ○ | × | × | △ |
| 校時 | ○ | ○ | ○ | × |
| headline sensor | ○ | ◎ | ○ | × |
| 郵件檢查 | ○ | ○ | ○ | × |
| plugin | ○ | ◎ | × | × |
| 本體更新 | × | △ | ○ | × |
| shell 倍率 | × | ○ | ○ | ○ |
| dressup | △ | ○ | × | △ |
| 日曆 | × | ○ | × | × |
| IM | × | ○ | × | × |
| 多重啟動 | △ | ◎ | ○ | ○ |
| ghost 自由移動 | × | ○ | × | × |
| 多個搭檔 | × | ○ | × | ○ |

SSP 的 headline sensor 也可使用 RSS。

SSP 的本體更新只有檢查功能。

有許多 SSP 專用 plugin。

MATERIA583 有錯誤，因此無法為搭檔進行 dressup。

MATERIA 若有多個執行檔，就能多重啟動。

SSP 可在單一處理程序中啟動多個角色。

## 推薦網站的橫幅

僅 MATERIA、SSP 可顯示。

將橫幅放進\*/ghost/master/banner/資料夾。

依照各 SHIORI 的格式，在 urllist 中

「網站名稱」 「URL」 「橫幅檔名（不含副檔名）」

依序填寫。

## 關於相容性的製作注意事項與備忘

- 在 MATERIA 中，郵件檢查、網路更新次數等從 0 開始計算。

  SSP、CROW 則從 1 開始。

  在 SSP 中，將 SHIORI Resource 的 useorigin1 設為 0，就會與 MATERIA 一樣使用零起算。

- 只有 MATERIA 的 surface 編號上限為 8192。

- 在 MATERIA、CROW 中，若 overlay 使用 pna，就無法正常呈現透明效果。

- MATERIA 的 surface 動畫等待時間最多只能識別到 10。

  若要設定更長的時間，請重複指定相同的動畫。

- 只有 SSP、CROW 能載入以 dft/dfp/dgt/dgp 加密的檔案。

- SSP 的動畫速度稍快（較流暢）。

- SSP 的 inputbox 可同時進行其他操作。

- SSP、CROW 的 balloon 也能使用半透明效果。

  但 inputbox 類型無法設為透明。

## SSP 專用功能

- 可處理下列影像格式。

  BMP/PNG/JPEG/GIF/MAG/XBM/PI/ICO/CUR

- 可使用 32bitPNG 顯示透明效果。

- 可安裝下列壓縮檔。

  CAB/自解壓縮

- surfacetable.txt (以顯示 surface 測試視窗取代)

  surfaces2.txt (可供 SSP 覆寫的 surfaces.txt)

  developer_options.txt (在 SSP 建立 updates2.dau 或 nar 時，用來指定排除檔案的文字檔)

- 可透過拖放 SSF 檔案播放對話。
