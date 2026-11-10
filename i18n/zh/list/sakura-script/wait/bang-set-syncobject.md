# `\![set,syncobject,同期オブジェクト名]`

**カテゴリ:** Wait commands

Set the specified named synchronization object to the signaled state (activate it).<br />
For a Semaphore, increment it by 1 with ReleaseSemaphore; for an Event, use SetEvent; for a WaitableTimer, set it to the signaled state immediately.<br />
Setting a Mutex that is not owned has no effect and is ignored.

**対応:** SSP 2.8.28
