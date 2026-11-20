# About `\![set,alignmenttodesktop,osuwari]`

`\![set,alignmenttodesktop,osuwari,オプション,…]` \[SSP 2.9.33\]

Makes the ghost's window "sit on", "stick to", or "hang from" the corners or edges of other windows. SSP incorporates the same behavior as ukiya's SAORI, "Osuwari.dll", and the options correspond to it. There is no need to write `seriko.alignmenttodesktop,free` in the shell's `descript.txt` (specifying `osuwari` is itself an alignment setting).

## Concept

At regular intervals, osuwari repeatedly answers the following question.

> Where on the screen should the upper-left corner of the ghost's window be placed?

The answer depends on which point of the ghost's window is aligned with which point of which window, and how many pixels it is offset. The elements involved are as follows.

- **Ghost's window**: A window for each character (`\0`, `\1`, etc.). Its size is the same as the currently displayed surface image, including transparent areas. Its position is expressed by the coordinates of its upper-left corner. When the surface changes and its size changes, the positions of its right edge, bottom edge, and center also change.
- **Target**: The window on which the ghost sits. It is measured by its visible frame, excluding invisible borders such as shadows.
- **Reference rectangle**: The rectangle on which the ghost sits instead of the target when it cannot sit on the target or would extend off-screen. It is either the whole monitor containing the target or its work area, as determined by `--area=` and `--side=`.
- **Origin**: The pair of points specifying which point of the ghost's window is aligned with which point of the target rectangle. `--origin=` selects the point on the ghost's window, and `--target-origin=` selects the point on the target rectangle.
- **Offset**: The displacement from the aligned position, specified by `--x=` and `--y=` (positive values move right and down).

The position is calculated for each of the X and Y axes using the following formula.

```
ゴーストのウインドウの左上 = 対象の矩形の点 − ゴーストのウインドウの点 + ずれ
```

`--origin=` determines the point on the ghost's window, and `--target-origin=` determines the point on the target rectangle. The rectangle used is the target's rectangle when sitting on the target, or the reference rectangle when the ghost cannot sit on it.

The options correspond to these decisions as follows.

| Decision | Option |
|---|---|
| Which window to sit on | `--target=` |
| Which point of the ghost's window to align | `--origin=` |
| Which point of the target rectangle to align with | `--target-origin=` |
| How far to offset from that position | `--x=` `--y=` |
| Where to sit when the ghost cannot sit on the target or would extend off-screen | `--area=` `--side=` `--margin=` `--noclip` |
| Range of movement by dragging | `--xmove` `--ymove` |
| Whether to appear in front of or behind the target | `--zorder=` |
| How often to follow the target | `--interval=` |

## How the position is determined

At each `--interval=`, the position is determined in the following order. However, it is not recalculated if the target, target rectangle, ghost window rectangle, surface base position, and sitting position have all remained unchanged since the previous check.

1. Find the target (`--target=`).
   - `active`: The foreground window. If the foreground window is one that the ghost cannot sit on (see below), use the last window it could sit on. If there has been no such window, there is no target.
   - `@文字列`: A window whose title contains the string and on which the ghost can sit. If there are multiple such windows, use the one nearest the front in Z-order.
   - `#数値`: The window whose window handle is the number specified in decimal. If the ghost cannot sit on it, there is no target.
   - `fix`: There is always no target.
2. Determine the rectangle to sit on. If there is a target and the ghost can sit on it, use the target rectangle. If there is no target, use the reference rectangle (`--area=` and `--side=`).
3. Align the two points selected by `--origin=` (the point on the ghost's window) and `--target-origin=` (the point on the other rectangle) to find the upper-left corner of the ghost's window. Add `--x=` and `--y=` to that position.
4. For each direction specified by `--xmove` or `--ymove`, if the ghost's window has been moved from its previous placement, such as by dragging, constrain that position inside the other rectangle and remember it as a proportion of the movable range. If a proportion has been remembered, use the position at that proportion within the other rectangle instead of the position calculated in step 3 ([Range of movement by dragging](bang-set-alignmenttodesktop.note.md#ドラッグで動かせる範囲)).
5. Check whether the ghost's window extends off-screen (the clipping check). If it does, replace the rectangle used in step 2 with the reference rectangle and repeat steps 3–4 once. Do not check again after the retry. No check is performed for `--target=fix`, `--noclip`, or when there is no target.
6. Move the ghost's window to the calculated position and adjust its Z-order (`--zorder=`).

The same selections for the two points in step 3 and the same offsets are used when retrying in step 5. Only the rectangle being sat on changes.

## Options

Options have the form `--名前=値`, and all are optional. Omitted options use their defaults, not the values specified in the previous call. Unrecognized options are ignored.

| Option | Default | Description |
|---|---|---|
| `--target=` | `active` | The target to follow. `active`: foreground window / `fix`: fixed to the screen (work area) / `@文字列`: a window whose title contains the string (case-insensitive) / `#数値`: the window whose handle is the number |
| `--origin=` | `osuwari` | Which point of the ghost's window to align with the target (the origin). Write it in the form `左右.上下` (see "Writing the origin" below). Corners can also be written as two letters, such as `tl`, `tr`, `bl`, or `br` |
| `--target-origin=` | Omitted (automatic) | \[SSP 2.9.34\] Which point of the target rectangle to align with the point of the ghost's window. The format is the same as `--origin=`, but `base` and `osuwari` cannot be used (see "Point on the target rectangle" below). If omitted, the point is on the same side as the `--origin=` point (`left` is the left edge, `right` is the right edge, and `center`, `base`, and `osuwari` are the center) |
| `--x=` `--y=` | `0` | Offset from the origin in pixels. In directions specified by `--xmove` or `--ymove`, this is the default until the window is moved |
| `--interval=` | `100` | Interval for checking the position in milliseconds. Values less than 10 are treated as 10 |
| `--xmove` `--ymove` | None | Allow dragging in that direction, within the target rectangle. The moved position is remembered as a proportion of the movable range (see "Range of movement by dragging" below). In directions not specified, the window returns to its sitting position even if dragged. These can also be written as, for example, `--xmove=false` |
| `--noclip` | None | Disable the clipping check |
| `--area=` | `workarea` | Reference area used when the ghost cannot sit on the target or would be clipped. `desktop`: entire screen / `workarea`: work area (the area excluding the taskbar, etc.) |
| `--side=` | `center` | Where to place the "virtual window" relative to the reference area when the ghost cannot sit on the target or would be clipped. `center`: the reference area itself / `top` `left` `right` `bottom`: place a virtual window 100 pixels thick on the top, left, right, or bottom side of the reference area |
| `--margin=` | `0_0_0_0` | Allowance for the clipping check in pixels. Specify in `左_上_右_下` order, separated by spaces or `_`. With `0_50_0_100`, for example, the window is not considered clipped until it extends more than 50 pixels above or 100 pixels below the screen |
| `--zorder=` | `front` | Z-order relative to the target window. `front`: display immediately above (in front of) the target / `back`: display immediately behind (directly below) the target. Does nothing while not sitting on a target (when the ghost cannot sit on it or with `--target=fix`) |

- The defaults for `--origin=` and `--area=` in the tag and `descript.txt` are `osuwari` and `workarea`. The built-in SAORI `osuwari` (compatible with Osuwari.dll) retains `tl` and `desktop` to match the original. \[SSP 2.9.34\] In 2.9.33, the defaults for the tag and `descript.txt` were also `tl` and `desktop`.
- When the ghost cannot sit on the target (`--target=fix`, no target window, or a foreground window that cannot be sat on with no previously usable window), or when it would be clipped (extend off-screen if placed there), it sits on the reference rectangle determined by `--area` and `--side` as a "virtual target". No clipping check is performed with `--target=fix`.
- Window rectangles are measured by their visible frames, excluding the invisible borders in Windows 10 and later. The reference screen is the monitor containing the target window, or the monitor containing the ghost if there is no target; while dragging, it is the monitor containing the cursor. Clipping is checked against the combined area of all monitors.
- The ghost cannot sit on minimized or hidden windows, windows on another virtual desktop, owned windows such as dialogs, or SSP's own windows (with `--target=active`). With `--target=active`, it also cannot sit on shell windows that are clearly unsuitable, such as the desktop, Alt+Tab and Task View, UWP windows displayed by the shell for Start, Search, IME panels, and similar functions, or full-screen Windows 8 Metro windows. When such a window is in the foreground, the ghost continues to sit on the last usable window. Windows explicitly specified with `@文字列` or `#数値` are not subject to these exclusions.
- While sitting, the ghost is displayed above the target window. osuwari makes the ghost topmost (always in front of other windows) only when the target is a topmost window, such as the taskbar; otherwise, the ghost is not topmost. However, a ghost configured to "always show in front" remains topmost regardless of the target. Even when the target is topmost, the ghost is displayed above it (whenever the target comes to the front, the ghost is also restored above it).
- With `--zorder=back`, the ghost is displayed immediately behind the target window (directly below it in Z-order). This can be used, for example, to make the ghost peek out from behind the target. Even if another application's window comes between them, the ghost returns immediately behind the target at the next position check (at the `--interval=` interval). If the target is a topmost window, such as the taskbar, the ghost also becomes topmost and is placed directly below the target among the topmost windows. If a ghost configured to "always show in front" sits behind a window that is not topmost, that setting takes priority and the ghost remains topmost (the back setting has no effect).
- To sit directly above the taskbar without following a window, use `--target=fix` to fix the ghost to the screen and use the bottom edge of the work area (for example, `--target=fix,--origin=bl,--area=workarea,--side=center`; use `--origin=br` for the right edge). Because the work area excludes the taskbar and similar elements, the ghost sits directly above the taskbar only when it is at the bottom of the screen. When the taskbar is at the top, left, or right of the screen, the ghost sits at the bottom of the screen (the bottom edge of the work area). When the taskbar is set to auto-hide, the work area covers the entire screen, so the ghost sits at the bottom of the screen.
- osuwari stops when another alignment (`top` `bottom` `left` `right` `free`) is specified, the shell is changed, and so on. `default` restores the ghost's default setting (`descript.txt`; see below). osuwari stops in window mode and resumes when normal mode is restored.
- The position while sitting is not saved as the standing position.
- Among windows linked by sticky window, specifying osuwari has no effect on the non-parent side (the linked child), because it follows the parent. When the parent sits, the child moves with it.
- `\0` and `\1` can each be specified separately. However, the Z-order of ghost windows is shared by the ghost as a whole, so when multiple characters sit, it is determined by the target of the character with the lower number.

## Specifying the origin \[SSP 2.9.34\]

`--origin=` aligns a point on the ghost's window with a point on the target rectangle. The format is `左右.上下`, where the part before `.` is the X axis and the part after it is the Y axis. Each part can use the following words (case-insensitive).

| Word | Point on the ghost's window | Point on the target rectangle (when `--target-origin=` is omitted) |
|---|---|---|
| `left` (for X) / `top` (for Y) | Left edge / top edge | Left edge / top edge |
| `right` (for X) / `bottom` (for Y) | Right edge / bottom edge | Right edge / bottom edge |
| `center` | Center | Center |
| `base` | Base position of the surface (`point.basepos.x` and `point.basepos.y`; defaults to the center at the feet) | Center |
| `osuwari` | Sitting position of the surface (`point.osuwaripos.x` and `point.osuwaripos.y`; defaults to the same as `base`) | Center |

- When `base` or `osuwari` is written alone without `.`, it applies to both the X and Y axes (`--origin=osuwari` means `osuwari.osuwari`). Any other word written alone specifies only the X axis, and the Y axis becomes `top`.
- `tl` is equivalent to `left.top`, `tr` to `right.top`, `bl` to `left.bottom`, and `br` to `right.bottom`.
- Unrecognized formats are ignored (the origin remains unchanged).
- The target rectangle has no `base` or `osuwari`, so its center is used when `--target-origin=` is omitted. For example, with the default `--origin=osuwari`, the ghost's sitting position is aligned with the center of the target rectangle. Adjust the sitting position with `--x=` and `--y=`, or change the target point with `--target-origin=`.
- Example: `--origin=center.bottom` aligns the ghost's center (X) and bottom edge (Y) with the target's center (X) and bottom edge (Y). `--origin=right.osuwari` aligns the ghost's right edge (X) and `point.osuwaripos.y` (Y) with the target's right edge (X) and center (Y).

## Point on the target rectangle \[SSP 2.9.34\]

`--target-origin=` determines the point on the target rectangle with which the point on the ghost's window is aligned. The format is the same as `--origin=` (`左右.上下`, `tl` `tr` `bl` `br`, or one word), but only `left` `right` `top` `bottom` `center` can be used. The target rectangle has no `base` or `osuwari`, so specifying either is treated as an unrecognized format and ignored.

- If omitted, the point is on the same side as the `--origin=` point. `left` and `top` mean the left and top edges, `right` and `bottom` mean the right and bottom edges, and `center`, `base`, and `osuwari` mean the center (the right column of the table above).
- If only one word is specified, it specifies the X axis, and the Y axis becomes `top`. `--target-origin=center` means `center.top` (the center of the target's top edge).
- Unrecognized formats are ignored (the point on the target rectangle remains unchanged).
- When the sitting target is the reference rectangle (when sitting is not possible), the point is on the reference rectangle (including a virtual window).
- Example: `--origin=osuwari --target-origin=center.top` aligns the surface's sitting position with the center of the target's top edge. `--origin=center.bottom --target-origin=center.top` aligns the ghost's center (X) and bottom edge (Y) with the target's center (X) and top edge (Y). The ghost's feet rest on the target's top edge regardless of the ghost's height.
- The built-in SAORI `osuwari` (compatible with Osuwari.dll) has no equivalent argument. As before, it aligns a corner of the ghost with the same corner of the target.

## Surface sitting position \[SSP 2.9.34\]

The sitting position can be specified with `point.osuwaripos.x` and `point.osuwaripos.y` in a surface brace in the shell's `surfaces.txt` ([point.osuwaripos.x](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.x.md) and [point.osuwaripos.y](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.y.md)). This is the point used by `osuwari` in `--origin=`; if omitted, it is the same as `point.basepos.x` and `point.basepos.y` (or their defaults if they are not specified).

For example, to place the sitting position at the waist of a surface with a width of 200 and a height of 300, write the following.

```
surface0
{
point.osuwaripos.x,100
point.osuwaripos.y,250
}
```

This position is measured in pixels from the top-left corner of the surface and scales with the surface. It is a separate point from the base position at the feet (`point.basepos`, or the center of the bottom edge (100,300) if omitted): `--origin=base` uses the base position, while `--origin=osuwari` uses the sitting position.

## Alignment example

The following example shows the surface above sitting on a window with its top-left corner at (400,400) and bottom-right corner at (1000,900). `--origin=osuwari --target-origin=center.top` aligns the ghost's sitting position with the center of the target's top edge.

![Relative positions of the ghost's window and the target when sitting with --origin=osuwari --target-origin=center.top](../../../assets/image/osuwari-origin.svg)

The sitting position (100,250) is aligned with the center of the target's top edge (700,400), so the ghost's top-left corner is at (700−100,400−250)=(600,150). The base position at the feet (by default, the center of the bottom edge) is at (700,450), 50 pixels below the sitting position and inside the window's top edge. The ghost is displayed in front of the target, so it appears to be sitting on the window's edge.

- If `point.osuwaripos` is specified for each surface, the ghost adjusts its sitting position when the surface changes so that the sitting position remains on the edge.
- If `--target-origin=` is omitted, the sitting position is aligned with the center of the target. To make the ghost sit on the edge, specify the target point, for example with `--target-origin=center.top`.
- Instead of using the sitting position, you can align the ghost by a corner or edge. `--origin=center.bottom --target-origin=center.top` aligns the center of the ghost's bottom edge with the center of the target's top edge (so its feet rest on it).
- If `--target-origin=` is omitted, the target point is always on the same side as the ghost's point, so the bottom edge cannot be aligned with the top edge. In that case, align the top edges and apply an offset, as in `--origin=tr --y=-300`. This offset is based on the ghost's height, so the feet will shift if the height changes.

## When sitting on the target is not possible or would go off-screen

When the ghost cannot sit on the target or would go off-screen by sitting on it, it sits on a reference rectangle instead. The reference rectangle is constructed in the following order.

1. Use `--area=` to select either the entire monitor containing the target (`desktop`) or its work area (`workarea`). If there is no target, use the monitor containing the ghost's window (or the monitor containing the cursor while dragging).
2. Use `--side=` to select either the rectangle from step 1 as is (`center`) or a virtual window placed outside it (`top` `left` `right` `bottom`). The virtual window is as long as the reference edge and 100 pixels thick.

![Virtual windows created by --side= and their positions relative to the reference rectangle](../../../assets/image/osuwari-side.svg)

When `bottom` is selected, the top edge of the virtual window overlaps the bottom edge of the reference rectangle. Combined with `--origin=osuwari --target-origin=center.top`, this places the sitting position at the center of the reference rectangle's bottom edge (on the top edge of the taskbar for the work area). With `--origin=center.bottom --target-origin=center.top`, the ghost's bottom edge rests there, placing its feet at the reference rectangle's bottom edge.

When sitting on the reference rectangle, `--origin=`, `--target-origin=`, `--x=`, and `--y=` are used in the same way as when sitting on a target.

!!! note "Note"
    If `--origin=osuwari --target-origin=center.top` is used with `--side=center` (the default), falling back to the reference rectangle places the ghost at the center of its top edge (the top edge of the entire work area). The sitting position (100,250) overlaps (960,0), so the ghost's top-left corner is at (860,-250), leaving most of it off-screen. No clipping check is performed after falling back to the reference rectangle, so the ghost is not pulled back. To make it sit at the bottom edge of the screen, combine this with `--side=bottom`.

The **clipping check** determines whether the entire ghost window, including transparent areas, fits within the rectangle enclosing all monitors.

- `--margin=` specifies how much to expand that rectangle outward. With `--margin=0_0_100_0`, the ghost is not considered clipped until it extends more than 100 pixels to the right. Use this when transparent surface padding alone would otherwise be considered clipped outside the screen.
- `--noclip` disables the clipping check entirely. Depending on the target's position, the ghost may remain off-screen.
- No clipping check is performed with `--target=fix` or when there is no target (the ghost is already sitting on the reference rectangle).

## Drag movement range

By default, dragging the ghost's window does not move it from its sitting position. `--xmove` permits horizontal dragging, and `--ymove` permits vertical dragging. Movement in an unspecified direction returns to the sitting position.

Movement is limited to the inside of the rectangle the ghost sits on.

- `--xmove`: The ghost window's left edge must be at or to the right of the rectangle's left edge, and its right edge must be at or to the left of the rectangle's right edge.
- `--ymove`: The ghost window's top edge must be at or below the rectangle's top edge, and its bottom edge must be at or above the rectangle's bottom edge.

The rectangle the ghost sits on is the target when sitting on the target, or the reference rectangle, including any virtual window, otherwise (with `--target=fix` or after falling back to the reference rectangle). For example, `--target=fix --origin=bl --xmove` makes the ghost stand on the bottom edge of the work area and allows only horizontal movement.

The moved position is remembered separately for each direction as a ratio within the movement range. A ratio of 0 places the ghost window's left edge (top edge) at the rectangle's left edge (top edge); a ratio of 1 places its right edge (bottom edge) at the rectangle's right edge (bottom edge).

- Until moved, the ghost sits at the position determined by `--origin=`, `--target-origin=`, `--x=`, and `--y=`. These define the default sitting position.
- Once moved, the ratio takes precedence in that direction, and `--origin=` and similar options are not used. The ghost sits at the same relative position even if the rectangle or the ghost window changes size. The same applies when the target or surface changes.
- The ratio is updated only when the ghost window is moved from its last placed position, such as by dragging or `\![move]`. It is not updated merely because the target moves or changes size.
- Directions in which movement is not permitted are still determined by the origin, target point, and offsets.
- Specifying `osuwari` again clears the remembered ratios and restores the defaults.
- Because movement is limited to the inside of the rectangle, once moved, the ghost cannot return to a position offset outside it, such as sitting on the target's top edge. To restore that position, specify `osuwari` again.
- When the ghost window is larger than the rectangle (the movement range is zero or less), no ratio can be determined. Moving it does not store a ratio; if a ratio is already stored, the ghost sits aligned with the rectangle's left edge (top edge). If it has not yet been moved, it remains at the default position.

For example, suppose the target's top-left corner is (300,400) and its bottom-right corner is (1100,1000), the ghost window is 200 wide and 300 high, and `--origin=tl --xmove` is specified. The initial top-left corner is (300,400).

- Dragging the left edge to 600 gives a ratio of 0.5 (the range is 300 to 900, and 600 is its midpoint).
- If the target's width becomes 600 (top-left (300,400), bottom-right (900,1000)), the range becomes 300 to 700 and the left edge moves to 500.
- If another window (top-left (1000,100), bottom-right (1400,800)) comes to the foreground, the range becomes 1000 to 1200 and the left edge moves to 1100.

## Z-order

While sitting, the ghost window maintains its Z-order relative to the target. Use `--zorder=` to select whether it appears in front of or immediately behind the target. This does not affect position calculations.

![Z-order of the ghost window and target with --zorder=front and --zorder=back](../../../assets/image/osuwari-zorder.svg)

- `front`: Moves the ghost immediately above the target only if it is below the target. If it is already above the target, it is not moved, even if another window is between them. This prevents ghosts sitting on the same window from competing for Z-order.
- `back`: Keeps the ghost immediately behind (directly below) the target. If a visible window from another application comes between them, the ghost is returned directly below the target at the next position check (at the interval specified by `--interval=`).

For topmost targets such as the taskbar and ghosts set to "Always on top", see the notes under "Options".

## Numerical examples

The following examples show where the upper-left corner of the ghost's window is placed under these conditions.

- Ghost window: 200 wide and 300 high. The surface reference position is the default center of the feet, (100,300). The sitting position is (100,250), specified in `surfaces.txt` as `point.osuwaripos.x,100` and `point.osuwaripos.y,250`.
- Screen: 1920×1080. The work area is 1920×1040 (the taskbar is at the bottom and is 40 pixels high).
- Target: Upper left (400,400), lower right (1000,900), unless otherwise noted.

Results for specifications that omit `--origin=` and `--area=` use the defaults in SSP 2.9.34 and later (`osuwari` and `workarea`). The defaults in 2.9.33 are `tl` and `desktop`, so the results differ.

| Specification | Upper left | Description |
|---|---|---|
| `--origin=osuwari` (default) | (600,400) | The sitting position (100,250) coincides with the center of the target (700,650). |
| `--origin=osuwari --target-origin=center.top` | (600,150) | The sitting position coincides with the center of the target's top edge (700,400). The ghost sits on the window edge (illustrated above). |
| `--origin=tr --x=-20 --y=-300` | (780,100) | Aligns the upper right with the target's upper right, then moves 20 left and 300 up. The bottom edge (400) coincides with the target's top edge, so the ghost stands on the top edge of the window. |
| `--origin=bl` | (400,600) | Aligns the lower left with the target's lower left. The bottom edge (900) coincides with the target's bottom edge. |
| `--origin=center.bottom --target-origin=center.top` | (600,100) | Aligns the center of the ghost's bottom edge with the center of the target's top edge (700,400). The ghost stands on the window's top edge regardless of its height. |
| `--target=fix --origin=osuwari --target-origin=center.top --side=bottom` | (860,790) | Aligns the sitting position with the center of the top edge (960,1040) of the virtual window below the work area. The ghost sits on the work area's bottom edge. |
| `--target=fix --origin=center.bottom --target-origin=center.top --side=bottom` | (860,740) | Aligns the center of the ghost's bottom edge with the same point. The ghost stands on the work area's bottom edge. |
| The specification in the third row, with a maximized target (upper left (0,0), lower right (1920,1040)). Add `--side=bottom`. | (1700,740) | The top edge would be off-screen (-300), so it is clipped. The ghost falls back to the virtual window below the work area and sits using the same `--origin=`, `--x=`, and `--y=`. Its bottom edge is at 1040 (the bottom edge of the work area). |
| Remove `--side=bottom` from the row above | (1700,-300) | The ghost falls back to the work area itself. Clipping is not checked, so the ghost sits off-screen. |
| `--target=fix --origin=bl` | (0,740) | The ghost stands at the lower left of the work area. With `--origin=br`, the result is (1720,740). |
| `--target=fix` | (860,270) | The sitting position coincides with the center of the work area (960,520). |
| Target is (1500,400)-(2000,900). `--origin=tr --y=-300 --side=bottom` | (1720,740) | The right edge at 2000 exceeds the screen's right edge at 1920, so it is clipped. The ghost falls back to the virtual window below the work area. |
| Add `--margin=0_0_100_0` or `--noclip` to the row above | (1800,100) | The ghost remains seated on the target because an overhang of 100 pixels to the right is allowed (or clipping is not checked). |

## Writing to descript.txt

You can also specify `osuwari` as the value of `seriko.alignmenttodesktop` in the ghost's or shell's `descript.txt` (including the versions prefixed with `sakura.`, `kero.`, or `char*.`). After the value, list the same `--` options as the tag, separated by commas ([※ Display position information](../../../descript/shell/descript-txt/note-1.md#補足)).

```
sakura.seriko.alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom
```

- The precedence is the same as for other values (ghost-wide < per-scope ghost setting < shell-wide < per-scope shell setting).
- Tracking starts with these settings when the ghost starts or the shell is switched.
- `\![set,alignmenttodesktop,default]` and `STOP` in the built-in SAORI `osuwari` restore the `descript.txt` settings. If `descript.txt` specifies osuwari, the ghost sits down again using osuwari.
- Unrecognized options are ignored and a warning is written to the error log.

## Relationship to the built-in SAORI

The built-in SAORI `osuwari` (compatible with Osuwari.dll) performs the same operation. However, to match the original, the SAORI's `START` retains the previous values when the seventh and subsequent arguments are omitted ([compatibility module](../../../spec/saori-ex/compat.md)).

## 記述例

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom]前面のウインドウの上端の中央に腰かける（横にだけ動かせる）。座れないときは、ワークエリアの下端に座る。\![set,alignmenttodesktop,default]
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--origin=tr,--x=-20,--y=-90,--xmove,--area=workarea,--side=bottom]前面のウインドウの右上に座る（横にだけ動かせる）。座れないときはワークエリアの下端に座る。\![set,alignmenttodesktop,default]
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=fix,--origin=br,--area=workarea,--side=center]ウインドウには追従せず、タスクバーの直上の右端に座る。\![set,alignmenttodesktop,default]
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--area=workarea,--side=bottom,--zorder=back]前面のウインドウの上端の中央に、そのウインドウのすぐ奥から腰かける。上半身が窓の上にのぞく。\![set,alignmenttodesktop,default]
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--origin=center.bottom,--target-origin=center.top,--area=workarea,--side=bottom]前面のウインドウの上端の中央に、足元を乗せて立つ。ウインドウが上に寄っていて座れないときは、ワークエリアの下端に立つ。\![set,alignmenttodesktop,default]
```
