# Owner-drawn menu

Image files used by the owner-drawn menu (right-click menu).

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
　　　　　　+-surfaces**.txt
　　　　　　+-alias.txt
　　　　　　+-thumbnail.png
　　　　　　+-makoto.dll
　　　　　　+-surfacetable.txt
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
```

The files do not necessarily need to be in the locations shown above; they can also be placed in subfolders.

When configuring the owner-drawn menu through SHIORI Resource, it is convenient to place the files under ghost/master (since paths are specified relative to ghost/master).

- **menu_background.png**: Background image for the owner-drawn menu.

  The menu area is determined by the menu dimensions, not by the image dimensions.

  Optional (the standard menu display is used if omitted).

- **menu_foreground.png**: Image for the cursor selection in the owner-drawn menu tree.

  Optional (the standard menu display is used if omitted).

- **menu_sidebar.png**: Image that can be added to the left side of the owner-drawn menu tree.

  Only the width is taken from the image.

  Optional.

For all of these, the images, text colors, and other settings are configured through the shell's [descript.txt](../descript/shell/index.md) or [SHIORI Resource](../list/shiori-resource/index.md).

When configured through SHIORI Resource, this can be used to change the menu display according to the ghost's state, for example if characters take turns or the ghost has a mode-switching feature.

If settings are specified in both the shell's descript.txt and SHIORI Resource, the SHIORI Resource settings take precedence.

The image filenames do not necessarily have to match the examples above (any names can be used).

See also the page on [owner-drawn menu settings](../dev/ownerdraw.md) for details.

Parts of the menu image that are cut off are filled with a solid color matching the color at the edge.

If no image is specified, a standard popup menu is displayed.
