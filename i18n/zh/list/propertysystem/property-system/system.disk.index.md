# system.disk.index(ID).(キー)

**カテゴリ:** プロパティシステム

第 ID 个（从 0 开始）驱动器的信息。ID 的范围为 0 到 system.disk.count - 1。(キー) 可填入以下字符串。

- **mountpoint**: Windows 上为驱动器号（去掉末尾的「\\」），其他 OS 上为挂载点。例： C: /home
- **type**: 驱动器类型，可为 fixed（固定磁盘）、removable（可移动磁盘）、network（网络驱动器）、optical（光驱）、ram（RAM 磁盘）或 unknown（未知）。
- **total**: 驱动器总容量（MB）。无法获取容量时（例如未插入媒体）为 -1。
- **free**: 驱动器可用容量（MB）。无法获取容量时（例如未插入媒体）为 -1。

**対応:** SSP 2.8.17
