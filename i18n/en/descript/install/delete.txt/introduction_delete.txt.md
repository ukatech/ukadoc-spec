# delete.txt

## Overview

See also the [File structure: “Network Updates”](../../../manual/update.md) page.

When updating, the client's (user's) files are only overwritten by the server's (author's) files; they are not synchronized.<br />
In other words, files once downloaded or created on the client cannot be removed even if they are deleted on the server.<br />
Therefore, if a file that was published needs to be removed after release, it must be listed in delete.txt.<br />
Note that delete.txt is not automatically deleted after the deletion is performed; once listed, its contents will continue to be excluded indefinitely unless changed.

The following specification applies to SSP only.

- **charset,(character encoding)**: Specify the file's character encoding

## 記述例

```
ghost\master\ai.dtx
ghost\master\testdict\
shell\master\surface110.png
```
