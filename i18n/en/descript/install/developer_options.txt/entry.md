# Relative path,option 1,option 2,...

**カテゴリ:** developer_options.txt

Specify options, separated by commas, for files and folders given as paths relative to the ghost's home folder.<br />
Separate levels in a relative path with “/”, not “\\”.<br />
When specifying a folder, append a / to the path.<br />
The wildcards \* and ? can be used (since SSP 2.5.17)<br />
The available options are as follows.

- **nonar**: Do not include the target in the nar when creating a nar.
- **noupdate**: Do not include the target in updates when creating updates2.dau (updates.txt).

<br />
Note that these options control file creation, so they are effective only *when creating a nar or update files using SSP or an application that can recognize this file*.

**既定値:** No behavior

**対応:** SSP
