# `\![set,syncobject,同期オブジェクト名]`

**カテゴリ:** 等待命令

将指定名称的同步对象设为信号状态（激活）。<br />
Semaphore 使用 ReleaseSemaphore 加 1，Event 使用 SetEvent，WaitableTimer 则立即设为信号状态。<br />
对不属于当前线程的 Mutex 执行 set 没有意义，因此会被忽略。

**対応:** SSP 2.8.28
