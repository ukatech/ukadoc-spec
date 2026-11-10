# `\![wait,syncobject,同期オブジェクト名,オプション]`

**カテゴリ:** 等待指令

等待指定名稱的同步物件進入訊號狀態（在 Windows 上為 Mutex、Semaphore、Event、WaitableTimer（自 2.8.28 起））。<br />
等待 Mutex 後會將其釋放，等待 Semaphore 後會釋放 1，取得 Event 及 WaitableTimer 後則不會執行其他操作。

可指定以下選項。

- 數值或 --timeout=數值……逾時時間。省略或設為 0 時會無限等待（直到指令碼中斷）；指定 1 以上時，會等待指定的毫秒數。
- --reset=0 or 1……指定等待後是否釋放 mutex 和 semaphore。設為 1 時會釋放（預設值），設為 0 時不釋放。

**対応:** SSP
