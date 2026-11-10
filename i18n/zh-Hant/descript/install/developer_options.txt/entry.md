# Relative path,option 1,option 2,...

**カテゴリ:** developer_options.txt

Specify comma-separated options for files and folders using paths relative to the ghost's home folder.<br />
Separate path levels with "/" rather than "\\".<br />
To specify a folder, add / at the end.<br />
You can use \* and ? as wildcards (since SSP 2.5.17).<br />
The options are as follows.

- **nonar**: Excludes the item from the nar when creating a nar.
- **noupdate**: Excludes the item from updates when creating updates2.dau (updates.txt).

<br />
Note that these options control file creation, so they are effective *only when creating nar or update files using SSP or an application that can recognize this file*.

**既定値:** No behavior

**対応:** SSP
