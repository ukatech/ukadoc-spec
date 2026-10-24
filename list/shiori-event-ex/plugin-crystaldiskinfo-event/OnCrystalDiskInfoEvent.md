# OnCrystalDiskInfoEvent

**カテゴリ:** プラグイン「CrystalDiskInfo Event PLUGIN」

ゴースト起動時に情報がある場合/情報が更新されたに発生。

- **Reference0**: ディスク群全体のステータス（＝最も悪いものの情報）と、更新日付。<br />
  カンマ区切りで、「(Good|Caution|Bad|Unknown),YYYY,NN,DD,HH,MM,SS」のように入る。
- **Reference\***: ディスク個別ステータス。<br />
  カンマ区切りで、マシン名,存在するディスク,全体のステータス,容量,摂氏温度,温度警告
