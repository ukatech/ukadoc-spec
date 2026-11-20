# Configuring the owner draw menu

This page explains how to configure the appearance of the owner draw menu (right-click menu).

See also [Owner draw menu](../manual/owner-draw-menu.md) in the file structure documentation.

Settings are specified in the shell's `descript.txt` or in responses to SHIORI Events issued to retrieve resources.

## 目次

1. [Configuring in the shell's descript.txt](ownerdraw.md#シェルのdescripttxtで設定する)
2. [Configuring with SHIORI Events](ownerdraw.md#shiori-eventで設定する)

## Configuring in the shell's descript.txt

The shell's `descript.txt` can specify three images used for the normal background, selected background, and sidebar, as well as text colors.

SSP also supports specifying the text size and font.

The layout of dressup menu items is also configured in the shell's `descript.txt`. See [Configuring dressup](bind.md) for details.

Note that if the same item is also configured using a SHIORI Event, the SHIORI Event setting takes precedence.

In SSP, the same items can also be specified in the ghost's `descript.txt` (`ghost/master/descript.txt`). If the same item is also present in the shell's `descript.txt`, the shell's setting takes precedence.

The following is an example of settings in `descript.txt`.

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png

menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom

menu.background.font.color.r,0
menu.background.font.color.g,0
menu.background.font.color.b,0
menu.foreground.font.color.r,0
menu.foreground.font.color.g,0
menu.foreground.font.color.b,255
menu.separator.color.r,0
menu.separator.color.g,0
menu.separator.color.b,0
menu.disable.font.color.r,120
menu.disable.font.color.g,120
menu.disable.font.color.b,120
```

Details of each line are available in [Shell settings](../descript/shell/descript-txt/menu.font.name.md); a brief explanation follows.

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png
```

These three lines specify the three images used in the owner draw menu.

background is the normal menu background.

foreground is the background image for the selected item. More precisely, only the area of the owner draw menu under the cursor is replaced with the corresponding area of the foreground image.

sidebar is the image attached to the left side of the owner draw menu.

[![The three images used in the owner draw menu](../assets/image/ownerdraw_materials.png)](../assets/image/ownerdraw_materials.png)

[![Owner draw menu display](../assets/image/ownerdraw_view.png)](../assets/image/ownerdraw_view.png)

*The top image shows the three images used; the bottom shows the actual display (example: Emily/Phase4.5).*

```
menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom
```

These three lines specify the alignment of each of the three images.

In the example above, the background and foreground images are aligned to the top left. If the menu becomes larger than the background image due to the length or number of menu items, the colors at the right and left edges of the image are extended into the excess areas to the right and bottom, respectively.

```
menu.background.font.color.r,0
menu.background.font.color.g,0
menu.background.font.color.b,0
menu.foreground.font.color.r,0
menu.foreground.font.color.g,0
menu.foreground.font.color.b,255
menu.separator.color.r,0
menu.separator.color.g,0
menu.separator.color.b,0
menu.disable.font.color.r,120
menu.disable.font.color.g,120
menu.disable.font.color.b,120
```

These lines specify text colors.

background is the normal menu text color, foreground is the text color of the item under the cursor, separator is the color of menu separators, and disable is the text color of inactive items, such as the dressup menu for a shell with no dressup options or the network update item for a ghost that does not support network updates.

Specify each RGB color component as a value from 0 to 255. If all rgb components are 255, the color is white; if all are 0, it is black.

## Configuring with SHIORI Events

In addition to settings equivalent to those available in the shell's `descript.txt`, you can configure the display names of menu items and the contents of the favorites and portal link collections.

Even if the same item is configured in the shell's `descript.txt`, the SHIORI Event setting takes precedence.

Consult the documentation for your SHIORI to learn how to set and return values in response to SHIORI Events that retrieve menu resources.

For example, the following page may be useful for Satori.

[Satori wiki - Right-click menu](http://soliton.sub.jp/satori/index.php?%B1%A6%A5%AF%A5%EA%A5%C3%A5%AF%A5%E1%A5%CB%A5%E5%A1%BC)

For other available SHIORI Events, see [SHIORI Resource](../list/shiori-resource/ownerdraw-image/menu.sidebar.bitmap.filename.md).
