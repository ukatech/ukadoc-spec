# `\![wait,syncobject,同期オブジェクト名,オプション]`

**カテゴリ:** Wait commands

Wait until the specified named synchronization object (Mutex, Semaphore, Event, or WaitableTimer (since 2.8.28) on Windows) is signaled.<br />
A Mutex is released after waiting; a Semaphore is released once after waiting; an Event or WaitableTimer is not operated on after being acquired.

The following options can be specified.

- Numeric value or --timeout=numeric value……Timeout period. If omitted or set to 0, wait indefinitely (until the script is interrupted); if set to 1 or greater, wait for the specified number of milliseconds.
- --reset=0 or 1……Whether to release the mutex and semaphore immediately after waiting. 1 releases them (default); 0 does not.

**対応:** SSP
