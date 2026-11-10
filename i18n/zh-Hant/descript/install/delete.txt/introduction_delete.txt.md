# delete.txt

## Overview

See also the [File structure: "Network updates"](../../../manual/update.md) page.

During updates, client (user) files are only overwritten by files from the server (author); they are not synchronized.<br />
In other words, files once downloaded or created on the client cannot be removed even if they are deleted from the server.<br />
Therefore, if you need to delete a file that has already been published, you must list it in delete.txt.<br />
Note that delete.txt is not automatically deleted after the deletion is performed, and its entries will continue to be excluded indefinitely unless changed.

The following specification applies to SSP only.

- **charset,(character encoding)**: Specifies the file's character encoding

## 記述例

```
ghost\master\ai.dtx
ghost\master\testdict\
shell\master\surface110.png
```
