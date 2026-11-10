# `\![set,syncobject,同期オブジェクト名]`

**カテゴリ:** Wait command

Sets the specified named synchronization object to the signaled state (activates it).<br />
For a Semaphore, this increments its count by 1 using ReleaseSemaphore; for an Event, it uses SetEvent; for a WaitableTimer, it signals it immediately.<br />
Setting a Mutex that is not owned has no effect and is ignored.

**対応:** SSP 2.8.28
