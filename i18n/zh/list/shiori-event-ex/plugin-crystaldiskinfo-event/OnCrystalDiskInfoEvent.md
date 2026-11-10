# OnCrystalDiskInfoEvent

**カテゴリ:** 插件“CrystalDiskInfo Event PLUGIN”

ghost启动时有信息/信息更新时触发。

- **Reference0**: 整组磁盘的状态（＝状态最差的磁盘信息）和更新日期。<br />
  以逗号分隔，格式类似“(Good|Caution|Bad|Unknown),YYYY,NN,DD,HH,MM,SS”。
- **Reference\***: 各个磁盘的状态。<br />
  以逗号分隔，依次为计算机名、存在的磁盘、整体状态、容量、摄氏温度、温度警告
