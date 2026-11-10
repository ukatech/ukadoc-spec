# `\![wait,syncobject,同期オブジェクト名,オプション]`

**カテゴリ:** Wait command

Wait until the specified named synchronization object (Mutex, Semaphore, Event, or WaitableTimer (from 2.8.28) on Windows) enters the signaled state.<br />
Mutex is released after waiting, Semaphore is released once after waiting, and Event and WaitableTimer are not operated on after being acquired.

The following options can be specified.

- Number or --timeout=number……Timeout duration. If omitted or set to 0, wait indefinitely (until the script is broken); if set to 1 or greater, wait for the specified number of milliseconds.
- --reset=0 or 1……Whether to release the mutex and semaphore immediately after waiting. 1 releases them (default); 0 does not.

**対応:** SSP
