# OnDesktopWallpaperChange

**カテゴリ:** OS state event

Occurs when the desktop wallpaper is changed on the OS side. *\[NOTIFY at startup / GET at other times\]*<br />
Occurs when the user changes the wallpaper in Personalization settings, as well as when it is automatically changed by a slideshow or Windows Spotlight, or when the theme changes.<br />
Slideshow and Spotlight change automatically at intervals as short as one minute, so when either triggers this event, it is notified with NOTIFY (cannot speak) even after startup.<br />
This is a different event from [OnWallpaperChange](../file-drop/OnWallpaperChange.md), which occurs when the wallpaper is changed by dragging and dropping an image file. If SSP itself changes the wallpaper (Reference1 is self), both events occur. Take care to avoid duplicate handling if responding to both.<br />
In [window mode](OnWindowModeChange.md), the wallpaper for the ghost is the container background. A wallpaper change on the OS side triggers this event only when the container background is “Desktop”; it does not occur for white, gray, black, or an image. Instead, it occurs when the container background changes (via the container menu, [`\![set,wallpaper]`](../../sakura-script/event/bang-set-wallpaper.md), or [`\![restore,wallpaper]`](../../sakura-script/event/bang-restore-wallpaper.md)), or when switching window modes changes the background visible to the ghost. It does not occur just by selecting the same background again.<br />
With perghost (one container per ghost), this event occurs only when the background of the container the ghost is on changes.

- **Reference0**: init (startup notification) or update (change after startup)
- **Reference1**: Cause of the change.<br />
  user: Changed by the user<br />
  slideshow: Automatic slideshow transition<br />
  spotlight: Automatic Windows Spotlight update<br />
  theme: Change caused by switching themes<br />
  self: Changed by SSP itself (image drag and drop or restore from a profile)<br />
  unknown: The change is known to have occurred, but its cause cannot be determined<br />
  In window mode, changes made through the container menu or by switching window modes are user; changes made with `\![set,wallpaper]` or `\![restore,wallpaper]` are self. At startup (init), if the container background is not “Desktop”, the value is unknown.
- **Reference2**: Full path to the current wallpaper image. Empty for a solid-color background or if the path could not be obtained.<br />
  Due to Windows behavior, this may be the path to a cache created by the OS (such as TranscodedWallpaper or the Spotlight cache), rather than the original image file selected by the user.<br />
  In window mode, if the container background is “Desktop”, this is the OS wallpaper; if it is an image, this is the full path to that image; if it is a color setting such as white, gray, or black, it is empty.
- **Reference3**: Full path to the previous wallpaper image. Empty if Reference0 is init.
- **Reference4**: Display style. One of center / tile / stretch / fit / fill / span.<br />
  In window mode, stretch-x / stretch-y are also possible if the container background is an image. For white, gray, or black, the value is center.
- **Reference5**: Desktop background color. The color shown in the margins around the wallpaper. R,G,B values separated by ASCII commas.<br />
  In window mode, this is the background color of the container: the image's base color if the background is an image (the specified color, if any; otherwise a color derived from the image), or the corresponding color for white, gray, or black.
- **Reference6～**: Wallpaper information for each monitor follows, with one entry per monitor, in the following format. \[`\1`\] is byte value 1.<br />
  Monitor number\[`\1`\]Full path to wallpaper image\[`\1`\]Display style<br />
  Monitor numbers correspond to the order of Reference1 and later in [OnDisplayChangeEx](OnDisplayChangeEx.md) (Reference1 is monitor number 0).<br />
  Since the OS does not store the display style separately for each monitor, the same value is currently used for all monitors (identical to Reference4).<br />
  On systems that cannot handle per-monitor wallpapers (Windows 7 and earlier), Reference6 and later are omitted.<br />
  In window mode, regardless of the container background type, there is only one entry, treating the container as one screen (monitor number 0).

**対応:** SSP 2.8.86
