# About `\![set,alignmenttodesktop,osuwari]`

`\![set,alignmenttodesktop,osuwari,オプション,…]` \[SSP 2.9.33\]

This makes a ghost window “sit” on, “attach” to, or “hang” from the corner or edge of another window. SSP has built in the same behavior as ukiya's SAORI, “Osuwari.dll,” and its options are compatible with it. There is no need to add `seriko.alignmenttodesktop,free` to the shell's `descript.txt` (`osuwari` itself specifies the alignment).

## How it works

At regular intervals, osuwari repeats the following:

> Where on the screen should the top-left corner of the ghost window be placed?

The answer depends on “which window,” “which point on it,” “which point on the ghost window,” and “how many pixels to offset it.” The elements are as follows.

- **Ghost window**: The window for each character (`\0`, `\1`, …). Its size matches the image of the currently displayed surface, including transparent areas. Its position is represented by the coordinates of its top-left corner. When the surface changes and its size changes, the positions of its right edge, bottom edge, and center also change.
- **Target**: The window that the ghost sits on. Its visible frame is used for measurements; invisible frames, such as shadows, are not included.
- **Reference rectangle**: The rectangle to sit on instead of the target when the target cannot be sat on or sitting on it would extend beyond the screen. This is either the entire monitor containing the target or its work area, determined by `--area=` and `--side=`.
- **Origin**: A pair of points specifying which point on the target rectangle to align with which point on the ghost window. Set the point on the ghost window with `--origin=` and the point on the target rectangle with `--target-origin=`.
- **Offset**: The displacement from the aligned position. Set it with `--x=` and `--y=` (positive values are right and down).

The position is calculated separately for the X and Y axes using the following formula.

```
ゴーストのウインドウの左上 = 対象の矩形の点 − ゴーストのウインドウの点 + ずれ
```

`--origin=` specifies the point on the ghost window, and `--target-origin=` specifies the point on the target rectangle. When sitting on a target, the target rectangle is used; when the target cannot be sat on, the reference rectangle is used.

The options for each setting are as follows.

| Setting | Option |
|---|---|
| Which window to sit on | `--target=` |
| Which point on the ghost window to align | `--origin=` |
| Which point on the target rectangle to align | `--target-origin=` |
| How far to offset from that point | `--x=` `--y=` |
| Where to sit when the target cannot be sat on or the ghost extends beyond the screen | `--area=` `--side=` `--margin=` `--noclip` |
| The range in which dragging can move the ghost | `--xmove` `--ymove` |
| Whether to appear in front of or behind the target | `--zorder=` |
| How often to follow the target | `--interval=` |

## How the position is determined

The position is determined in the following order at each `--interval=` interval. However, it is not recalculated if the target, target rectangle, ghost window rectangle, surface reference position, and sitting position have all remained unchanged since the previous check.

1. Find the target (`--target=`).
   - `active`: The foreground window. If a window that cannot be sat on (see below) is in the foreground, use the most recent window that could be sat on. If there is no such window yet, there is no target.
   - `@string`: A window whose title contains the string and that can be sat on. If there are multiple matches, use the one highest in the Z-order.
   - `#number`: The window whose handle is the specified number (in decimal). If it cannot be sat on, there is no target.
   - `fix`: There is never a target.
2. Determine the rectangle to sit on. If there is a target and it can be sat on, use its rectangle. If there is no target, use the reference rectangle (`--area=` and `--side=`).
3. Overlay the two points selected by `--origin=` (the point on the ghost window) and `--target-origin=` (the point on the other rectangle) to calculate the top-left corner of the ghost window. Add `--x=` and `--y=` to that position.
4. In the directions specified by `--xmove` and `--ymove`, if the ghost window has been moved from its previous position (for example, by dragging), constrain it to the inside of the other rectangle and remember its position as a ratio of the movable range. If a ratio has been remembered, use the position at that ratio within the other rectangle instead of the position calculated in step 3 ([range in which dragging can move the ghost](bang-set-alignmenttodesktop.note.md#ドラッグで動かせる範囲)).
5. Check whether the ghost window extends beyond the screen (the clipping check). If it does, replace the rectangle from step 2 with the reference rectangle and repeat steps 3–4 once. Do not check again after repeating them. Skip the check when `--target=fix`, `--noclip`, or there is no target.
6. Move the ghost window to the calculated position and adjust its Z-order (`--zorder=`).

The same two points and offset from step 3 are used when repeating the calculation in step 5. Only the rectangle to sit on changes.

## Options

Options use the form `--name=value`, and all can be omitted. Omitted options use their default values, not the values specified in the previous call. Options that cannot be interpreted are ignored.

| Option | Default | Description |
|---|---|---|
| `--target=` | `active` | Target to follow. `active`: foreground window / `fix`: fixed to the screen (work area) / `@string`: window whose title contains the string (case-insensitive) / `#number`: window whose handle is the specified number |
| `--origin=` | `osuwari` | Which point on the ghost window to align with the target (the origin). Write it as `horizontal.vertical` (see “How to write origins” below). You can also specify a corner using two letters, such as `tl`, `tr`, `bl`, or `br` |
| `--target-origin=` | omitted (automatic) | \[SSP 2.9.34\] Which point on the target rectangle to align with the point on the ghost window. The syntax is the same as for `--origin=`, but `base` and `osuwari` cannot be used (see “Points on the target rectangle” below). If omitted, it uses the same side as the point specified by `--origin=` (`left` is the left edge, `right` is the right edge, and `center`, `base`, and `osuwari` are the center) |
| `--x=` `--y=` | `0` | Offset from the origin, in pixels. In directions where `--xmove` or `--ymove` is specified, this is the default position until the ghost is moved |
| `--interval=` | `100` | Interval between position checks, in milliseconds. Values below 10 are treated as 10 |
| `--xmove` `--ymove` | none | Allow dragging in the specified direction (up to the inside of the target rectangle). The moved position is remembered as a ratio of the movable range (see “Range in which dragging can move the ghost” below). In directions not specified, dragging returns the ghost to its sitting position. Can also be written as `--xmove=false` |
| `--noclip` | none | Do not perform the clipping check |
| `--area=` | `workarea` | Reference used when the target cannot be sat on or the ghost extends beyond the screen. `desktop`: entire screen / `workarea`: work area (the area excluding the taskbar, etc.) |
| `--side=` | `center` | Where to place the “virtual window” relative to the reference when the target cannot be sat on or the ghost extends beyond the screen. `center`: the reference itself / `top`, `left`, `right`, `bottom`: place a 100-pixel-thick virtual window above, to the left, to the right, or below the reference |
| `--margin=` | `0_0_0_0` | Tolerance for the clipping check, in pixels. Specify in the order `left_top_right_bottom`, separated by spaces or `_`. With `0_50_0_100`, the ghost is not considered clipped until it extends 50 pixels above or 100 pixels below |
| `--zorder=` | `front` | Z-order relative to the target window. `front`: display immediately above (in front of) the target / `back`: display immediately behind (directly below) the target. Does nothing when not sitting on a target (when it cannot be sat on or with `--target=fix`) |

- The defaults for `--origin=` and `--area=` are `osuwari` and `workarea` for the tag and `descript.txt`. The built-in SAORI `osuwari` (compatible with Osuwari.dll) retains the original defaults, `tl` and `desktop`. \[SSP 2.9.34\] In 2.9.33, the defaults for the tag and `descript.txt` were also `tl` and `desktop`.
- When the target cannot be sat on (with `--target=fix`, when the target window does not exist, or when the foreground window cannot be sat on and there is no previously usable window) and when the ghost extends beyond the screen (sitting on the target as-is would extend beyond the screen), the ghost sits on the reference rectangle determined by `--area` and `--side`, treated as a “virtual target.” The clipping check is not performed with `--target=fix`.
- Window rectangles are measured using their visible frames (excluding invisible frames on Windows 10 and later). The reference monitor is the one containing the target window (or the monitor containing the ghost when there is no target; while dragging, the monitor containing the cursor). Clipping is checked against the combined area of all monitors.
- The ghost cannot sit on minimized or hidden windows, windows on another virtual desktop, owned windows such as dialogs, or SSP's own windows (when `--target=active`). With `--target=active`, it also cannot sit on shell windows that it is clearly not appropriate to sit on, such as the desktop, Alt+Tab and Task View, UWP windows displayed by the shell such as Start, Search, and IME panels, and full-screen Metro windows in Windows 8. If one of these windows is in the foreground, the ghost stays on the most recent window it could sit on. Windows explicitly specified with `@string` or `#number` are not excluded.
- While sitting on a target, the ghost is displayed above its window. osuwari makes the ghost topmost (always in front of other windows) only when the target is a topmost window (such as the taskbar); otherwise, the ghost is not topmost. However, ghosts configured to “always stay on top” remain topmost due to that setting, regardless of the target. Even when the target is a topmost window, the ghost is displayed above it (whenever the target comes to the foreground, the ghost is also brought to the top).
- With `--zorder=back`, the ghost is displayed immediately behind the target window (directly below it in the Z-order). This can be used to make the ghost peek out from behind the target. If another application's window gets between them, the ghost returns to immediately behind the target at the next position check (at the `--interval=` interval). When the target is a topmost window (such as the taskbar), the ghost also becomes topmost and is placed directly below the target among the topmost windows. If a ghost configured to “always stay on top” sits behind a window that is not topmost, that setting takes precedence, so the ghost remains topmost and the request to sit behind the target has no effect.
- To sit just above the taskbar without following a window, fix the ghost to the screen with `--target=fix` and use the bottom edge of the work area (for example, `--target=fix,--origin=bl,--area=workarea,--side=center`. Use `--origin=br` for the right edge). The work area excludes the taskbar and similar items, so the ghost sits just above the taskbar only when it is at the bottom of the screen. When the taskbar is at the top or sides of the screen, the ghost sits at the bottom edge of the screen (the bottom edge of the work area). If the taskbar is set to hide automatically, the work area is the entire screen, so the ghost sits at the bottom edge of the screen.
- osuwari stops if another alignment (`top`, `bottom`, `left`, `right`, `free`) is specified, the shell is changed, and so on. `default` restores the ghost's default setting (`descript.txt`; see below). It stops in window mode and resumes when returning to normal mode.
- The position while sitting is not saved as the standing position.
- Of the windows linked by sticky window, the side that is not the parent (the linked child) follows the parent, so specifying osuwari has no effect on it. When the parent sits, the child moves with it.
- `\0` and `\1` can be specified separately. However, since the Z-order of the ghost window is shared by the entire ghost, when multiple characters sit on targets, the target for the character with the smallest number determines it.

## How to specify the origin \[SSP 2.9.34\]

`--origin=` aligns a point on the ghost window with a point on the target rectangle. Use the form `horizontal.vertical`; the part before `.` specifies the X axis, and the part after it specifies the Y axis. The following terms can be used (case-insensitive).

| Term | Point on the ghost window | Point on the target rectangle (when `--target-origin=` is omitted) |
|---|---|---|
| `left` (for X) / `top` (for Y) | Left edge / top edge | Left edge / top edge |
| `right` (for X) / `bottom` (for Y) | Right edge / bottom edge | Right edge / bottom edge |
| `center` | Center | Center |
| `base` | Surface base position (`point.basepos.x` and `point.basepos.y`; defaults to the bottom center) | Center |
| `osuwari` | Surface sitting position (`point.osuwaripos.x` and `point.osuwaripos.y`; defaults to the same as `base`) | Center |

- If `base` or `osuwari` is specified as a single term without `.`, it applies to both the X and Y axes (`--origin=osuwari` is equivalent to `osuwari.osuwari`). Any other single term specifies only the X axis, with `top` used for the Y axis.
- `tl` is equivalent to `left.top`, `tr` to `right.top`, `bl` to `left.bottom`, and `br` to `right.bottom`.
- Unrecognized specifications are ignored (the origin does not change).
- The target rectangle has no `base` or `osuwari` point, so its center is used when `--target-origin=` is omitted. For example, the default `--origin=osuwari` places the ghost’s sitting position at the center of the target rectangle. To move the sitting position, use `--x=` and `--y=`, or change the point on the target side with `--target-origin=`.
- Example: `--origin=center.bottom` aligns the ghost’s center (X) and bottom edge (Y) with the target’s center (X) and bottom edge (Y). `--origin=right.osuwari` aligns the ghost’s right edge (X) and `point.osuwaripos.y` (Y) with the target’s right edge (X) and center (Y).

## Point on the target rectangle \[SSP 2.9.34\]

`--target-origin=` specifies the point on the target rectangle to which a point on the ghost window is aligned. Its format is the same as `--origin=` (`horizontal.vertical`, `tl` `tr` `bl` `br`, or a single term), and the available terms are only `left` `right` `top` `bottom` and `center`. The target rectangle has no `base` or `osuwari` point, so those terms are ignored as unrecognized specifications.

- If omitted, the point is on the same side as the point specified by `--origin=`. `left` and `top` mean the left and top edges, `right` and `bottom` mean the right and bottom edges, and `center` `base` and `osuwari` mean the center (the right-hand column in the table above).
- A single term specifies only the X axis, with `top` used for the Y axis. `--target-origin=center` is equivalent to `center.top` (the center of the target’s top edge).
- Unrecognized specifications are ignored (the point on the target rectangle does not change).
- When the object to sit on is the reference rectangle (when sitting is not possible), the point is on the reference rectangle (including the virtual window).
- Example: `--origin=osuwari --target-origin=center.top` aligns the surface sitting position with the center of the target’s top edge. `--origin=center.bottom --target-origin=center.top` aligns the ghost’s center (X) and bottom edge (Y) with the target’s center (X) and top edge (Y). The ghost’s feet rest on the target’s top edge, regardless of the ghost’s height.
- The built-in SAORI `osuwari` (compatible with Osuwari.dll) has no corresponding argument. As before, it aligns the same corners of the ghost and the target.

## Surface sitting position \[SSP 2.9.34\]

You can specify the sitting position with `point.osuwaripos.x` and `point.osuwaripos.y` in a surface brace in the shell’s `surfaces.txt` ([point.osuwaripos.x](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.x.md)・[point.osuwaripos.y](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.y.md)). These are the points used by `osuwari` in `--origin=`; if omitted, they are the same as `point.basepos.x` and `point.basepos.y` (or their defaults, if those are also omitted).

For example, to place the sitting position at the waist on a surface 200 pixels wide and 300 pixels high, write:

```
surface0
{
point.osuwaripos.x,100
point.osuwaripos.y,250
}
```

This position is measured in pixels from the top-left of the surface, and scales with the surface. It is a separate point from the base position at the feet (`point.basepos`; defaults to the bottom center (100,300) if omitted). `--origin=base` uses the base position, and `--origin=osuwari` uses the sitting position.

## Positioning examples

The following example shows the surface above sitting on a window whose top-left is (400,400) and bottom-right is (1000,900). `--origin=osuwari --target-origin=center.top` places the ghost’s sitting position at the center of the target’s top edge.

![Position of the ghost window relative to the target when sitting with --origin=osuwari --target-origin=center.top](../../../assets/image/osuwari-origin.svg)

The sitting position (100,250) is aligned with the center of the target’s top edge (700,400), so the ghost’s top-left is (700−100,400−250)=(600,150). The base position at the feet (the bottom center by default) is 50 pixels below the sitting position, at (700,450), inside the top edge of the window. Since the ghost is displayed in front of the target, it appears to be sitting on the window’s edge.

- If you specify `point.osuwaripos` for each surface, the ghost will reposition itself so the sitting position rests on the edge when the surface changes.
- If `--target-origin=` is omitted, the sitting position is aligned with the center of the target. To make the ghost sit on an edge, specify a point on the target side, such as `--target-origin=center.top`.
- You can also align using a corner or edge of the ghost without using the sitting position. `--origin=center.bottom --target-origin=center.top` aligns the center of the ghost’s bottom edge with the center of the target’s top edge (so the feet rest on it).
- If `--target-origin=` is omitted, the point on the target side is always on the same side as the ghost’s point, so you cannot specify a combination that aligns the bottom edge with the top edge. In that case, align the top edges and offset the ghost, as in `--origin=tr --y=-300`. This offset is based on the ghost’s height, so the feet will shift if its height changes.

## When it cannot sit or overflows

When it cannot sit on the target, or sitting on it would cause it to overflow, it sits on the reference rectangle instead of the target. The reference rectangle is created in the following order.

1. Use `--area=` to choose either the entire monitor containing the target (`desktop`) or its work area (`workarea`). If there is no target, use the monitor containing the ghost window (or, while dragging, the monitor containing the cursor).
2. Use `--side=` to choose whether to use 1 as is (`center`) or use a virtual window placed outside it (`top` `left` `right` `bottom`). The virtual window has the same length as the corresponding edge of the reference rectangle and is 100 pixels thick.

![Relationship between the virtual window created by --side= and the reference rectangle](../../../assets/image/osuwari-side.svg)

When `bottom` is selected, the top edge of the virtual window overlaps the bottom edge of the reference rectangle. Combined with `--origin=osuwari --target-origin=center.top`, the sitting position rests at the center of the reference rectangle’s bottom edge (or, for the work area, sits on the top edge of the taskbar). With `--origin=center.bottom --target-origin=center.top`, the bottom edge of the ghost rests there, with its feet standing on the bottom edge of the reference rectangle.

When sitting on the reference rectangle, `--origin=`, `--target-origin=`, `--x=` and `--y=` work just as they do when sitting on a target.

!!! note "Note"
    If you leave `--side=center` (the default) with `--origin=osuwari --target-origin=center.top`, when it falls onto the reference rectangle it sits at the center of the top edge of the reference rectangle (the entire work area). The sitting position (100,250) overlaps (960,0), so the ghost’s top-left corner is at (860,-250), leaving most of it off screen. After it falls onto the reference rectangle, clipping is not checked, so it is not pulled back. To make it sit at the bottom edge of the screen, combine this with `--side=bottom`.

**Clipping check** determines whether the entire ghost window, including transparent areas, fits inside the rectangle enclosing all monitors.

- `--margin=` is the amount by which to expand that rectangle outward. With `--margin=0_0_100_0`, it is not considered clipped until it overflows 100 pixels to the right. Use this when the transparent margins of a surface extending off screen would otherwise trigger clipping.
- `--noclip` disables the clipping check entirely. Depending on the target’s position, the ghost may remain off screen.
- No clipping check is performed when `--target=fix` is specified or when there is no target (it is already sitting on the reference rectangle).

## Range of movement by dragging

By default, dragging the ghost window cannot move it from its sitting position. `--xmove` allows dragging horizontally, and `--ymove` allows dragging vertically. In a direction that is not specified, it returns to its sitting position when moved.

It can only move within the rectangle of the object it is sitting on.

- `--xmove`: the left edge of the ghost window must be at or to the right of the object’s left edge, and its right edge must be at or to the left of the object’s right edge.
- `--ymove`: the top edge of the ghost window must be at or below the object’s top edge, and its bottom edge must be at or above the object’s bottom edge.

The object it sits on is the target when it is sitting on a target, and the reference rectangle (including the virtual window) when it is not sitting on a target (`--target=fix` or after falling onto the reference rectangle). For example, `--target=fix --origin=bl --xmove` stands at the bottom edge of the work area and can move only horizontally.

The moved position is remembered separately for each direction as a ratio within the range of movement. A ratio of 0 means the position where the left edge (top edge) of the ghost window overlaps the object’s left edge (top edge); a ratio of 1 means the position where its right edge (bottom edge) overlaps the object’s right edge (bottom edge).

- Until it is moved, it sits at the position determined by `--origin=`, `--target-origin=`, `--x=` and `--y=`. These are the defaults for sitting.
- Once it is moved, the ratio takes precedence in that direction, and `--origin=` and the other options are not used. It sits at the same relative position even if the object’s size or the ghost window’s size changes. The same applies when changing the target or switching surfaces.
- The ratio is updated only when the ghost window is moved from its previous placement (by dragging or `\![move]`). It is not updated just because the target moves or changes size.
- In directions where it cannot move, its position is still determined by the origin, the point on the target, and the offset.
- Specifying `osuwari` again clears the remembered ratio and restores the default.
- Since the range of movement is only within the object, once it has been moved it cannot return to a position shifted outside the object (such as sitting on the target’s top edge). To return to that position, specify `osuwari` again.
- If the ghost window is larger than the object (the range of movement is 0 or less), no ratio can be determined. Moving it does not store a ratio; if a ratio is already remembered, it sits aligned with the object’s left edge (top edge). If it has not yet been moved, it stays at the default position.

For example, when the target has top-left (300,400) and bottom-right (1100,1000), the ghost window is 200 pixels wide and 300 pixels high, and `--origin=tl --xmove` is specified, the initial top-left position is (300,400).

- Dragging the left edge to 600 (the range is 300 to 900, so this is the midpoint) sets the ratio to 0.5.
- When the target’s width becomes 600 (top-left (300,400), bottom-right (900,1000)), the range is 300 to 700, and the left edge is at 500.
- When another window (top-left (1000,100), bottom-right (1400,800)) comes to the front, the range is 1000 to 1200, and the left edge is at 1100.

## Stacking order

While sitting, the ghost window maintains its stacking order relative to the target. Use `--zorder=` to choose whether it appears in front of the target or directly behind it. This does not affect position calculations.

![Stacking order of the ghost window and target with --zorder=front and --zorder=back](../../../assets/image/osuwari-zorder.svg)

- `front`: Move the ghost directly above the target only if it is behind the target. If it is already in front of the target, do not move it (the same applies if another window is between them; this prevents ghosts sitting on the same window from competing over their stacking order).
- `back`: Keep it directly behind the target. If a visible window from another application gets between them, move it back directly behind the target at the next position check (at the `--interval=` interval).

For cases where the target is the frontmost window (such as the taskbar), and for ghosts with the “Always on top” setting, see the notes in “Options”.

## Numerical examples

The following shows where the top-left corner of the ghost window will be under these conditions.

- Ghost window: width 200, height 300. The surface reference position is the default bottom center (100,300). The sitting position is specified in `surfaces.txt` as `point.osuwaripos.x,100` and `point.osuwaripos.y,250` (100,250).
- Screen: 1920×1080. Work area: 1920×1040 (the taskbar is at the bottom and is 40 pixels high).
- Target: top-left (400,400), bottom-right (1000,900), unless otherwise noted.

The values for specifications that omit `--origin=` and `--area=` use the defaults (`osuwari` and `workarea`) from SSP 2.9.34 onward. In 2.9.33, the defaults are `tl` and `desktop`, so the results differ.

| Specification | Top-left | Description |
|---|---|---|
| `--origin=osuwari` (default) | (600,400) | The sitting position (100,250) overlaps the center of the target (700,650). |
| `--origin=osuwari --target-origin=center.top` | (600,150) | The sitting position overlaps the center of the target's top edge (700,400). The ghost sits on the window's edge (diagram above). |
| `--origin=tr --x=-20 --y=-300` | (780,100) | Align the top-right corner with the target's top-right corner, then move 20 pixels left and 300 pixels up. The bottom edge (400) overlaps the target's top edge, so the ghost stands on the window's top edge. |
| `--origin=bl` | (400,600) | Align the bottom-left corner with the target's bottom-left corner. The bottom edge (900) overlaps the target's bottom edge. |
| `--origin=center.bottom --target-origin=center.top` | (600,100) | Align the center of the ghost's bottom edge with the center of the target's top edge (700,400). The ghost stands on the top edge of the window, regardless of its height. |
| `--target=fix --origin=osuwari --target-origin=center.top --side=bottom` | (860,790) | Align the sitting position with the center of the top edge (960,1040) of the virtual window below the work area. The ghost sits on the edge at the bottom of the work area. |
| `--target=fix --origin=center.bottom --target-origin=center.top --side=bottom` | (860,740) | Align the center of the ghost's bottom edge with the same point. The ghost stands at the bottom of the work area. |
| With the specification from row 3, the target is maximized (top-left (0,0), bottom-right (1920,1040)). Add `--side=bottom` | (1700,740) | The top edge would be outside the screen (-300), so the ghost would be clipped. It moves to the virtual window below the work area and sits there using the same `--origin=`, `--x=`, and `--y=` values. Its bottom edge is at 1040 (the bottom of the work area). |
| Omit `--side=bottom` from the row above | (1700,-300) | The ghost moves to the work area itself. Clipping is not checked, so it sits outside the screen. |
| `--target=fix --origin=bl` | (0,740) | The ghost stands at the bottom-left of the work area. With `--origin=br`, it would be at (1720,740). |
| `--target=fix` | (860,270) | The sitting position overlaps the center of the work area (960,520). |
| Target is (1500,400)-(2000,900). `--origin=tr --y=-300 --side=bottom` | (1720,740) | The right edge, 2000, exceeds the screen's right edge at 1920, so the ghost would be clipped. It moves to the virtual window below the work area. |
| Add `--margin=0_0_100_0` or `--noclip` to the row above | (1800,100) | The ghost stays seated on the target because 100 pixels of overflow to the right are allowed (or clipping is not checked). |

## Write in descript.txt

You can also specify `osuwari` as the value of `seriko.alignmenttodesktop` in the ghost's or shell's `descript.txt` (including entries prefixed with `sakura.`, `kero.`, or `char*.`). After the value, list the same `--` options as for the tag, separated by commas ([※display position information](../../../descript/ghost/descript-txt/note-1.md#補足)).

```
sakura.seriko.alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom
```

- The priority is the same as for other values (ghost-wide < ghost scope-specific < shell-wide < shell scope-specific).
- On ghost startup or when switching shells, tracking starts with those settings.
- `\![set,alignmenttodesktop,default]` and `STOP` for the built-in SAORI `osuwari` restore the settings from `descript.txt`. If `descript.txt` specifies osuwari, the ghost sits down in the osuwari position again.
- Unrecognized options are ignored and a warning is written to the error log.

## Relationship with the built-in SAORI

The built-in SAORI `osuwari` (compatible with Osuwari.dll) performs the same operation. However, in accordance with the original, if the seventh and subsequent arguments to SAORI's `START` are omitted, their previous values are retained ([compatibility module](../../../spec/saori-ex/compat.md)).

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
