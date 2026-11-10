# system.disk.index(ID).(key)

**カテゴリ:** Property System

Information about the drive at index ID (zero-based). The ID range is from 0 to system.disk.count - 1. The strings that can be used for (key) are as follows.

- **mountpoint**: On Windows, the drive letter (without the trailing "\\"); on other OSes, the mount point. Example: C: /home
- **type**: Drive type: fixed (fixed disk), removable (removable disk), network (network drive), optical (optical drive), ram (RAM disk), or unknown.
- **total**: Total drive capacity (MB). Returns -1 if the capacity cannot be retrieved (for example, no media is inserted).
- **free**: Free drive capacity (MB). Returns -1 if the capacity cannot be retrieved (for example, no media is inserted).

**対応:** SSP 2.8.17
