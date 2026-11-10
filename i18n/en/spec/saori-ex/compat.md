# Compatibility modules

SSP includes compatibility implementations for the following commonly used SAORI DLLs. When a ghost loads one of these DLLs, SSP substitutes its built-in implementation without reading the DLL (determined by the file name).<br />
\[SSP 2.9.13\] These can also be called from Direct SSTP using the name with `.dll` removed from the DLL name (such as `Module: string`). Arguments and return values are the same as in the original SAORI.

`houchi` `clipcopy` `textcopy` `saori_ip` `saori_cpuid` `mciaudio` `cpuusage` `httpc` `string` `hanayu` `osuwari` (`osuwari` from \[SSP 2.9.33\])

- Direct SSTP has no `load` / `unload`, so modules that maintain state per ghost (`mciaudio` / `httpc` / `string` / `hanayu`) are initialized on that ghost's first call and discarded when the ghost exits (including when SHIORI is reloaded). They do not share state with instances loaded as DLLs.
- Calls without a ghost return 400 (`ghost required`) for operations that depend on a ghost (`httpc` retrieval, saving, and `bg`; `hanayu` `show`; `mciaudio` `load` / `play` / `loop` / `stop`).
- `houchi` works when loaded, so calling it from Direct SSTP does nothing.
- Direct SSTP requests are processed on SSP's main thread, so use `bg` when retrieving data with `httpc` (otherwise, SSP's display freezes while the data is retrieved).

## osuwari \[SSP 2.9.33\]

Compatible with ukiya's `Osuwari.dll`. It makes the ghost's window follow the foreground window, a specified window, or a screen rectangle (it performs the same operation as [`\![set,alignmenttodesktop,osuwari,…]`](../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md); the meaning of the options is also described there). Arguments are positional, as in the original.

- `START`: In order from `Argument1`: HWND to control / tracking target (`ACTIVE` `FIX` `@title` `#handle`) / origin (`TL` `TR` `BL` `BR`) / x offset / y offset / update interval (milliseconds; 0 means 100) / (optional) options (`XMOVE` `YMOVE` `NOCLIP` `BACK`, space-separated. `BACK` places the window immediately behind the target window. This option is not in the original) / (optional) fallback when it cannot be positioned (`DESKTOP` `WORKAREA` and `CENTER` `LEFT` `RIGHT` `TOP` `BOTTOM`, space-separated) / (optional) clipping margin (`left_top_right_bottom`).
  - If arguments from the 7th onward are omitted, their values from the previous `START` are retained. This is the same behavior as the original. With `\![set,alignmenttodesktop,osuwari,…]`, omitted options are set to their defaults each time (not retained).
  - The HWND to control can only be **the character window of that ghost**, as reported by the `OnHWND` event (`hwnd`). Other windows are not moved (500 if it cannot be found).
- `STOP`: Stops the positioning set by the SAORI and restores the ghost/shell default alignment (`descript.txt`). If the default in `descript.txt` is osuwari, it positions the window using osuwari again. It does not stop positioning set with `\![set,alignmenttodesktop,osuwari,…]`. It also stops when the SAORI is unloaded (including when SHIORI is reloaded).
- Success returns 204; insufficient or unparseable arguments return 400; if the HWND to control cannot be found, it returns 500 (`source window is not exist`).
- Differences from the original are as follows.
  - The window rectangle is measured using its visible frame.
  - The reference screen is the monitor containing the target window (clipping is checked against the combined area of all monitors).
  - The original bug that always sets `side` to `TOP` when `DESKTOP` is specified is not present.
  - It does not position the window on minimized or hidden windows.
  - There is no need to write `seriko.alignmenttodesktop,free` in the shell's `descript.txt`.
- Renamed DLLs (such as `osuwari0.dll`) are not covered by this compatibility implementation. The actual DLL is loaded.
