# developer_options.txt

## Overview

See also the pages [File structure: “Network updates”](../../../manual/update.md) and [File structure: “Installation”](../../../manual/install.md).

This file sets options for files targeted when SSP creates archives or network update information files.<br />
SSP can create archives (.nar) or update files (updates2.dau) by dragging and dropping a package folder, such as a ghost, onto SSP; this file is referenced when that feature runs.<br />
Therefore, as a rule, note that this file is *completely unrelated* if you create those files with other tools, such as “Sodate” or “ghost distribution automation systems.”<br />
As an exception, some tools, such as “Satorist,” implement features that read and use developer_options.txt.

## 記述例

```
ghost/master/savedata.txt,noupdate
shell/old/,nonar
ghost/master/profile/,nonar,noupdate
```

## Notes

Be aware that settings must be made *on one line per target (file or folder)*. For example, if you write the following, *only the setting made later (below) takes effect, and the nonar option is disabled*.

```
ghost/master/profile/,nonar
ghost/master/profile/,noupdate
```

To specify two options, the correct format is as shown above:

```
ghost/master/profile/,nonar,noupdate
```

Write it this way.
