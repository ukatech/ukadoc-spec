# `\![reset,syncobject,同期オブジェクト名]`

**カテゴリ:** Wait command

Sets the specified named synchronization object to the nonsignaled state (deactivates it).<br />
For an Event, this uses ResetEvent; for a WaitableTimer, it uses CancelWaitableTimer to set it to the nonsignaled state.<br />
Reset operations on Semaphores and Mutexes have no effect and are ignored.

**対応:** SSP 2.8.28
