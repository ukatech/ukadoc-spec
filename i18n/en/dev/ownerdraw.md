# Configuring the owner-draw menu

This page explains how to configure the display of the owner-draw menu (right-click menu).

Also refer to “[Owner-draw menu](../manual/owner-draw-menu.md)” in File structure.

Configure this in the shell's `descript.txt`, or in responses to some SHIORI Events issued to retrieve resources.

## 目次

1. [Configure in the shell's descript.txt](ownerdraw.md#シェルのdescripttxtで設定する)
2. [Configure with SHIORI Events](ownerdraw.md#shiori-eventで設定する)

## Configure in the shell's descript.txt

In the shell's `descript.txt`, you can configure three images used for the normal and selected backgrounds and the sidebar, as well as the text color.

SSP also allows you to specify the text size and font.

The placement of items in the dressup menu is also configured in the shell's `descript.txt`. For details, refer to “[Configuring dressup](bind.md)”.

Note that if the same setting is also specified using a SHIORI Event, the setting from the SHIORI Event takes precedence.

Here is an example of the `descript.txt` settings.

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
menu.disable.font.color.120
menu.disable.font.color.120
menu.disable.font.color.120
```

Details for each line are in “[Shell settings](../descript/shell/descript-txt/menu.font.name.md)”; here is a general explanation.

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png
```

The three lines above configure each of the three images used by the owner-draw menu.

background is the menu background in its normal state.

foreground is the background image for the selected item. This may be a little difficult to understand, but only the area where the cursor is currently positioned in the owner-draw menu is replaced with the corresponding area of the foreground image, over the background image.

sidebar is the image displayed on the left side of the owner-draw menu.

[![The three images used by the owner-draw menu](../assets/image/ownerdraw_materials.png)](../assets/image/ownerdraw_materials.png)

[![Owner-draw menu display](../assets/image/ownerdraw_view.png)](../assets/image/ownerdraw_view.png)

*The three images used are shown above; the actual display is shown below (example: Emily/Phase4.5)*

```
menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom
```

The three lines above configure the placement of each of the three images.

In the example above, the background and foreground images are positioned with their top-left corners as the origin. If the menu becomes larger than the background image due to the number of characters or items, the colors at the image's right and bottom edges are extended to fill the areas beyond it.

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
menu.disable.font.color.120
menu.disable.font.color.120
menu.disable.font.color.120
```

The settings above specify text colors.

background is the menu text color in its normal state, foreground is the text color when the cursor is over an item, separator is the color of menu separators, and disable is the text color for inactive items, such as the dressup menu in a shell without dressups or the network update item in a ghost that does not support network updates.

Specify each RGB color component as a value from 0 to 255. If all RGB values are 255, the color is white; if they are all 0, it is black.

## Configure with SHIORI Events

In addition to settings equivalent to those made in the shell's `descript.txt`, you can configure the display names of menu items and the contents of the link collections for favorites and portals.

Even if the same setting is specified in the shell's `descript.txt`, the setting from the SHIORI Event takes precedence.

For details on how to set and return values for SHIORI Events that retrieve menu resources, refer to the documentation for each SHIORI.

For example, the following page may be useful for Satori.

[Satori wiki - Right-click menu](http://soliton.sub.jp/satori/index.php?%B1%A6%A5%AF%A5%EA%A5%C3%A5%AF%A5%E1%A5%CB%A5%E5%A1%BC)

For information about other available SHIORI Events, refer to “[SHIORI Resource](../list/shiori-resource/ownerdraw-image/menu.sidebar.bitmap.filename.md)”.
