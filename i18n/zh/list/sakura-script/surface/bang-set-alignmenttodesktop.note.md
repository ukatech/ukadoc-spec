# About `\![set,alignmenttodesktop,osuwari]`

`\![set,alignmenttodesktop,osuwari,オプション,…]` \[SSP 2.9.33\]

“Seat,” “stick,” or “hang” the ghost window on a corner or edge of another window. This is the same operation as ukiya's SAORI “Osuwari.dll,” built into SSP, and its options correspond to that implementation. There is no need to write `seriko.alignmenttodesktop,free` in the shell's `descript.txt` (`osuwari` itself specifies the alignment when selected).

## How it works

osuwari repeats the following at regular intervals:

> Where on the screen should the top-left corner of the ghost window be placed?

The answer is determined by “which window,” “which point on it,” “which point of the ghost window,” and “how many pixels to offset.” The elements are as follows.

- **Ghost window**: The window for each character (`\0`・`\1`…). Its size is the same as the image of the surface currently displayed, including transparent areas. Its position is represented by the top-left coordinates. When the surface changes and its size changes, the positions of its right edge, bottom edge, and center also change.
- **Target**: The window the ghost sits on. It is measured using the visible frame (excluding invisible frames such as shadows).
- **Reference rectangle**: The rectangle the ghost sits on instead of the target when it cannot sit on the target or when sitting on it would extend off the screen. This is either the entire monitor containing the target or its work area, determined by `--area=` and `--side=`.
- **Origin**: The pair of points specifying “which point of the ghost window to align with which point of the target rectangle.” Set the point on the ghost window with `--origin=` and the point on the target rectangle with `--target-origin=`.
- **Offset**: The displacement from the aligned position. Set it with `--x=` and `--y=` (right and down are positive).

The position is calculated separately for the X and Y axes using the following formula.

```
ゴーストのウインドウの左上 = 対象の矩形の点 − ゴーストのウインドウの点 + ずれ
```

The point on the ghost window is set by `--origin=`, and the point on the target rectangle is set by `--target-origin=`. When the ghost sits on a target, the target rectangle is used; when it cannot sit on a target, the reference rectangle is used.

The options corresponding to each setting are as follows.

| Setting | Option |
|---|---|
| Which window to sit on | `--target=` |
| Which point of the ghost window to align | `--origin=` |
| Which point of the target rectangle to align with | `--target-origin=` |
| How much to offset from there | `--x=` `--y=` |
| Where to sit when unable to sit on the target or when extending off screen | `--area=` `--side=` `--margin=` `--noclip` |
| Range in which dragging is allowed | `--xmove` `--ymove` |
| Whether to be in front of or behind the target | `--zorder=` |
| How often to follow the target | `--interval=` |

## How the position is determined

The position is determined in the following order at each `--interval=` interval. However, it is not recalculated if the target, target rectangle, ghost window rectangle, surface's reference position, and sitting position are all unchanged since the previous check.

1. Find the target (`--target=`).
   - `active`: The foreground window. If a window that cannot be sat on (see below) is in the foreground, use the window the ghost was sitting on immediately before. If there is no previously usable window, there is no target.
   - `@string`: Among the windows whose titles contain the string, use one the ghost can sit on. If there are multiple, use the one closest to the front in Z-order.
   - `#number`: The window whose window handle is the number (in decimal). If the ghost cannot sit on it, there is no target.
   - `fix`: There is no target.
2. Determine the rectangle to sit on. If there is a target and the ghost can sit on it, use the target rectangle. If there is no target, use the reference rectangle (`--area=` and `--side=`).
3. Overlay the two points selected by `--origin=` (the point on the ghost window) and `--target-origin=` (the point on the target rectangle) to find the top-left corner of the ghost window. Add `--x=` and `--y=` to that position.
4. In the directions specified by `--xmove` and `--ymove`, if the ghost window has been moved from its previous position (such as by dragging), constrain that position to within the target and remember it as a ratio within the movable range. If a ratio has been remembered, use the position at that ratio within the target rectangle instead of the position calculated in step 3 ([range in which dragging is allowed](bang-set-alignmenttodesktop.note.md#ドラッグで動かせる範囲)).
5. Check whether the ghost window extends off the screen (clipping check). If it does, replace the target in step 2 with the reference rectangle and repeat steps 3–4 once. Do not check again after repeating. Skip the check when `--target=fix`, when `--noclip` is specified, or when there is no target.
6. Move the ghost window to the calculated position and adjust its stacking order (`--zorder=`).

The same values for the two points selected in step 3 and the offset are used when repeating steps 3–4 in step 5. Only the rectangle the ghost sits on changes.

## Options

Options use the form `--name=value` and can all be omitted. Omitted options take their default values, not the values specified in the previous call. Options that cannot be interpreted are ignored.

| Option | Default | Description |
|---|---|---|
| `--target=` | `active` | Target to follow. `active`: foreground window / `fix`: fixed to the screen (work area) / `@string`: window whose title contains the string (case-insensitive) / `#number`: window whose window handle is the number |
| `--origin=` | `osuwari` | Which point of the ghost window to align with the target (origin). Write it in the form `左右.上下` (see “How to write the origin” below). You can also write a corner as two characters, such as `tl`, `tr`, `bl`, or `br` |
| `--target-origin=` | Omitted (automatic) | \[SSP 2.9.34\] Which point of the target rectangle to align with the point on the ghost window. The format is the same as for `--origin=`, but `base` and `osuwari` cannot be used (see “Points on the target rectangle” below). If omitted, uses the same side as the point specified by `--origin=` (`left` is the left edge, `right` is the right edge, and `center`, `base`, and `osuwari` are the center) |
| `--x=` `--y=` | `0` | Offset from the origin (pixels). In directions where `--xmove` or `--ymove` is specified, this is the default until the ghost is moved |
| `--interval=` | `100` | Interval for checking the position (milliseconds). Values below 10 are treated as 10 |
| `--xmove` `--ymove` | None | Allow dragging in that direction (up to the inside of the target rectangle). The moved position is remembered as a ratio within the movable range (see “Range in which dragging is allowed” below). In a direction not specified, the ghost returns to its sitting position even if dragged. Can also be written as `--xmove=false` |
| `--noclip` | None | Do not perform the clipping check |
| `--area=` | `workarea` | Reference area when unable to sit on the target or when clipped. `desktop`: entire screen / `workarea`: work area (the area excluding the taskbar and similar elements) |
| `--side=` | `center` | Where to place a “virtual window” relative to the reference area when unable to sit on the target or when clipped. `center`: the reference area itself / `top`, `left`, `right`, `bottom`: place a virtual window 100 pixels thick above, to the left, to the right, or below the reference area |
| `--margin=` | `0_0_0_0` | Tolerance for the clipping check (pixels). In the order `左_上_右_下`, separated by spaces or `_`. With `0_50_0_100`, the ghost is not considered clipped until it extends 50 pixels above or 100 pixels below |
| `--zorder=` | `front` | Stacking order relative to the target window. `front`: display immediately above (in front of) the target / `back`: display immediately behind (directly below) the target. Has no effect while not sitting on a target (when unable to sit on a target or with `--target=fix`) |

- The defaults for `--origin=` and `--area=` are `osuwari` and `workarea` for the tag and `descript.txt`. The built-in SAORI `osuwari` (compatible with Osuwari.dll) retains `tl` and `desktop` to match the original. \[SSP 2.9.34\] In 2.9.33, `tl` and `desktop` were also the defaults for the tag and `descript.txt`.
- When the ghost cannot sit on the target (with `--target=fix`, when there is no target window, or when the foreground window cannot be sat on and there is also no previously usable window), or when clipped (sitting there as-is would extend off the screen), the ghost sits on the reference rectangle determined by `--area` and `--side`, treating it as a “virtual target.” With `--target=fix`, no clipping check is performed.
- Window rectangles are measured using the visible frame (not including the invisible frame on Windows 10 and later). The reference screen is the monitor containing the target window (or the monitor containing the ghost when there is no target; while dragging, the monitor containing the cursor). Clipping is checked against the combined area of all monitors.
- The ghost cannot sit on minimized or hidden windows, windows on another virtual desktop, owned windows such as dialogs, or SSP's own windows (when `--target=active`). With `--target=active`, it also cannot sit on shell windows that are clearly unsuitable targets (the desktop, Alt+Tab and Task View, UWP windows displayed by the shell such as Start, Search, and IME panels, and full-screen Metro windows in Windows 8). When one of these windows is in the foreground, the ghost continues sitting on the window it could sit on immediately before. Windows explicitly specified with `@string` or `#number` are not subject to these exclusions.
- While sitting on a target, the ghost is displayed above the target window. osuwari makes the ghost topmost (always displayed in front of other windows) only when the target is a topmost window (such as the taskbar); otherwise, the ghost does not become topmost. However, a ghost with the “always on top” setting remains topmost because of that setting, regardless of the target. Even when the target is a topmost window, the ghost is displayed above it (whenever the target comes to the foreground, the ghost is brought above it as well).
- With `--zorder=back`, the ghost is displayed immediately behind the target window (directly below it in Z-order). This allows uses such as peeking out from a position hidden by the target. Even if another application's window gets between them, the ghost returns immediately behind the target at the next position check (at each `--interval=` interval). When the target is a topmost window (such as the taskbar), the ghost also becomes topmost and is placed directly below the target among topmost windows. A ghost with the “always on top” setting remains topmost when sitting behind a window that is not topmost (the setting takes precedence, so the behind setting has no effect).
- To sit immediately above the taskbar without following a window, fix the ghost to the screen with `--target=fix` and use the bottom edge of the work area (for example: `--target=fix,--origin=bl,--area=workarea,--side=center`. For the right edge, use `--origin=br`). Since the work area excludes the taskbar and similar elements, the ghost sits immediately above the taskbar only when the taskbar is at the bottom of the screen. If the taskbar is at the top or sides of the screen, the ghost sits at the bottom edge of the screen (the bottom edge of the work area). When the taskbar is set to hide automatically, the work area is the entire screen, so the ghost sits at the bottom edge of the screen.
- osuwari stops when another alignment (`top`, `bottom`, `left`, `right`, `free`) is specified, the shell is changed, or similar actions occur. `default` returns to the ghost's default settings (`descript.txt`; see below). It stops while in window mode and resumes when returning to normal mode.
- The position while sitting is not saved as the standing position.
- Of the windows linked by a sticky window, osuwari has no effect when specified for the side that is not the parent (the linked child), because it follows the parent. When the parent sits, the child moves with it.
- `\0` and `\1` can be specified separately. However, stacking order for the ghost window is set once per ghost, so when multiple characters sit on targets, the target for the character with the lower number determines the order.

## 原点的写法 \[SSP 2.9.34\]

`--origin=`将ghost窗口上的点对齐到目标矩形上的点。格式为`左右.上下`，`.`前面是X轴，后面是Y轴。每个轴都可以填写以下词语（不区分大小写）。

| 词语 | ghost窗口上的点 | 目标矩形上的点（省略`--target-origin=`时） |
|---|---|---|
| `left`（X轴时）/ `top`（Y轴时） | 左端 / 上端 | 左端 / 上端 |
| `right`（X轴时）/ `bottom`（Y轴时） | 右端 / 下端 | 右端 / 下端 |
| `center` | 中央 | 中央 |
| `base` | surface的基准位置（`point.basepos.x`・`point.basepos.y`。默认是脚下中央） | 中央 |
| `osuwari` | surface的坐下位置（`point.osuwaripos.x`・`point.osuwaripos.y`。默认与`base`相同） | 中央 |

- 只填写`base`或`osuwari`一个词且不带`.`时，会同时应用于X轴和Y轴（`--origin=osuwari`等同于`osuwari.osuwari`）。只填写其他词语时，只指定X轴，Y轴为`top`。
- `tl`等同于`left.top`，`tr`等同于`right.top`，`bl`等同于`left.bottom`，`br`等同于`right.bottom`。
- 无法解析的写法会被忽略（原点不变）。
- 目标矩形一侧没有`base`和`osuwari`，因此省略`--target-origin=`时会使用中央。例如，默认的`--origin=osuwari`会将ghost的坐下位置放到目标矩形的中央。可以用`--x=`和`--y=`移动坐下位置，或通过`--target-origin=`更改目标一侧的点。
- 例如：`--origin=center.bottom`会将ghost的中央（X轴）和下端（Y轴）分别对齐到目标的中央（X轴）和下端（Y轴）。`--origin=right.osuwari`会将ghost的右端（X轴）和`point.osuwaripos.y`（Y轴）分别对齐到目标的右端（X轴）和中央（Y轴）。

## 目标矩形上的点 \[SSP 2.9.34\]

`--target-origin=`用于指定目标矩形一侧的点，ghost窗口上的点将与之重合。格式与`--origin=`相同（`左右.上下`・`tl` `tr` `bl` `br`・一个词），可填写的词语只有`left` `right` `top` `bottom` `center`。目标矩形没有`base`和`osuwari`，因此填写这些词语时会被视为无法解析的写法并忽略。

- 省略时，目标矩形上的点会与`--origin=`指定的点处于同一侧。`left`・`top`对应左端・上端，`right`・`bottom`对应右端・下端，`center`・`base`・`osuwari`对应中央（见上表右列）。
- 只填写一个词时，只指定X轴，Y轴为`top`。`--target-origin=center`等同于`center.top`（目标上端的中央）。
- 无法解析的写法会被忽略（目标矩形上的点不变）。
- 当坐下的对象是基准矩形（无法坐下时）时，使用基准矩形（包括虚拟窗口）上的点。
- 例如：`--origin=osuwari --target-origin=center.top`会将surface的坐下位置对齐到目标上端的中央。`--origin=center.bottom --target-origin=center.top`会将ghost的中央（X轴）和下端（Y轴）分别对齐到目标的中央（X轴）和上端（Y轴）。这样ghost的脚下会落在目标上端，不受ghost高度影响。
- 内置SAORI的`osuwari`（兼容Osuwari.dll）没有与此对应的参数。与以往一样，它会将ghost的角与目标的同一角对齐。

## surface的坐下位置 \[SSP 2.9.34\]

可以在shell的`surfaces.txt`中的surface块内，通过`point.osuwaripos.x`・`point.osuwaripos.y`指定坐下位置（[point.osuwaripos.x](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.x.md)・[point.osuwaripos.y](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.y.md)）。这是`--origin=`的`osuwari`所使用的点；如果未填写，则与`point.basepos.x`・`point.basepos.y`（若未填写，则使用各自的默认值）相同。

例如，要在宽200、高300的surface上将坐下位置设在腰部，可以这样写。

```
surface0
{
point.osuwaripos.x,100
point.osuwaripos.y,250
}
```

该位置是从surface左上角开始测量的像素坐标，并会随surface的缩放而缩放。它与脚下的基准位置（`point.basepos`；未填写时为下端中央(100,300)）是不同的点；`--origin=base`使用基准位置，`--origin=osuwari`使用坐下位置。

## 位置对齐示例

下面示例展示上述surface坐在左上角为(400,400)、右下角为(1000,900)的窗口上。`--origin=osuwari --target-origin=center.top`会将ghost的坐下位置与目标上端的中央重合。

![使用 --origin=osuwari --target-origin=center.top 坐下时，ghost窗口与目标的位置关系](../../../assets/image/osuwari-origin.svg)

坐下位置(100,250)与目标上端的中央(700,400)重合，因此ghost的左上角为(700−100,400−250)=(600,150)。脚下的基准位置（默认为下端中央）在坐下位置下方50像素处，即(700,450)，位于窗口上端以内。ghost显示在目标前方，因此看起来就像坐在窗口边缘上。

- 如果为每个surface都填写`point.osuwaripos`，切换surface时也会重新调整坐姿，使坐下位置落在边缘上。
- 省略`--target-origin=`时，坐下位置会与目标中央重合。要让ghost坐在边缘上，应像`--target-origin=center.top`这样指定目标一侧的点。
- 也可以不使用坐下位置，而通过ghost的角或边进行对齐。`--origin=center.bottom --target-origin=center.top`会将ghost下端的中央对齐到目标上端的中央（脚下会落在目标上）。
- 省略`--target-origin=`时，目标一侧的点始终与ghost一侧相同，因此无法通过这种组合将下端对齐到上端。这种情况下，可以使用`--origin=tr --y=-300`，像这样对齐两个上端并移动位置。这个偏移值是根据ghost的高度设置的，因此高度变化时脚下的位置也会偏移。

## 无法坐下或坐下后超出范围时

无法坐在目标上，或坐下后超出范围时，会改为坐在基准矩形上。基准矩形按以下顺序确定。

1. 使用`--area=`选择目标所在显示器的整个区域（`desktop`）或工作区（`workarea`）。没有目标时，使用有 ghost 窗口的显示器（拖动期间使用光标所在的显示器）。
2. 使用`--side=`选择直接使用第 1 步确定的区域（`center`），还是使用放在其外侧的虚拟窗口（`top` `left` `right` `bottom`）。虚拟窗口与基准边等长，厚度为 100 像素。

![--side=创建的虚拟窗口与基准矩形的位置关系](../../../assets/image/osuwari-side.svg)

选择`bottom`时，虚拟窗口的上边缘与基准矩形的下边缘重合。再配合`--origin=osuwari --target-origin=center.top`，坐下位置就会落在基准矩形下边缘的中央（如果是工作区，则会坐在任务栏的上边缘）。使用`--origin=center.bottom --target-origin=center.top`时，ghost 的下边缘会落在该处，脚下会立在基准矩形的下边缘上。

坐在基准矩形上时，`--origin=`、`--target-origin=`、`--x=`和`--y=`的用法与坐在目标上时相同。

!!! note "注"
    如果保持`--side=center`（默认值），并设置`--origin=osuwari --target-origin=center.top`，落到基准矩形上时，就会坐在基准矩形（整个工作区）上边缘的中央。坐下位置(100,250)与(960,0)重合，因此 ghost 的左上角会在(860,-250)，大部分会出现在屏幕外。落到基准矩形上后不会进行超出范围检测，因此不会被拉回。要让 ghost 坐在屏幕下边缘，请同时使用`--side=bottom`。

**超出范围检测**会检查 ghost 窗口整体（包括透明部分）是否位于包围所有显示器的矩形内。

- `--margin=`用于向外扩展该矩形。使用`--margin=0_0_100_0`时，向右超出 100 像素以内都不会被视为超出范围。适用于仅因 surface 的透明留白伸出屏幕就被判定为超出范围的情况。
- `--noclip`表示不进行超出范围检测。根据目标的位置，ghost 可能会停留在屏幕外。
- 使用`--target=fix`时，以及没有目标时，不进行超出范围检测（因为本来就是坐在基准矩形上）。

## 可通过拖动移动的范围

默认情况下，即使拖动 ghost 窗口，也无法将其移出坐下位置。`--xmove`允许横向拖动，`--ymove`允许纵向拖动。未指定的方向即使移动，也会返回坐下位置。

只能在坐下对象的矩形内移动。

- `--xmove`: ghost 窗口的左边缘不得超出对象的左边缘，右边缘不得超出对象的右边缘。
- `--ymove`: ghost 窗口的上边缘不得超出对象的上边缘，下边缘不得超出对象的下边缘。

坐下对象是指坐在目标上时的目标，以及未坐在目标上时（`--target=fix`或落到基准矩形上时）的基准矩形（包括虚拟窗口）。例如，`--target=fix --origin=bl --xmove`会让 ghost 立在工作区下边缘，并且只能横向移动。

移动后的位置会按方向记录为可移动范围内的比例。比例 0 表示 ghost 窗口的左边缘（上边缘）与对象的左边缘（上边缘）重合的位置，比例 1 表示右边缘（下边缘）与对象的右边缘（下边缘）重合的位置。

- 移动之前，坐下位置由`--origin=`、`--target-origin=`、`--x=`和`--y=`决定。这些是坐下时的默认位置。
- 移动一次后，该方向会优先采用比例，不再使用`--origin=`等参数。即使对象大小或 ghost 窗口大小发生变化，坐下位置仍保持相同比例。更换目标或切换 surface 时也一样。
- 只有 ghost 窗口从上一次的摆放位置被移动时（例如拖动或使用`\![move]`），才会更新比例。仅仅是对象移动或大小改变时，不会更新比例。
- 对于无法移动的方向，位置仍由原点、对象一侧的点和偏移量决定。
- 重新指定`osuwari`时，已记录的比例会清除，并恢复为默认值。
- 可移动范围仅限于对象内部，因此移动一次后，就无法回到对象外的位置（例如坐在目标上边缘的位置）。要回到该位置，请重新指定`osuwari`。
- ghost 窗口比对象大时（可移动范围小于或等于 0），无法确定比例。移动时不会记录比例；如果已有记录的比例，就会对齐对象的左边缘（上边缘）坐下。如果还没有移动过，则保持默认位置。

例如，目标的左上角为(300,400)、右下角为(1100,1000)，ghost 窗口宽 200、高 300，且指定了`--origin=tl --xmove`时，初始左上角为(300,400)。

- 将左边缘拖到 600 后（范围为 300 到 900，位于正中间），比例为 0.5。
- 目标宽度变为 600（左上角(300,400)、右下角(900,1000)）后，范围变为 300 到 700，左边缘会变为 500。
- 另一个窗口（左上角(1000,100)、右下角(1400,800)）成为前景窗口后，范围变为 1000 到 1200，左边缘会变为 1100。

## 前后关系

坐着时，ghost 窗口会保持与目标的前后关系。使用`--zorder=`选择显示在目标前方还是紧靠目标后方。这不会影响位置计算。

![--zorder=front 和 --zorder=back 时 ghost 窗口与目标的前后关系](../../../assets/image/osuwari-zorder.svg)

- `front`: 仅当 ghost 位于目标后方时，才将其移到目标正前方。若已在目标前方，则不移动（即使中间隔着另一个窗口也一样。这样可以避免坐在同一窗口上的多个 ghost 争抢排列顺序）。
- `back`: 保持在目标正后方（紧接其后）。如果其他应用的可见窗口插入两者之间，则会在下一次检查位置时（按`--interval=`设定的间隔）移回目标正后方。

如果目标是最前面的窗口（例如任务栏），或者 ghost 启用了“始终显示在前”设置，请参阅“选项”中的补充说明。

## Numerical examples

The following shows where the top-left corner of the ghost window will be under these conditions.

- Ghost window: 200 wide × 300 high. The surface reference position is the default bottom center (100,300). The sitting position is (100,250), specified in `surfaces.txt` as `point.osuwaripos.x,100` and `point.osuwaripos.y,250`.
- Screen: 1920×1080. The work area is 1920×1040 (the taskbar is at the bottom and is 40 pixels high).
- Target: Unless otherwise specified, top-left (400,400) and bottom-right (1000,900).

Values for specifications that omit `--origin=` and `--area=` are calculated using the defaults from SSP 2.9.34 onward (`osuwari` and `workarea`). In 2.9.33, the defaults are `tl` and `desktop`, so the results differ.

| Specification | Top-left | Details |
|---|---|---|
| `--origin=osuwari` (default) | (600,400) | The sitting position (100,250) overlaps the target center (700,650). |
| `--origin=osuwari --target-origin=center.top` | (600,150) | The sitting position overlaps the center of the target's top edge (700,400). The ghost sits on the window's edge (diagram above). |
| `--origin=tr --x=-20 --y=-300` | (780,100) | Align the top-right corner with the target's top-right corner, then move 20 pixels left and 300 pixels up. The bottom edge (400) overlaps the target's top edge, so the ghost stands on the window's top edge. |
| `--origin=bl` | (400,600) | Align the bottom-left corner with the target's bottom-left corner. The bottom edge (900) overlaps the target's bottom edge. |
| `--origin=center.bottom --target-origin=center.top` | (600,100) | Align the bottom center of the ghost with the top center of the target (700,400). The ghost stands on the window's top edge, regardless of its height. |
| `--target=fix --origin=osuwari --target-origin=center.top --side=bottom` | (860,790) | Align the sitting position with the top center (960,1040) of the virtual window below the work area. The ghost sits on the bottom edge of the work area. |
| `--target=fix --origin=center.bottom --target-origin=center.top --side=bottom` | (860,740) | Align the ghost's bottom center with the same point. The ghost stands on the bottom edge of the work area. |
| Using the specification in row 3, with the target maximized (top-left (0,0), bottom-right (1920,1040)). Add `--side=bottom` | (1700,740) | The top edge would be outside the screen (-300), so the ghost is clipped. It falls to the virtual window below the work area and sits there using the same `--origin=`, `--x=` and `--y=`. The bottom edge is at 1040 (the bottom edge of the work area). |
| Remove `--side=bottom` from the row above | (1700,-300) | The ghost falls to the work area itself. Since no clipping check is performed, it sits outside the screen. |
| `--target=fix --origin=bl` | (0,740) | The ghost stands at the bottom-left of the work area. With `--origin=br`, it is at (1720,740). |
| `--target=fix` | (860,270) | The sitting position overlaps the center of the work area (960,520). |
| Target is (1500,400)-(2000,900). `--origin=tr --y=-300 --side=bottom` | (1720,740) | The right edge at 2000 exceeds the right edge of the screen at 1920, so the ghost is clipped. It falls to the virtual window below the work area. |
| Add `--margin=0_0_100_0` or `--noclip` to the row above | (1800,100) | Since an overhang of 100 pixels to the right is allowed (or no check is performed), the ghost stays seated on the target. |

## Specify in descript.txt

You can also specify `osuwari` as the value of `seriko.alignmenttodesktop` in the ghost or shell's `descript.txt` (including entries prefixed with `sakura.`, `kero.` or `char*.`). After the value, list the same `--` options as for the tag, separated by commas ([※ Display position information](../../../descript/ghost/descript-txt/note-1.md#補足)).

```
sakura.seriko.alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom
```

- The priority is the same as for other values (entire ghost < individual ghost scope < entire shell < individual shell scope).
- Tracking starts with these settings when the ghost starts or the shell changes.
- `\![set,alignmenttodesktop,default]` and `STOP` for the built-in SAORI `osuwari` restore the settings from `descript.txt`. If `descript.txt` specifies osuwari, the ghost sits down again using osuwari.
- Unrecognized options are ignored, with a warning written to the error log.

## Relationship to the built-in SAORI

The built-in SAORI `osuwari` (compatible with Osuwari.dll) performs the same processing. However, to match the original, `START` in SAORI carries over the previous values when the seventh and subsequent arguments are omitted ([compatibility module](../../../spec/saori-ex/compat.md)).

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
