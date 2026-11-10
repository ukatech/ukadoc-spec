# Overall structure

## Ghosts and shells

Ghost configuration files are placed in the ghost storage folder of the baseware (SSP, materia, etc.).

Every ghost must have exactly one master ghost and one master shell.

From the shell’s perspective, every shell must belong to exactly one ghost.

Therefore, the file structure of both is arranged so that the shell is contained within the ghost, as shown below.

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau
　　　　　　+-*.ico
　　　　　　+-*.cur
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-makoto.dll (必要な時のみ)
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
　　　　　　+-readme.txt (必要な時のみ)
　　　　　　+-thumbnail.png
　　　　　　+-surfaces**.txt (SSPのみ）
　　　　　　+-surfacetable.txt (必要な時のみ)(SSPのみ)
　　　　　　+-alias.txt (必要な時のみ)(旧仕様）
　　　　+-(additional_shell)
　　+-delete.txt (必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
　　+-developer_options.txt (必要な時のみ)(SSPのみ)
　　+-.narignore (必要な時のみ)(SSPのみ)
　　+-.updateignore (必要な時のみ)(SSPのみ)
　　+-.narinclude (必要な時のみ)(SSPのみ)
　　+-.updateinclude (必要な時のみ)(SSPのみ)
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-thumbnail.png
```

## Balloons

Balloons are managed centrally by each baseware, rather than separately for each ghost, and are shared by all ghosts.

Each balloon’s configuration files are placed under the baseware’s balloon storage folder as shown below.

```filetree
+-(myballoon)
　　+-descript.txt
　　+-balloons*s.txt
　　+-balloonk*s.txt
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-balloons*.png
　　+-balloonk*.png
　　+-balloons*.pna （MATERIA不可）
　　+-balloonk*.pna （MATERIA不可）
　　+-balloonc*.png
　　+-online*.png
　　+-sstp.png
　　+-arrow*.png
　　+-thumbnail.png
　　+-ok_down.png/ok_up.png （SSPのみ）
　　+-cancel_down.png/cancel_up.png （SSPのみ）
　　+-mode_down.png/mode_up.png （SSPのみ）
　　+-sstp_new.png （SSPのみ）
　　+-marker.png （SSPのみ）
　　+-delete.txt (SSPのみ・必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
```

- **(myghost)\\**: The home directory (root folder) of each ghost.

  Alphanumeric folder names are recommended.

- **(myghost)\\ghost\\**: The folder for files used internally by the ghost.

- **(myghost)\\ghost\\master\\**: The folder used by default for the ghost.

  Currently, only master is used (a remnant of the original design).

For details about the file structure within the ghost folder, see the “[Ghost](ghost.md)” page.

For details about makoto.dll, see the “[Translator](translator.md)” page.

- **(myghost)\\shell\\**: The folder that contains the ghost’s shell folders (groups of files for displaying graphics).

- **(myghost)\\shell\\master\\**: The folder for the default shell. Required.

- **(myghost)\\shell\\(additional_shell)\\**: The folder for an additional shell. The name is arbitrary (alphanumeric names are recommended). Its file structure is the same as master.

  Any number of these folders can exist. If present, they can be selected from owner-draw menus and other places.

For details about the file structure within the shell folder, see the “[Shell](shell.md)” page.

For details about menu_background.png, menu_foreground.png, and menu_sidebar.png, see the “[Owner-draw menu](owner-draw-menu.md)” page.

For details about makoto.dll, see the “[Translator](translator.md)” page.

- **(myghost)\\[delete.txt](../descript/install/delete.txt/index.md)**: File deletion settings file.

  See the [linked page](../descript/install/delete.txt/index.md) for details.

  Optional.

- **(myghost)\\[developer_options.txt](../descript/install/developer_options.txt/index.md)**: SSP-only settings file for NAR and update file creation features.

  See the [linked page](../descript/install/developer_options.txt/index.md) for details.

  Optional.

- **(myghost)\\readme.txt or readme.md**: The readme for the entire ghost.

  It is common to specify details such as the distributor and distribution source.

  You can use a character encoding other than Shift JIS by writing charset,UTF-8 on the first line or including a BOM.

  It is opened during installation and can also be opened from owner-draw menus and other places.

  Optional, but recommended.

  Instead of readme.txt, you can use readme.md. In that case, Markdown formatting is interpreted, and the file is displayed with formatting such as text sizes and tables.<br />
  Embedded images using `\![画像説明]`(画像パス) are also interpreted, but can only be used when the image path is relative, the file actually exists inside the ghost, and the image is in PNG or JPEG format.

- **(myghost)\\terms.txt or terms.md**: Displays the terms of use. A dialog displaying this content appears before a NAR/ZIP file is installed.

  Since installation is interrupted while the dialog is displayed, include this file only when absolutely necessary.

  As with the readme, you can use a character encoding other than Shift JIS by writing charset,UTF-8 on the first line or including a BOM.

  Optional, and *should be omitted if not needed*.

  terms.md can be used under the same conditions as readme.md.

- **(myghost)\\thumbnail.png**: The thumbnail displayed when selecting a ghost in the menu tree.

  Supported image formats are PNG and JPG.

  Renaming a PNG to PNR makes the pixel at the top-left of the image (coordinates 0,0) transparent, along with all pixels of the same color.

  Optional.

- **(myballoon)\\**: The home directory (root folder) of each balloon.

  Alphanumeric folder names are recommended.

For details about the file structure within the balloon folder, see the “[Balloon](balloon.md)” page.
