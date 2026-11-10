# OnCrystalDiskInfoEvent

**カテゴリ:** plugin「CrystalDiskInfo Event PLUGIN」

ghost 啟動時已有資訊，或資訊更新時發生。

- **Reference0**: 所有磁碟的整體狀態（＝狀態最差者的資訊）與更新日期。<br />
  以逗號分隔，內容如下：「(Good|Caution|Bad|Unknown),YYYY,NN,DD,HH,MM,SS」。
- **Reference\***: 個別磁碟的狀態。<br />
  以逗號分隔，內容依序為電腦名稱、存在的磁碟、整體狀態、容量、攝氏溫度、溫度警告
