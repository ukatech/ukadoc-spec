# `\![reset,syncobject,同期オブジェクト名]`

**カテゴリ:** Wait command

Set the specified named synchronization object to the non-signaled state (deactivate it).<br />
For Event, use ResetEvent; for WaitableTimer, use CancelWaitableTimer to set it to the non-signaled state.<br />
Reset has no effect on Semaphore or Mutex, so it is ignored.

**対応:** SSP 2.8.28
