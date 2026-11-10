# `\![wait,syncobject,同期オブジェクト名,オプション]`

**カテゴリ:** 等待命令

等待指定名称的同步对象变为信号状态（在 Windows 上为 Mutex、Semaphore、Event、WaitableTimer（从 2.8.28 起））。<br />
等待 Mutex 后会释放它，等待 Semaphore 后会释放 1 个资源，获取 Event 和 WaitableTimer 后则不执行其他操作。

可以指定以下选项。

- 数值或 --timeout=数值……超时时间。省略或设为 0 时无限等待（直到脚本中断）；指定 1 以上的数值时，等待指定的毫秒数。
- --reset=0 or 1……指定等待后是否释放 mutex 和 semaphore。设为 1 时释放（默认值），设为 0 时不释放。

**対応:** SSP
