# `\![set,syncobject,同期オブジェクト名]`

**カテゴリ:** 等待指令

將指定名稱的同步物件設為訊號狀態（啟用）。<br />
Semaphore 會透過 ReleaseSemaphore 加 1，Event 會透過 SetEvent，WaitableTimer 則會立即設為訊號狀態。<br />
對未持有的 Mutex 執行 set 沒有意義，因此會忽略。

**対応:** SSP 2.8.28
