# system.os.(キー)

**カテゴリ:** プロパティシステム

目前執行中的 OS 資訊。可填入 (キー) 的字串如下。

- **type**: OS 類型，例如 Windows、MacOS、Darwin、Linux、Android、FreeBSD、ReactOS 等。若為 Web 上的執行階段，則為 "Web"。（因歷史原因，值採用 TitleCase）
- **arch**: OS 架構，例如 x86、x64、arm、arm64、ia64、risc-v、ppc、mips、loongarch 等。若無法確定或與架構無關，則為 "unknown"
- **name**: OS 名稱。例如：Windows 11 22H2
- **version**: OS 核心版本。例如：10.0。請注意，此值可能與 OS 名稱不一致。例如：Windows 10 和 11 的值都會是 10.0。
- **build**: OS 組建編號。例如：22621
- **parenttype**: 若在某種相容 OS／相容層上執行，則為其類型。若沒有則為空字串。目前為 Wine 或 ReactOS。
- **parentname**: 相容 OS／相容層的主機端（父層）OS 名稱。若沒有則為空字串。例如：Linux 5.19.0-23-generic
- **locale**: OS UI 地區設定名稱。由語言代碼與國家／地區代碼以「-」連接而成。例如：ja-JP（SSP 2.8.17 以後）
- **locale.language**: OS UI 語言代碼（ISO 639）。例如：ja（SSP 2.8.17 以後）
- **locale.country**: OS UI 國家／地區代碼（ISO 3166）。例如：JP（SSP 2.8.17 以後）
- **timezone.offset**: 目前時區相對於 UTC 的偏移量（以分鐘為單位）。相對於 UTC 較早的地區會是負值。例如：日本標準時間為 -540（SSP 2.8.17 以後）
- **dst**: 目前正在實施夏令時間時為 1，否則為 0。（SSP 2.8.17 以後）
- **uptime**: OS 啟動後經過的時間（秒）。（SSP 2.8.17 以後）
- **unixtime**: 目前時間的 UNIX 時間（自 1970-01-01 00:00:00 UTC 起經過的秒數）。（SSP 2.8.17 以後）
- **idletime**: 自上次使用者輸入（鍵盤、滑鼠操作）起經過的時間（秒）。（SSP 2.8.17 以後）

**対応:** SSP 2.6.26/27
