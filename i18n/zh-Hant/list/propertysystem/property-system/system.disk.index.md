# system.disk.index(ID).(キー)

**カテゴリ:** 屬性系統

第 ID 個（從 0 開始）的磁碟機資訊。ID 的範圍為 0 至 system.disk.count - 1。可填入 (キー) 的字串如下。

- **mountpoint**: Windows 上為磁碟機代號（不含末尾的「\\」），其他 OS 上則為掛載點。例如： C: /home
- **type**: 磁碟機種類，可能為 fixed（固定磁碟）、removable（可卸除式磁碟）、network（網路磁碟機）、optical（光碟機）、ram（RAM 磁碟）或 unknown（不明）。
- **total**: 磁碟機總容量（MB）。若無法取得容量（例如未插入媒體），則為 -1。
- **free**: 磁碟機可用容量（MB）。若無法取得容量（例如未插入媒體），則為 -1。

**対応:** SSP 2.8.17
