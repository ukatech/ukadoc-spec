# `\![reset,syncobject,同期オブジェクト名]`

**カテゴリ:** 等待命令

将指定名称的同步对象设为非信号状态（停用）。<br />
Event 使用 ResetEvent，WaitableTimer 使用 CancelWaitableTimer 设为非信号状态。<br />
对 Semaphore 和 Mutex 执行 reset 没有意义，因此会被忽略。

**対応:** SSP 2.8.28
