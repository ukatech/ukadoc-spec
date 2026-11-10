# OnCrystalDiskInfoEvent

**カテゴリ:** Plugin "CrystalDiskInfo Event PLUGIN"

Triggered when information is available or updated at ghost startup.

- **Reference0**: The status of all disks (that is, information for the worst one) and the update date.<br />
  It is comma-separated and takes the form "(Good|Caution|Bad|Unknown),YYYY,NN,DD,HH,MM,SS".
- **Reference\***: Individual disk status.<br />
  Comma-separated values: machine name, existing disk, overall status, capacity, temperature in Celsius, temperature warning
