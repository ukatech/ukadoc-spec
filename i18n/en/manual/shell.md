# Shell

The files in a shell folder are as follows.

```filetree
+-(myghost)
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-readme.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-surfaces**.txt （SSPのみ）
　　　　　　+-alias.txt（旧仕様）
　　　　　　+-thumbnail.png
　　　　　　+-makoto.dll
　　　　　　+-surfacetable.txt (SSPのみ)
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
```

※For menu_background.png, menu_foreground.png, and menu_sidebar.png, see the “[Owner-draw menu](owner-draw-menu.md)” page.

- **[descript.txt](../descript/shell/index.md)**: A file for identifying the shell and configuring its basic settings.

  See the [linked page](../descript/shell/index.md) for details on what to include in the file.

- **readme.txt**: Used by the shell author to provide information such as the distribution source.

  This file is optional, but if provided, it can be viewed during installation or from the baseware menu.

  It is especially recommended when the ghost author and shell author are different.

- **surface\*.png**: Surface files.

  Images displayed on the desktop.

  There are no restrictions on image size or color depth.

  The file format is PNG[※](shell.md#シェル).

  Areas that match the color of the top-left pixel (coordinates 0,0) are treated as the transparent color (key color) and displayed as transparent.

  Although there is [a somewhat standard allocation](../descript/shell-surfaces/surface-brace/caption_standarddef.md) for surface numbers, they are basically unrestricted.

  However, surface0 and surface10 are required (recommended but not required for SSP).

  Therefore, even for a ghost with only one character, you need to provide an image filled with a single color as surface10.png, for example.

  If the baseware is MATERIA (embryo, the original Ukagaka), surface numbers can range from 0 to 8192.

  Other baseware has no such limit.

  In SSP 2.7.38 and later, specifying an animated GIF/APNG/animated WebP as surface\*.png will animate it without requiring a SERIKO definition.

- **surface\*.pna**: An alpha channel definition file for a surface.

  A grayscale PNG image (black: transparent ←→ opaque: white) renamed with the extension pna.

  Placing a pna file with the same number as the surface enables semi-transparency for that surface.

  | ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
  | --- | --- | --- | --- | --- |
  | surface0.png |  | surface0.pna |  | Desktop display |

  Areas that are not fully transparent will have hit detection.

  pna files are ignored in unsupported environments, such as Windows 9x or systems with very old graphics cards.

  In SSP, you can also use the PNG file's own alpha channel (transparency information) by changing the [setting](../descript/shell/descript-txt/seriko.use_self_alpha.md).

- **(element).png**: Under the [element](../descript/shell-surfaces/surface-brace/element-star.md) specification, PNG images[※](shell.md#シェル) with arbitrary names can be composited as parts and treated as a single surface. These are the images used for those parts.

  ※You may replace (element) with any name you like. Any number of images can be used, and they are not required.

  In SSP 2.7.38 and later, specifying an animated GIF/APNG/animated WebP in an element definition in surfaces.txt will animate it without requiring a SERIKO definition.

  See also “surfaces.txt” below for details.

- **(element).pna**: A pna file for each element image used in compositing.

- **[surfaces.txt](../descript/shell-surfaces/index.md)**: A file that defines surface ID assignments, layer compositing, animation, hit detection, and more.

  See [surfaces.txt](../descript/shell/index.md) for details on the definitions.

  For animation and dressup, see Animation.

- **[surfaces\*\*.txt](../descript/shell-surfaces/index.md)**: For SSP only.

  Any string can be used for \*\*.

  Support for names such as surfaces2.txt, introduced in the 2.01 series, and the ability to use arbitrary strings were added in 2.2.57 and later.

  Its functions are the same as those of `surfaces.txt`.

  This is for using SSP-specific features while maintaining compatibility.

  This file is optional. It is also fine to add only the necessary parts.

- **[alias.txt](../descript/shell-surfaces/surface-alias-brace/caption_aliastxt.md)**: Obsolete format. A text file for defining sakura(kero).alias braces.

  Its functionality has now been integrated into surfaces.txt.

- **thumbnail.png**: A thumbnail displayed when selecting a shell in the menu tree.

  Supported image formats are png and jpg.

  Renaming a png file to pnr makes areas matching the color of the top-left pixel (coordinates 0,0) transparent.

  This file is optional.

- **[makoto.dll](translator.md)**: Used for the translate function.

  The same file can be provided on the [ghost side](ghost.md). See the [linked page](translator.md) for details.

  This file is optional.

- **[surfacetable.txt](../descript/shell-surfacetable/index.md)**: For SSP only.

  A file defining surface contents for use with the “Surface Test” feature in the SSP development palette and other shell creation support utilities.

  See the [linked page](../descript/shell-surfacetable/index.md) for details.

  This file is optional.

!!! tip "Tip"

    - **[※1](shell.md#シェル),[※2](shell.md#シェル)**: SSP also supports encrypted PNG (DAP/DDP/DFP/DGP), non-animated GIF, JPEG, and BMP, but these are *deprecated*.

      They can be loaded for backward compatibility, but there is no guarantee that formats other than PNG will be supported for features and specifications added in the future.

      Also, transparency features (pna and [seriko.use_self_alpha](../descript/shell/descript-txt/seriko.use_self_alpha.md)) are currently unavailable for all formats other than PNG, and JPEG is prone to color shifts due to compression, making it unsuitable for use with transparent colors.
