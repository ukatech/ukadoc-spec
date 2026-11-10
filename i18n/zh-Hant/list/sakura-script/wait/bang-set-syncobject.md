# `\![set,syncobject,同期オブジェクト名]`

**カテゴリ:** Wait command

Set the specified named synchronization object to the signaled state (activate it).<br />
For Semaphore, increment it by 1 with ReleaseSemaphore; set Event with SetEvent; set WaitableTimer to the signaled state immediately.<br />
Setting a Mutex that is not owned has no effect, so it is ignored.

**対応:** SSP 2.8.28
