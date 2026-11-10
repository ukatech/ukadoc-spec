# Shell

The files in the shell folder are as follows.

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

※For menu_background.png, menu_foreground.png, and menu_sidebar.png, see the page 「[Owner Draw Menu](owner-draw-menu.md)」.

- **[descript.txt](../descript/shell/index.md)**: A file for identifying the shell and configuring basic settings.

  For the contents of the text file, see the [linked page](../descript/shell/index.md).

- **readme.txt**: Used by the shell creator to provide information such as the distribution source.

  This file is optional, but if provided, it can be referenced during installation and from the baseware menu.

  It is particularly advisable to provide one when the ghost creator and shell creator are different.

- **surface\*.png**: Surface files.

  Images displayed on the desktop.

  There are no restrictions on image size or color depth.

  The file format is PNG[※](shell.md#シェル).

  Areas with the same color as the top-left pixel (coordinates 0,0) are treated as the transparent color (key color) and displayed as transparent.

  Although there is a [somewhat standard assignment](../descript/shell-surfaces/surface-brace/caption_standarddef.md) for surface numbers, they are basically unrestricted.

  However, surface0 and surface10 are required (recommended but not required for SSP).

  Therefore, even for a ghost with only one character, you need to provide an image filled with a single color as surface10.png, for example.

  If the baseware is MATERIA (embryo, the original 伺か), surface numbers can range from 0 to 8192.

  Other baseware has no restrictions.

  In SSP 2.7.38 and later, specifying an animated GIF/APNG/animated WebP as surface\*.png will animate it without requiring a SERIKO definition.

- **surface\*.pna**: Surface alpha channel definition files.

  These are grayscale PNG images (black: transparent ←→ opaque: white) renamed with the pna extension.

  Placing a pna file with the same number as the surface enables the surface to be made translucent.

  | ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
  | --- | --- | --- | --- | --- |
  | surface0.png |  | surface0.pna |  | Desktop display |

  Areas that are not fully transparent will have hit detection.

  In unsupported environments, such as Windows9x and very old graphics cards, pna files are ignored.

  In SSP, you can also configure it to use the PNG's own alpha channel (transparency information) through the [setting](../descript/shell/descript-txt/seriko.use_self_alpha.md).

- **(element).png**: The [element](../descript/shell-surfaces/surface-brace/element-star.md) specification allows PNG images[※](shell.md#シェル) with arbitrary names to be composited as parts and treated as a single surface. These are the images used for those parts.

  ※You can replace (element) with any name you like. Any number of images can be used, and they are not required.

  In SSP 2.7.38 and later, specifying an animated GIF/APNG/animated WebP in an element definition in surfaces.txt will animate it without requiring a SERIKO definition.

  See also 「surfaces.txt」 below for details.

- **(element).pna**: A pna file for each element composite part image.

- **[surfaces.txt](../descript/shell-surfaces/index.md)**: A file defining surface ID assignments, layer composition, animation, hit detection, and other properties.

  For the definitions, see [surfaces.txt](../descript/shell/index.md).

  For animation and dressup, see Animation.

- **[surfaces\*\*.txt](../descript/shell-surfaces/index.md)**: For SSP only.

  Any string can be used in place of \*\*.

  Support for the name surfaces2.txt in the 2.01 series and later, allowing arbitrary strings to be appended, was introduced in 2.2.57 and later.

  Its functionality is the same as `surfaces.txt`.

  This file is for using SSP-specific features while maintaining compatibility.

  This file is optional. It is also fine to add only the necessary parts.

- **[alias.txt](../descript/shell-surfaces/surface-alias-brace/caption_aliastxt.md)**: Legacy specification. A text file for describing sakura(kero).alias braces.

  Its functionality has now been integrated into surfaces.txt.

- **thumbnail.png**: A thumbnail displayed when selecting a shell in the menu tree.

  Supported image formats are png and jpg.

  Renaming a png file to pnr makes areas with the same color as the top-left pixel (coordinates 0,0) transparent.

  This file is optional.

- **[makoto.dll](translator.md)**: Used for the translate feature.

  It can be provided on the [ghost side](ghost.md) as well. See the [linked page](translator.md) for details.

  This file is optional.

- **[surfacetable.txt](../descript/shell-surfacetable/index.md)**: For SSP only.

  A file defining surface contents, intended for use with the “Surface Test” feature in the SSP development palette and other shell creation support utilities.

  See the [linked page](../descript/shell-surfacetable/index.md) for details.

  This file is optional.

!!! tip "Tip"

    - **[※1](shell.md#シェル),[※2](shell.md#シェル)**: SSP can also use encrypted PNG (DAP/DDP/DFP/DGP), GIF (non-animated), JPEG, and BMP, but these formats are *deprecated*.

      They can be loaded for backward compatibility, but there is no guarantee that formats other than PNG will be supported in features and specifications added in the future.

      Also, even now, transparency features (pna and [seriko.use_self_alpha](../descript/shell/descript-txt/seriko.use_self_alpha.md)) are unavailable for all formats except PNG, and JPEG has the additional drawback of being prone to color shifts due to compression, making it unsuitable for use with transparent colors.
