# system.disk.index(ID).(key)

**カテゴリ:** Property system

Information about the drive at index ID (0-based). The range of ID is 0 to system.disk.count - 1. The strings that can be used for (key) are as follows.

- **mountpoint**: On Windows, the drive letter (excluding the trailing "\\"); on other operating systems, the mount point. Example: C: /home
- **type**: The drive type. One of fixed (fixed disk), removable (removable disk), network (network drive), optical (optical drive), ram (RAM disk), or unknown.
- **total**: The total drive capacity (MB). If the capacity cannot be retrieved (e.g. no media inserted), the value is -1.
- **free**: The available drive capacity (MB). If the capacity cannot be retrieved (e.g. no media inserted), the value is -1.

**対応:** SSP 2.8.17
