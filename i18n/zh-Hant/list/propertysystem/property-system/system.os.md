# system.os.(鍵)

**カテゴリ:** 屬性系統

執行中的 OS 資訊。(鍵)中填入的字串如下。

- **type**: OS 的種類。例如 Windows,MacOS,Darwin,Linux,Android,FreeBSD,ReactOS。若為網頁上的執行環境則為 "Web"。（由於歷史因素，值採用 TitleCase）
- **arch**: OS 的架構。例如 x86,x64,arm,arm64,ia64,risc-v,ppc,mips,loongarch。若無法確定或與架構無關則為 "unknown"
- **name**: OS 的名稱。例如：Windows 11 22H2
- **version**: OS 的核心版本。例如：10.0。請注意，可能與 OS 的名稱不一致。例如：Windows 10 和 11 都是 10.0。
- **build**: OS 的組建編號。例如：22621
- **parenttype**: 在相容 OS／相容層上執行時，其種類。若沒有則為空字串。目前為 Wine 或 ReactOS。
- **parentname**: 相容 OS／相容層的主機端（父端）OS 名稱。若沒有則為空字串。例如：Linux 5.19.0-23-generic
- **locale**: OS 的 UI 地區設定名稱。以「-」連接語言代碼與國家或地區代碼。例如：ja-JP（SSP 2.8.17 以後）
- **locale.language**: OS 的 UI 語言代碼（ISO 639）。例如：ja（SSP 2.8.17 以後）
- **locale.country**: OS 的 UI 國家或地區代碼（ISO 3166）。例如：JP（SSP 2.8.17 以後）
- **timezone.offset**: 目前時區相對於 UTC 的偏移量（以分鐘為單位）。在時間快於 UTC 的地區為負值。例如：日本標準時間為 -540（SSP 2.8.17 以後）
- **dst**: 目前套用日光節約時間時為 1，否則為 0。若透過 SSP 的「虛擬變更目前時間」（時光機）調整時間，則依調整後的日期時間回傳是否為日光節約時間。（SSP 2.8.17 以後）
- **uptime**: OS 啟動後的經過時間（秒）。（SSP 2.8.17 以後）
- **unixtime**: 目前時間的 UNIX 時間（自 1970-01-01 00:00:00 UTC 起經過的秒數）。若透過 SSP 的「虛擬變更目前時間」（時光機）調整時間，則回傳調整後的時間。（SSP 2.8.17 以後）
- **timeshift**: SSP 的「虛擬變更目前時間」（時光機）造成的目前時間偏移量（秒）。為有符號整數，向未來調整時為正，向過去調整時為負，未調整時為 0。（SSP 2.9.39 以後）
- **idletime**: 自最後一次使用者輸入（鍵盤或滑鼠操作）起經過的時間（秒）。（SSP 2.8.17 以後）

**対応:** SSP 2.6.26/27
