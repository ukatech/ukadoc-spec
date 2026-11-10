# OnCrystalDiskInfoEvent

**カテゴリ:** Plugin “CrystalDiskInfo Event PLUGIN”

Occurs when information is available at ghost startup or when information is updated.

- **Reference0**: The status of all disks (that is, the status of the worst one) and the update date.<br />
  Comma-separated, in the format “(Good|Caution|Bad|Unknown),YYYY,NN,DD,HH,MM,SS”.
- **Reference\***: Individual disk status.<br />
  Comma-separated: machine name, existing disk, overall status, capacity, temperature in Celsius, temperature warning
