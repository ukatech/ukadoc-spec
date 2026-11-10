# OnDesktopWallpaperChange

**カテゴリ:** OS state event

Occurs when the desktop wallpaper is changed on the OS side. *\[NOTIFY at startup/GET otherwise\]*<br />
This occurs when the user changes the wallpaper in Personalization settings, as well as when it is automatically changed by a slideshow or Windows Spotlight, or when the theme is switched.<br />
Slideshows and Spotlight switch automatically at intervals as short as one minute. Therefore, when either triggers the event, it is notified using NOTIFY (cannot speak) even after startup.<br />
This is a separate event from [OnWallpaperChange](../file-drop/OnWallpaperChange.md), which occurs when the wallpaper is changed by dragging and dropping an image file. If SSP itself changes the wallpaper (Reference1 is self), both events occur. If responding to both, take care to avoid handling the change twice.<br />
In [window mode](OnWindowModeChange.md), the wallpaper for a ghost is the container background. A wallpaper change on the OS side triggers this event only when the container background is “Desktop”; it does not occur for white, gray, black, or an image. Instead, it occurs when the container background is changed (using the container menu, [`\![set,wallpaper]`](../../sakura-script/event/bang-set-wallpaper.md), or [`\![restore,wallpaper]`](../../sakura-script/event/bang-restore-wallpaper.md)), and when the background visible to the ghost changes due to switching window mode. It does not occur if the same background is simply selected again.<br />
With perghost (one container per ghost), the event occurs only when the background of the container the ghost is on changes.

- **Reference0**: init (startup notification) or update (change after startup)
- **Reference1**: Cause of the change.<br />
  user: Changed by the user<br />
  slideshow: Automatic slideshow change<br />
  spotlight: Automatic update by Windows Spotlight<br />
  theme: Change caused by switching themes<br />
  self: Changed by SSP itself (image drag and drop or restoration from a profile)<br />
  unknown: The change is confirmed, but its cause cannot be determined<br />
  In window mode, changes made using the container menu or by switching window mode are user; changes made using `\![set,wallpaper]` or `\![restore,wallpaper]` are self. For a startup notification (init), unknown is returned if the container background is anything other than “Desktop”.
- **Reference2**: Full path of the current wallpaper image. Empty for a solid-color background or if it could not be obtained.<br />
  Due to Windows behavior, this may be the path to a cache created by the OS (such as TranscodedWallpaper or the Spotlight cache), rather than the original image file selected by the user.<br />
  In window mode, this is the OS wallpaper if the container background is “Desktop”; the full path of the image if it is an image; and empty if it is a color setting such as white, gray, or black, or if no image is set.
- **Reference3**: Full path of the previous wallpaper image. Empty if Reference0 is init.
- **Reference4**: Display style. One of center / tile / stretch / fit / fill / span.<br />
  In window mode, stretch-x / stretch-y are also possible when the container background is an image. For white, gray, or black, this is center.
- **Reference5**: Desktop background color. The color shown in the margins around the wallpaper. R,G,B values separated by half-width commas.<br />
  In window mode, this is the base color of the container background if it is an image (the specified color if set, otherwise a color determined from the image), or the corresponding color if it is white, gray, or black.
- **Reference6～**: Wallpaper information for each monitor follows in the format below, repeated for the number of monitors. \[`\1`\] is byte value 1.<br />
  Monitor number\[`\1`\]Full path of wallpaper image\[`\1`\]Display style<br />
  Monitor numbers correspond to the order of Reference1 and onward in [OnDisplayChangeEx](OnDisplayChangeEx.md) (Reference1 is monitor number 0).<br />
  Since the OS does not maintain a display style for each monitor, the value is currently the same for all monitors (identical to Reference4).<br />
  Reference6 and onward are not included in environments that cannot handle per-monitor wallpapers (Windows 7 and earlier).<br />
  In window mode, regardless of the container background type, only one entry is included, treating the container as a single screen (monitor number 0).

**対応:** SSP 2.8.86
