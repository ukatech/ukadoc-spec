# Ghost

The files in the master ghost folder are as follows.

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-(saori).dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau （旧仕様）
　　　　　　+-updates.txt （旧仕様）
　　　　　　+-*.ico
　　　　　　+-*.cur
　　　　　　+-thumbnail.png
　　　　　　+-ai0.png
　　　　　　+-ai0_dark.png
```

- **[descript.txt](../descript/ghost/index.md)**: A file used to identify the ghost.

  Without it, the baseware will not recognize the ghost.

  See the [linked page](../descript/ghost/index.md) for details, including the contents of the text file.

- **[updates2.dau](update.md)**

- **[updates.txt](update.md)**: A file containing update information.

  Placing it here is an old specification; generally, it only needs to be in the root (directly under (myghost)).

  See the [linked page](update.md) for details.

- **shiori.dll**: The core of the ghost. Almost essential.

  Many general-purpose SHIORI implementations are available and are normally used.

  It receives [SHIORI Event](../list/shiori-event/index.md) messages ([additional explanation](../memo/shiori-event.md)) from the baseware (such as SSP), constructs [Sakura Script](../list/sakura-script/index.md) instructions for the ghost, and returns them to the baseware.

  How to create the core parts of a ghost, including how to write its dialogue, differs entirely depending on the SHIORI, so refer to the documentation for the SHIORI.

- **(saori).dll**: A module that extends SHIORI functionality.

  Generally placed in the same directory as shiori.dll.

  However, a relative path can also be specified when calling it from SHIORI.

  Usage depends on the SHIORI, so refer to the documentation for the SHIORI.

  This file is optional.

- **[makoto.dll](translator.md)**: A DLL for translation.

  See the [linked page](translator.md) for details. It can also be placed on the [shell side](shell.md).

  This file is optional.

- **\*.ico**: An icon file.

  32×32 and 16×16 sizes can be used.

  It is displayed when the ghost is minimized to an icon and in the ghost explorer, among other places.

  This file is optional. If omitted, the default icon is used.

- **\*.cur**: A cursor file.

  The cursor changes to the specified cursor when it is over the ghost.

  This file is optional. If omitted, the normal cursor remains in use.

- **thumbnail.png**: A thumbnail displayed when the ghost is selected in the menu tree.

  The supported image formats are png and jpg.

  If png is renamed to pnr, the color of the top-left pixel (coordinates 0,0) is made transparent.

  This file is optional.

- **ai0.png / ai0_dark.png**: See the [AI graph explanation](../descript/shell/descript-txt/shiori.logo.file.md).

  This file is optional.

In addition, SHIORI implementations and similar components commonly have several files outside the dll, such as string resource files called "dictionaries" (in fact, ghost creators often primarily edit these files).<br />
For details about these files, refer to the documentation for the SHIORI in use.
