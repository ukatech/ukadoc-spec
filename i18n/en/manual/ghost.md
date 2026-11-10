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

  Without this file, the ghost will not be recognized by the baseware.

  For details such as the contents of the text file, see the [linked page](../descript/ghost/index.md).

- **[updates2.dau](update.md)**

- **[updates.txt](update.md)**: A file containing update information.

  This is the old format at this location, and it generally only needs to be in the root folder (directly under (myghost)).

  For details, see the [linked page](update.md).

- **shiori.dll**: The ghost's core. Almost essential.

  Many general-purpose SHIORI implementations are available, so one is normally used.

  It receives [SHIORI Event](../list/shiori-event/index.md) ([supplementary explanation](../memo/shiori-event.md)) sent from the baseware (such as SSP), builds [Sakura Script](../list/sakura-script/index.md), which instructs the ghost's behavior, and returns it to the baseware.

  The way to create the core parts of a ghost, such as writing actual dialogue, differs entirely depending on the SHIORI, so refer to the documentation for each SHIORI.

- **(saori).dll**: A module that extends SHIORI functionality.

  It is generally placed in the same directory as shiori.dll.

  However, a relative path can also be specified when calling it from SHIORI.

  The procedure for using it depends on the SHIORI, so refer to the SHIORI documentation.

  This file is optional.

- **[makoto.dll](translator.md)**: A DLL for translation.

  For details, see the [linked page](translator.md). It can also be placed on the [shell side](shell.md).

  This file is optional.

- **\*.ico**: Icon files.

  32×32 and 16×16 icons can be used.

  They are displayed when minimized to an icon, in the ghost explorer, and elsewhere.

  This file is optional. If omitted, the default icon is used.

- **\*.cur**: Cursor files.

  The cursor changes to the specified cursor when it is over the ghost.

  This file is optional. If omitted, the cursor remains unchanged.

- **thumbnail.png**: A thumbnail displayed when selecting a ghost in the menu tree.

  The supported image formats are PNG and JPG.

  Renaming a PNG file to PNR makes pixels matching the color of the top-left pixel (coordinates 0,0) transparent.

  This file is optional.

- **ai0.png / ai0_dark.png**: See the [AI graph description](../descript/ghost/descript-txt/shiori.logo.file.md).

  This file is optional.

In addition to these, SHIORI (and other components) generally includes several files outside the DLL, such as text resource files called "dictionaries" (in fact, ghost authors often primarily edit these files).<br />
For details about these files, refer to the documentation for each SHIORI you use.
