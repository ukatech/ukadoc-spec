# Compatibility modules

SSP includes compatibility functions for the following commonly used SAORI DLLs. When a ghost loads one of these DLLs, SSP replaces it with its built-in function without reading the DLL (determined by the file name).<br />
\[SSP 2.9.13\] These can also be called from Direct SSTP using the DLL name without `.dll` (such as `Module: string`). Arguments and return values are the same as the original SAORI.

`houchi` `clipcopy` `textcopy` `saori_ip` `saori_cpuid` `mciaudio` `cpuusage` `httpc` `string` `hanayu` `osuwari`（`osuwari` is available since \[SSP 2.9.33\]）

- Direct SSTP has no `load` / `unload`, so modules that maintain state per ghost (`mciaudio` / `httpc` / `string` / `hanayu`) are initialized on that ghost's first call and discarded when the ghost exits (including when SHIORI is reloaded). They do not share state with instances loaded as DLLs.
- When called without a ghost, operations that depend on a ghost (`httpc` retrieval, saving, and `bg`; `hanayu`'s `show`; `mciaudio`'s `load` / `play` / `loop` / `stop`) return 400 (`ghost required`).
- `houchi` takes effect when loaded, so calling it from Direct SSTP does nothing.
- Direct SSTP requests are processed on SSP's main thread, so use `bg` for `httpc` retrieval (otherwise, SSP's screen will freeze during retrieval).

## osuwari \[SSP 2.9.33\]

Compatibility with ukiya's `Osuwari.dll`. It makes the ghost's window follow the foreground window, a specified window, or a rectangle on the screen (the same operation as [`\![set,alignmenttodesktop,osuwari,…]`](../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md); the meaning of the options is also described there). Arguments are positional, as in the original.

- `START`: Starting from `Argument1`, specify the controlled HWND / follow target (`ACTIVE` `FIX` `@title` `#handle`) / origin (`TL` `TR` `BL` `BR`) / x offset / y offset / update interval (milliseconds; 0 means 100) / (optional) options (`XMOVE` `YMOVE` `NOCLIP` `BACK`, separated by spaces; `BACK` sits immediately behind the target window; not available in the original) / (optional) placement when it cannot sit (`DESKTOP` `WORKAREA` and `CENTER` `LEFT` `RIGHT` `TOP` `BOTTOM`, separated by spaces) / (optional) clipping margin (`left_top_right_bottom`).
  - If the seventh and subsequent arguments are omitted, their values from the previous `START` are carried over. This matches the original behavior. With `\![set,alignmenttodesktop,osuwari,…]`, omitted options are set to their defaults each time (they are not carried over).
  - The controlled HWND can only be the **character window of that ghost** reported by the `OnHWND` event (`hwnd`). Other windows will not be moved (500 if it cannot be found).
- `STOP`: Stops the seating set by SAORI and restores the alignment to the ghost/shell default (`descript.txt`). If the default in `descript.txt` is osuwari, it sits down with osuwari again. This does not stop settings made with `\![set,alignmenttodesktop,osuwari,…]`. It also stops when SAORI is unloaded (including when SHIORI is reloaded).
- Returns 204 on success, 400 if arguments are missing or cannot be interpreted, and 500 if the controlled HWND cannot be found (`source window is not exist`).
- The differences from the original are as follows.
  - Window rectangles are measured using the visible frame.
  - The reference screen is the monitor containing the target window (clipping is checked against the area spanning all monitors).
  - The original bug where `side` is always `TOP` when `DESKTOP` is specified is not present.
  - It does not sit on minimized or hidden windows.
  - There is no need to write `seriko.alignmenttodesktop,free` in the shell's `descript.txt`.
- Renamed DLLs (such as `osuwari0.dll`) are not covered by compatibility. The actual DLL is loaded.
