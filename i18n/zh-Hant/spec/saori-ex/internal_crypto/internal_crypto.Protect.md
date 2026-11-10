# Protect

**カテゴリ:** internal_crypto

使用作業系統的資料保護功能（Windows 的 DPAPI）封裝資料。只有相同電腦上的相同使用者（若為`--scope=machine`則是相同電腦上的所有使用者）才能透過 [Unprotect](internal_crypto.Unprotect.md) 還原封裝內容。<br />
此功能可讓儲存在存檔資料中的權杖等內容，即使被複製到其他電腦或其他使用者手上也無法讀取；但它並非用來區隔 ghost（以相同使用者身分執行的其他 ghost 或程式仍可還原）。

- **Argument1**: data（預設格式為`text`）
- **選項**: `--data-in=` / `--scope=user`（預設） / `--scope=machine`（其他值會回傳 400 `invalid parameter`） / `--out=`（預設為`base64`） / `--charset=`

**若將存檔資料移至其他電腦（例如共享 SSP 存檔資料、透過雲端儲存空間同步，或手動複製），或重新建立 Windows 使用者，將無法再使用 Unprotect**。腳本請將 Unprotect 失敗視為「要求使用者重新登入」等情況處理。

**対応:** SSP 2.9.13
