# `\![reset,syncobject,同期オブジェクト名]`

**カテゴリ:** Wait commands

Set the specified named synchronization object to the non-signaled state (deactivate it).<br />
For an Event, ResetEvent sets it to the non-signaled state; for a WaitableTimer, CancelWaitableTimer does so.<br />
Reset has no effect on a Semaphore or Mutex and is ignored.

**対応:** SSP 2.8.28
