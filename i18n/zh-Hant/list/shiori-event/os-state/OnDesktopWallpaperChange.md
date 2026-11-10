# OnDesktopWallpaperChange

**カテゴリ:** OS state event

Occurs when the desktop wallpaper is changed by the OS. *\[NOTIFY at startup / GET otherwise\]*<br />
Occurs when the user changes the wallpaper in Personalization settings, as well as when it is automatically changed by a slideshow or Windows Spotlight, or when the theme is switched.<br />
Slideshow and Spotlight change automatically at intervals as short as one minute, so when either triggers the event, it is notified as NOTIFY (cannot speak) even after startup.<br />
This is a separate event from [OnWallpaperChange](../file-drop/OnWallpaperChange.md), which occurs when the wallpaper is changed by dragging and dropping an image file. If SSP itself changes the wallpaper (Reference1 is self), both events occur. Take care to avoid handling the change twice if responding to both.<br />
In [window mode](OnWindowModeChange.md), the wallpaper for a ghost is the container background. A wallpaper change by the OS triggers this event only when the container background is “Desktop”; it does not occur for white, gray, black, or an image. Instead, it occurs when the container background changes (via the container menu, [`\![set,wallpaper]`](../../sakura-script/event/bang-set-wallpaper.md), or [`\![restore,wallpaper]`](../../sakura-script/event/bang-restore-wallpaper.md)), or when the background visible to the ghost changes due to switching window mode. It does not occur if the same background is selected again.<br />
With perghost (one container per ghost), the event occurs only when the background of the container the ghost is on changes.

- **Reference0**: init (startup notification) or update (change after startup)
- **Reference1**: Cause of the change.<br />
  user: Changed by the user<br />
  slideshow: Automatic slideshow change<br />
  spotlight: Automatic Windows Spotlight update<br />
  theme: Change due to switching themes<br />
  self: Changed by SSP itself (image drag-and-drop / restore from profile)<br />
  unknown: The change is known to have occurred, but its cause cannot be determined<br />
  In window mode, changes made through the container menu or by switching window mode are user; changes made through `\![set,wallpaper]` or `\![restore,wallpaper]` are self. For startup notification (init), this is unknown if the container background is not “Desktop”.
- **Reference2**: Full path of the current wallpaper image. Empty for a solid-color background or if unavailable.<br />
  Due to Windows behavior, this may be the path to an OS-created cache (such as TranscodedWallpaper or a Spotlight cache), rather than the original image file selected by the user.<br />
  In window mode, if the container background is “Desktop”, this is the OS wallpaper; if it is an image, this is the full path to that image; if it is white, gray, black, or a specified color without an image, it is empty.
- **Reference3**: Full path of the previous wallpaper image. Empty if Reference0 is init.
- **Reference4**: Display style. One of center / tile / stretch / fit / fill / span.<br />
  In window mode, stretch-x / stretch-y may also be returned if the container background is an image. For white, gray, or black, the value is center.
- **Reference5**: Desktop background color. The color displayed in the margins around the wallpaper. R,G,B separated by half-width commas.<br />
  In window mode, if the container background is an image, this is its base color (the specified color, if set; otherwise, a color derived from the image); for white, gray, or black, it is that color.
- **Reference6～**: Wallpaper information for each monitor follows, in the format below, repeated for the number of monitors. \[`\1`\] is byte value 1.<br />
  Monitor number\[`\1`\]full path of wallpaper image\[`\1`\]display style<br />
  Monitor numbers correspond to the order of Reference1～ in [OnDisplayChangeEx](OnDisplayChangeEx.md) (Reference1 is monitor number 0).<br />
  Since the OS does not retain the display style per monitor, the value is currently the same for all monitors (identical to Reference4).<br />
  In environments that cannot handle wallpaper per monitor (Windows 7 and earlier), Reference6 and later are not included.<br />
  In window mode, regardless of the container background type, only one entry is included (monitor number 0), treating the container as a single screen.

**対応:** SSP 2.8.86
