# `\![wait,syncobject,同期オブジェクト名,オプション]`

**カテゴリ:** Wait command

Waits until the specified named synchronization object (Mutex, Semaphore, Event, or WaitableTimer (since 2.8.28) on Windows) is signaled.<br />
A Mutex is released after waiting; a Semaphore is released once after waiting; an Event or WaitableTimer is left unchanged after being acquired.

The following options can be specified.

- Number or --timeout=number……Timeout duration. If omitted or set to 0, waits indefinitely (until the script is interrupted); if set to 1 or greater, waits for the specified number of milliseconds.
- --reset=0 or 1……Whether to release the mutex and semaphore immediately after waiting. 1 releases them (default); 0 does not release them.

**対応:** SSP
