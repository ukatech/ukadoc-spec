# `\![reset,syncobject,同期オブジェクト名]`

**カテゴリ:** 等待指令

將指定名稱的同步物件設為非訊號狀態（停用）。<br />
Event 會透過 ResetEvent、WaitableTimer 會透過 CancelWaitableTimer 設為非訊號狀態。<br />
對 Semaphore 及 Mutex 執行 reset 沒有意義，因此會忽略。

**対応:** SSP 2.8.28
