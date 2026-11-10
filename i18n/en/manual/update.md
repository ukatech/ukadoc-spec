# Network Updates

For settings and other information related to network updates, see the page "[Support for Network Updates](../dev/update.md)".

The files related to network updates are arranged as follows.

- **For ghosts**:

  ```filetree
  +-(myghost)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt (SSPのみ)
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(SSP only) To support network updates for an additional shell**:

  ```filetree
  +-(myshell)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(SSP only) To support network updates for a balloon**:

  ```filetree
  +-(myballoon)
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-descript.txt
  　　+-balloons*s.txt
  　　+-balloonk*s.txt
  　　+-readme.txt
  　　+-balloons*.png
  　　+-balloonk*.png
  　　:
  　　:
  ```

  Plugins, headline sensors, and other similar items should also be placed in their respective folders.

- **updates2.dau**: A file listing the MD5 hashes of files targeted for updates, among other information.

  It is used during network updates to detect whether files have been corrupted or tampered with between the server and the files actually downloaded.

  It is usually generated using baseware features, for example, and does not need to be edited manually.

  For the creation procedure and other details, see the page "[Support for Network Updates](../dev/update.md)"

- **updates.txt**: Serves almost the same purpose as updates2.dau. Either one is sufficient (having both is also fine).

  Its format differs slightly, and it can avoid issues such as dau files being blocked from upload due to extension restrictions.

- **[delete.txt](../descript/install/delete.txt/index.md)**: A file for configuring file deletion.

  Place it on the server in the same location as updates2.dau.

  It is used to prevent files that are no longer needed from accumulating.

  For details such as its format, see the [linked page](../descript/install/delete.txt/index.md).

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: SSP only.

  Place it where you want to create updates2.dau (in the top-level directory).

  This file specifies files to exclude when creating updates2.dau (updates.txt) with SSP.

  It does not need to be uploaded to the server (for example, you can exclude the file itself), but it does no harm to leave it there, so use your discretion while considering situations such as users repackaging it as a nar.

  For details such as its format, see the [linked page](../descript/install/developer_options.txt/index.md).
