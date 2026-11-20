# 关于 `\![set,alignmenttodesktop,osuwari]`

`\![set,alignmenttodesktop,osuwari,オプション,…]` \[SSP 2.9.33\]

让 ghost 的窗口“坐在”“贴在”其他窗口的角落或边缘，或“悬挂”在其上。SSP 内置了与 ukiya 的 SAORI“Osuwari.dll”相同的处理，选项也与其对应。无需在 shell 的 `descript.txt` 中写入 `seriko.alignmenttodesktop,free`（指定 `osuwari` 本身就是一种对齐方式指定）。

## 基本思路

osuwari 每隔一定时间重复确定以下事项。

> 将 ghost 窗口的左上角放在屏幕的什么位置。

答案取决于将“ghost 窗口的哪个点”对齐到“哪个窗口的”“哪个点”，以及“偏移多少像素”。涉及的概念如下。

- **ghost 窗口**: 每个角色（`\0`、`\1`…）各自的窗口。大小与当前显示的 surface 图像相同，包括透明部分。位置用左上角坐标表示。surface 改变导致大小变化时，右边缘、下边缘和中心的位置也会改变。
- **目标**: ghost 要坐的窗口。按可见边框测量（不包括阴影等不可见边框）。
- **基准矩形**: 无法坐在目标上，或坐在目标上会超出屏幕时，代替目标供 ghost 坐的矩形。它是目标所在显示器的整个区域或工作区，由 `--area=` 和 `--side=` 决定。
- **原点**: “将 ghost 窗口的哪个点对齐到目标矩形的哪个点”的组合。ghost 窗口一侧的点由 `--origin=` 决定，目标矩形一侧的点由 `--target-origin=` 决定。
- **偏移**: 相对于对齐位置的偏移量。由 `--x=` 和 `--y=` 决定（向右、向下为正）。

位置的 X 轴和 Y 轴坐标分别按以下公式计算。

```
ゴーストのウインドウの左上 = 対象の矩形の点 − ゴーストのウインドウの点 + ずれ
```

ghost 窗口的点由 `--origin=` 决定，目标矩形的点由 `--target-origin=` 决定。坐在目标上时使用目标矩形，无法坐在目标上时使用基准矩形。

需要确定的事项与选项的对应关系如下。

| 确定的事项 | 选项 |
|---|---|
| 坐在哪个窗口上 | `--target=` |
| 对齐 ghost 窗口的哪个点 | `--origin=` |
| 对齐到目标矩形的哪个点 | `--target-origin=` |
| 从那里偏移多少 | `--x=` `--y=` |
| 无法坐下或超出屏幕时坐在哪里 | `--area=` `--side=` `--margin=` `--noclip` |
| 可通过拖动移动的范围 | `--xmove` `--ymove` |
| 位于目标前方还是后方 | `--zorder=` |
| 追踪的时间间隔 | `--interval=` |

## 位置的确定方式

每隔 `--interval=` 指定的时间，按以下顺序确定位置。但是，如果目标、目标矩形、ghost 窗口矩形、surface 的基准位置和坐下位置均未相对于上次发生变化，则不重新计算。

1. 查找目标（`--target=`）。
   - `active`: 前台窗口。前台是无法坐的窗口（见下文）时，使用上一个可以坐的窗口。如果尚无可以坐的窗口，则没有目标。
   - `@文字列`: 标题包含指定字符串且可以坐的窗口。如果有多个，则使用 Z 顺序中靠前的窗口。
   - `#数値`: 窗口句柄为指定数值（十进制）的窗口。如果无法坐下，则没有目标。
   - `fix`: 始终没有目标。
2. 确定要坐的矩形。有目标且可以坐时使用目标矩形。没有目标时使用基准矩形（`--area=` 和 `--side=`）。
3. 将 `--origin=`（ghost 窗口的点）和 `--target-origin=`（对方矩形的点）选定的两个点重合，求出 ghost 窗口的左上角。再加上 `--x=` 和 `--y=`。
4. 对于指定了 `--xmove`、`--ymove` 的方向，如果 ghost 窗口相对于上次放置结果被移动过（如拖动），则将该位置限制在对方矩形内，并记住其在可移动范围中的比例。如果有已记住的比例，则使用对方矩形中该比例对应的位置，而不是步骤 3 求出的位置（[可通过拖动移动的范围](bang-set-alignmenttodesktop.note.md#ドラッグで動かせる範囲)）。
5. 检查 ghost 窗口是否超出屏幕（越界判定）。如果超出，则将步骤 2 的对象换为基准矩形，仅再重新执行一次步骤 3～4。重新执行后不再检查。`--target=fix`、`--noclip` 或没有目标时不进行检查。
6. 将 ghost 窗口移动到求出的位置，并调整前后顺序（`--zorder=`）。

步骤 5 重新执行时，步骤 3 的两个点的选择和偏移使用相同的值。改变的只有要坐的矩形。

## 选项

选项采用 `--名前=値` 的形式，全部可以省略。省略的选项使用默认值，而不是上次调用时指定的值。无法解析的选项会被忽略。

| 选项 | 默认值 | 内容 |
|---|---|---|
| `--target=` | `active` | 要追踪的目标。`active`: 前台窗口 / `fix`: 固定在屏幕（工作区）上 / `@文字列`: 窗口标题包含指定字符串的窗口（不区分大小写） / `#数値`: 窗口句柄为指定数值的窗口 |
| `--origin=` | `osuwari` | 将 ghost 窗口的哪个点对齐到目标（原点）。以 `左右.上下` 的形式书写（见下方“原点的写法”）。也可以像 `tl` `tr` `bl` `br` 一样用两个字符表示角落 |
| `--target-origin=` | 省略（自动） | \[SSP 2.9.34\] 将 ghost 窗口的点对齐到目标矩形的哪个点。格式与 `--origin=` 相同，但不能使用 `base` 和 `osuwari`（见下方“目标矩形的点”）。省略时，使用与 `--origin=` 的点相同的一侧（`left` 为左边缘，`right` 为右边缘，`center`、`base`、`osuwari` 为中心） |
| `--x=` `--y=` | `0` | 相对于原点的偏移量（像素）。在指定了 `--xmove` `--ymove` 的方向上，这是移动前的默认值 |
| `--interval=` | `100` | 检查位置的间隔（毫秒）。小于 10 时按 10 处理 |
| `--xmove` `--ymove` | 无 | 允许在相应方向上拖动（限于目标矩形内）。移动后的位置按其在可移动范围中的比例记住（见下方“可通过拖动移动的范围”）。未指定的方向上，即使拖动也会返回坐下位置。也可以写成 `--xmove=false` |
| `--noclip` | 无 | 不进行越界判定 |
| `--area=` | `workarea` | 无法坐下或越界时的基准。`desktop`: 整个屏幕 / `workarea`: 工作区（除任务栏等以外的部分） |
| `--side=` | `center` | 无法坐下或越界时，“虚拟窗口”相对于基准的放置位置。`center`: 基准本身 / `top` `left` `right` `bottom`: 在基准的上、左、右、下侧放置厚度为 100 像素的虚拟窗口 |
| `--margin=` | `0_0_0_0` | 越界判定的容差（像素）。按 `左_上_右_下` 的顺序，用空格或 `_` 分隔。`0_50_0_100` 表示向上超出 50 像素、向下超出 100 像素以内均不视为越界 |
| `--zorder=` | `front` | 与目标窗口的前后顺序。`front`: 显示在目标正上方（前方） / `back`: 显示在目标紧后方（正下方）。未坐在目标上时（无法坐下或 `--target=fix`）不进行任何操作 |

- 在标签和 `descript.txt` 中，`--origin=` 和 `--area=` 的默认值分别为 `osuwari` 和 `workarea`。内置 SAORI 的 `osuwari`（兼容 Osuwari.dll）为与原作保持一致，默认值仍为 `tl` 和 `desktop`。\[SSP 2.9.34\] 在 2.9.33 中，标签和 `descript.txt` 的默认值也是 `tl` 和 `desktop`。
- 无法坐在目标上时（`--target=fix`、没有目标窗口，或前台窗口无法坐且此前也没有可以坐的窗口），以及越界时（直接坐下会超出屏幕），会将 `--area` 和 `--side` 决定的基准矩形作为“虚拟目标”坐下。`--target=fix` 不进行越界判定。
- 窗口矩形按可见边框测量（不包括 Windows 10 及以后版本中的不可见边框）。作为基准的屏幕是目标窗口所在的显示器（没有目标时为 ghost 所在的显示器；拖动时为光标所在的显示器）。越界判定使用所有显示器合并后的区域。
- 无法坐在最小化或隐藏的窗口、其他虚拟桌面的窗口、对话框等被拥有的窗口，以及 SSP 自身的窗口（`--target=active` 时）上。`--target=active` 时，也无法坐在明显不应坐的 shell 窗口上（桌面、Alt+Tab 和任务视图、开始菜单、搜索及 IME 面板等由 shell 显示的 UWP 窗口，以及 Windows 8 的 Metro 全屏窗口）。当前台是此类窗口时，继续坐在上一个可以坐的窗口上。通过 `@文字列`、`#数値` 自行指定的窗口不受此排除规则影响。
- 坐下期间，ghost 显示在目标窗口上方。只有当目标是置顶窗口（如任务栏）时，osuwari 才会将 ghost 设为置顶（始终位于其他窗口前方）；否则 ghost 不会置顶。但是，设置了“始终显示在前方”的 ghost 会因该设置而保持置顶，不受目标影响。目标为置顶窗口时，ghost 也会显示在目标上方（每当目标出现在前台，ghost 也会回到其上方）。
- `--zorder=back` 时，ghost 显示在目标窗口的紧后方（Z 顺序中正下方）。可用于从目标遮挡的位置探出头等效果。即使其他应用的窗口插入两者之间，下次检查位置时（按 `--interval=` 的间隔）也会回到紧后方。目标为置顶窗口（如任务栏）时，ghost 也会置顶，并在置顶窗口的顺序中位于目标正下方。设置了“始终显示在前方”的 ghost 坐在非置顶窗口后方时，优先保持该设置并继续置顶（后方指定不生效）。
- 如果只需坐在任务栏正上方（不跟随窗口），可使用 `--target=fix` 固定在屏幕上，并使用工作区的下边缘（例: `--target=fix,--origin=bl,--area=workarea,--side=center`。右边缘使用 `--origin=br`）。由于工作区不包含任务栏等，只有任务栏位于屏幕下方时才会坐在其正上方。任务栏位于屏幕上方或左右两侧时，会坐在屏幕下边缘（工作区下边缘）。设置为自动隐藏任务栏时，工作区为整个屏幕，因此会坐在屏幕下边缘。
- 指定其他对齐方式（`top` `bottom` `left` `right` `free`）、更换 shell 等操作会停止 osuwari。`default` 会恢复 ghost 的默认设置（`descript.txt`，见后文）。窗口模式期间会停止，返回普通模式后恢复。
- 坐下期间的位置不会作为站立位置保存。
- 在通过 sticky window 联动的窗口中，非父窗口的一侧（联动子窗口）会跟随父窗口，因此指定 osuwari 也不生效。父窗口坐下时，子窗口会一起移动。
- `\0` 和 `\1` 可以分别指定。但 ghost 窗口的前后顺序以 ghost 为单位统一确定，因此多个角色坐下时，由编号较小的角色的目标决定。

## 原点的写法 \[SSP 2.9.34\]

`--origin=`将 ghost 窗口上的点与目标矩形上的点对齐。格式为`左右.上下`，`.`前为 X 轴，后为 Y 轴。各轴可使用以下词语（不区分大小写）。

| 词语 | ghost 窗口上的点 | 目标矩形上的点（省略`--target-origin=`时） |
|---|---|---|
| `left`（X 轴时）/ `top`（Y 轴时） | 左端 / 上端 | 左端 / 上端 |
| `right`（X 轴时）/ `bottom`（Y 轴时） | 右端 / 下端 | 右端 / 下端 |
| `center` | 中央 | 中央 |
| `base` | surface 的基准位置（`point.basepos.x`、`point.basepos.y`；默认为脚下中央） | 中央 |
| `osuwari` | surface 的坐姿位置（`point.osuwaripos.x`、`point.osuwaripos.y`；默认与`base`相同） | 中央 |

- `base`和`osuwari`不带`.`、只写一个词时，同时用于 X 轴和 Y 轴（`--origin=osuwari`即`osuwari.osuwari`）。其他词只写一个时，仅指定 X 轴，Y 轴为`top`。
- `tl`与`left.top`相同，`tr`与`right.top`相同，`bl`与`left.bottom`相同，`br`与`right.bottom`相同。
- 无法解析的写法会被忽略（原点不变）。
- 目标矩形侧没有`base`和`osuwari`，因此省略`--target-origin=`时使用中央。例如，默认的`--origin=osuwari`会将 ghost 的坐姿位置对齐到目标矩形的中央。可通过`--x=`和`--y=`偏移坐姿位置，或通过`--target-origin=`更改目标侧的点。
- 例：`--origin=center.bottom`将 ghost 的中央（X）和下端（Y）与目标的中央（X）和下端（Y）对齐。`--origin=right.osuwari`将 ghost 的右端（X）和`point.osuwaripos.y`（Y）与目标的右端（X）和中央（Y）对齐。

## 目标矩形上的点 \[SSP 2.9.34\]

`--target-origin=`决定目标矩形侧与 ghost 窗口上的点重合的点。格式与`--origin=`相同（`左右.上下`、`tl` `tr` `bl` `br`、单个词），但只能使用`left` `right` `top` `bottom` `center`。目标矩形没有`base`和`osuwari`，因此写入时会作为无法解析的写法被忽略。

- 省略时，使用与`--origin=`的点相同的一侧。`left`、`top`对应左端、上端，`right`、`bottom`对应右端、下端，`center`、`base`、`osuwari`对应中央（见上表右列）。
- 只写一个词时，仅指定 X 轴，Y 轴为`top`。`--target-origin=center`即`center.top`（目标上端的中央）。
- 无法解析的写法会被忽略（目标矩形上的点不变）。
- 坐靠的对象为基准矩形（无法坐靠时）时，使用基准矩形（包括虚拟窗口）上的点。
- 例：`--origin=osuwari --target-origin=center.top`将 surface 的坐姿位置与目标上端的中央对齐。`--origin=center.bottom --target-origin=center.top`将 ghost 的中央（X）和下端（Y）与目标的中央（X）和上端（Y）对齐。ghost 的脚下会落在目标上端，且不受 ghost 高度的影响。
- 内置 SAORI 的`osuwari`（兼容 Osuwari.dll）没有对应的参数。与以往一样，将 ghost 的角与目标的同一角对齐。

## surface 的坐姿位置 \[SSP 2.9.34\]

可在 shell 的`surfaces.txt`的 surface 括号块中，通过`point.osuwaripos.x`和`point.osuwaripos.y`指定坐姿位置（[point.osuwaripos.x](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.x.md)、[point.osuwaripos.y](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.y.md)）。这是`--origin=`的`osuwari`使用的点；未指定时与`point.basepos.x`、`point.basepos.y`相同（若也未指定，则使用其默认值）。

例如，对于宽 200、高 300 的 surface，要将坐姿位置设在腰部，可按如下方式编写。

```
surface0
{
point.osuwaripos.x,100
point.osuwaripos.y,250
}
```

此位置以 surface 左上角为起点，单位为像素，并随 surface 的缩放而缩放。它与脚下的基准位置（`point.basepos`；未指定时为下端中央 (100,300)）是不同的点，`--origin=base`使用基准位置，`--origin=osuwari`使用坐姿位置。

## 位置对齐示例

下面展示上述 surface 坐在左上角为 (400,400)、右下角为 (1000,900) 的窗口上的示例。`--origin=osuwari --target-origin=center.top`将 ghost 的坐姿位置与目标上端的中央重合。

![使用 --origin=osuwari --target-origin=center.top 坐靠时，ghost 窗口与目标的位置关系](../../../assets/image/osuwari-origin.svg)

由于坐姿位置 (100,250) 与目标上端的中央 (700,400) 重合，ghost 的左上角为 (700−100,400−250)=(600,150)。脚下的基准位置（默认为下端中央）位于坐姿位置下方 50 像素处的 (700,450)，落在窗口上端以内。由于 ghost 显示在目标前方，看起来就像坐在窗口边缘。

- 如果为每个 surface 都指定`point.osuwaripos`，切换 surface 时也会重新调整坐姿，使坐姿位置落在边缘上。
- 省略`--target-origin=`时，坐姿位置与目标中央重合。要让 ghost 坐在边缘上时，可使用`--target-origin=center.top`等方式指定目标侧的点。
- 也可以不使用坐姿位置，而通过 ghost 的角或边对齐。`--origin=center.bottom --target-origin=center.top`将 ghost 下端的中央与目标上端的中央对齐（脚下落在目标上）。
- 省略`--target-origin=`时，目标侧的点始终与 ghost 侧位于同一侧，因此无法指定将下端与上端对齐的组合。此时可使用`--origin=tr --y=-300`等方式，将上端对齐后再偏移。此偏移量与 ghost 的高度相匹配，因此高度变化时脚下位置也会偏移。

## 无法坐在目标上和超出边界时

无法坐在目标上或坐上去会超出边界时，会改为坐在基准矩形上，而不是目标上。基准矩形按以下顺序确定。

1. 通过`--area=`选择目标所在显示器的整个区域（`desktop`）或工作区（`workarea`）。没有目标时，使用 ghost 窗口所在的显示器（拖动时使用光标所在的显示器）。
2. 通过`--side=`选择直接使用第 1 步的区域（`center`），还是使用放在其外侧的虚拟窗口（`top` `left` `right` `bottom`）。虚拟窗口的长度与基准边相同，厚度为 100 像素。

![--side=创建的虚拟窗口与基准矩形的位置关系](../../../assets/image/osuwari-side.svg)

选择`bottom`时，虚拟窗口的上边缘与基准的下边缘重合。配合`--origin=osuwari --target-origin=center.top`使用时，坐下位置会落在基准下边缘的中央（如果是工作区，则会坐在任务栏的上边缘）。使用`--origin=center.bottom --target-origin=center.top`时，ghost 的下边缘会落在该位置，脚下站在基准的下边缘。

坐在基准矩形上时，`--origin=`、`--target-origin=`以及`--x=` `--y=`的用法与坐在目标上时相同。

!!! note "注"
    如果将`--origin=osuwari --target-origin=center.top`与默认的`--side=center`一起使用，回退到基准矩形时会坐在基准（整个工作区）上边缘的中央。坐下位置(100,250)与(960,0)重合，因此 ghost 的左上角为(860,-250)，大部分会出现在屏幕外。回退到基准矩形后不会进行超出边界判定，因此不会被拉回。要让它坐在屏幕下边缘时，请配合`--side=bottom`使用。

**超出边界判定**检查 ghost 的整个窗口（包括透明部分）是否处于包围所有显示器的矩形内。

- `--margin=`指定该矩形向外扩展的量。使用`--margin=0_0_100_0`时，向右超出不超过 100 像素不会被判定为超出边界。当 surface 的透明留白仅因出现在屏幕外就被判定为超出边界时，可使用此参数。
- `--noclip`不进行超出边界判定。根据目标位置，ghost 可能会一直停留在屏幕外。
- 使用`--target=fix`时以及没有目标时，不进行超出边界判定（本来就坐在基准矩形上）。

## 可通过拖动移动的范围

默认情况下，即使拖动 ghost 窗口，也无法将其从坐下位置移开。`--xmove`允许水平拖动，`--ymove`允许垂直拖动。未指定的方向即使移动也会返回坐下位置。

只能在所坐对象的矩形内部移动。

- `--xmove`: ghost 窗口的左边缘不小于对象的左边缘，右边缘不大于对象的右边缘。
- `--ymove`: ghost 窗口的上边缘不小于对象的上边缘，下边缘不大于对象的下边缘。

所坐对象在坐在目标上时是目标，在未坐在目标上时（使用`--target=fix`或回退到基准矩形时）是基准矩形（包括虚拟窗口）。例如，`--target=fix --origin=bl --xmove`会站在工作区的下边缘，只能水平移动。

移动后的位置按其在可移动范围内的比例，分别记录各方向的值。比例 0 表示 ghost 窗口的左边缘（上边缘）与对象的左边缘（上边缘）重合的位置，比例 1 表示右边缘（下边缘）与对象的右边缘（下边缘）重合的位置。

- 移动之前，坐在`--origin=` `--target-origin=` `--x=` `--y=`确定的位置。这些参数决定坐下时的默认位置。
- 移动一次后，该方向上的比例优先，不再使用`--origin=`等参数。即使对象或 ghost 窗口的大小改变，也会坐在相同比例的位置。更换目标或切换 surface 时也是如此。
- 仅当 ghost 窗口从上次布局结果的位置被移动时（通过拖动或`\![move]`），才会更新比例。仅因目标移动或大小改变，不会更新比例。
- 不可移动的方向仍由原点、目标侧的点和偏移量决定。
- 重新指定`osuwari`后，记录的比例会被清除，并恢复默认位置。
- 由于可移动范围仅限于对象内部，移动一次后，不会返回偏移到对象外的位置（例如坐在目标上边缘的位置）。要返回该位置，请重新指定`osuwari`。
- ghost 窗口大于对象时（可移动范围小于或等于 0），无法确定比例。即使移动也不会记录比例；如果已有记录的比例，则与对象的左边缘（上边缘）对齐并坐下。如果尚未移动过，则保持在默认位置。

例如，目标左上角为(300,400)、右下角为(1100,1000)，ghost 窗口宽 200、高 300，使用`--origin=tl --xmove`时，初始左上角为(300,400)。

- 拖动使左边缘移动到600时（范围为300到900，恰好在中间），比例变为0.5。
- 目标宽度变为600（左上角(300,400)、右下角(900,1000)）时，范围变为300到700，左边缘变为500。
- 另一个窗口（左上角(1000,100)、右下角(1400,800)）移到前面时，范围变为1000到1200，左边缘变为1100。

## 前后层级关系

坐下期间，ghost 窗口会保持与目标的前后层级关系。通过`--zorder=`选择显示在目标前面还是紧邻其后。不影响位置计算。

![使用 --zorder=front 和 --zorder=back 时，ghost 窗口与目标的前后层级关系](../../../assets/image/osuwari-zorder.svg)

- `front`: 仅当 ghost 位于目标下方时，将其移到目标正上方。如果已经位于目标上方则不移动（即使中间有其他窗口也是如此，以免与坐在同一窗口上的其他 ghost 争夺排列顺序）。
- `back`: 保持在目标紧后方（正下方）。如果中间出现其他应用的可见窗口，则在下次位置检查时（间隔由`--interval=`指定）返回正下方。

目标为最前面的窗口（如任务栏）时，以及 ghost 设置为“始终显示在最前面”时，请参阅“选项”中的补充说明。

## 数值示例

以下列条件为例，说明 ghost 窗口左上角的位置。

- ghost 窗口：宽200、高300。surface 的基准位置为默认的脚下中央(100,300)。坐姿位置为(100,250)，在`surfaces.txt`中写为`point.osuwaripos.x,100`、`point.osuwaripos.y,250`。
- 屏幕：1920×1080。工作区为1920×1040（任务栏位于下方，高度为40）。
- 目标：除非另有说明，左上角为(400,400)，右下角为(1000,900)。

省略`--origin=`和`--area=`的指定值按 SSP 2.9.34及以后的默认值（`osuwari`和`workarea`）计算。2.9.33的默认值为`tl`和`desktop`，因此结果不同。

| 指定值 | 左上角 | 说明 |
|---|---|---|
| `--origin=osuwari`（默认） | (600,400) | 坐姿位置(100,250)与目标中心(700,650)重合。 |
| `--origin=osuwari --target-origin=center.top` | (600,150) | 坐姿位置与目标上边缘中央(700,400)重合。坐在窗口边缘上（见上图）。 |
| `--origin=tr --x=-20 --y=-300` | (780,100) | 将右上角对齐目标的右上角，再向左移动20、向上移动300。下边缘(400)与目标上边缘重合，站在窗口上边缘。 |
| `--origin=bl` | (400,600) | 将左下角对齐目标的左下角。下边缘(900)与目标下边缘重合。 |
| `--origin=center.bottom --target-origin=center.top` | (600,100) | 将 ghost 的下边缘中央对齐目标的上边缘中央(700,400)。无论 ghost 高度如何，都站在窗口上边缘。 |
| `--target=fix --origin=osuwari --target-origin=center.top --side=bottom` | (860,790) | 将坐姿位置与工作区下方虚拟窗口的上边缘中央(960,1040)重合。坐在工作区下边缘上。 |
| `--target=fix --origin=center.bottom --target-origin=center.top --side=bottom` | (860,740) | 将 ghost 的下边缘中央对齐同一点。站在工作区下边缘。 |
| 使用第3行的指定值，目标已最大化（左上角(0,0)、右下角(1920,1040)）。添加`--side=bottom` | (1700,740) | 由于上边缘位于屏幕外(-300)，会被裁切。回退到工作区下方的虚拟窗口，并以相同的`--origin=` `--x=` `--y=`坐下。下边缘为1040（工作区下边缘）。 |
| 从上一行中去掉`--side=bottom` | (1700,-300) | 回退到工作区本身。由于不进行裁切判定，会坐在屏幕外。 |
| `--target=fix --origin=bl` | (0,740) | 站在工作区左下角。使用`--origin=br`时为(1720,740)。 |
| `--target=fix` | (860,270) | 坐姿位置与工作区中心(960,520)重合。 |
| 目标为(1500,400)-(2000,900)。`--origin=tr --y=-300 --side=bottom` | (1720,740) | 由于右边缘2000超出屏幕右边缘1920，会被裁切。回退到工作区下方的虚拟窗口。 |
| 在上一行中添加`--margin=0_0_100_0`或`--noclip` | (1800,100) | 由于允许向右超出100像素（或不进行判定），仍会坐在目标上。 |

## 写入 descript.txt

在 ghost、shell 的`descript.txt`中的`seriko.alignmenttodesktop`（包括带有`sakura.`、`kero.`、`char*.`前缀的项）也可以将`osuwari`写作值。在值后面以逗号分隔，依次写入与标签相同的`--`选项（[※显示位置信息](../../../descript/shell/descript-txt/note-1.md#補足)）。

```
sakura.seriko.alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom
```

- 优先级与其他值相同（ghost 侧全局＜ghost 侧各 scope＜shell 侧全局＜shell 侧各 scope）。
- 启动 ghost 或切换 shell 时，按该设置开始跟踪。
- `\![set,alignmenttodesktop,default]`和内置 SAORI 的`osuwari`的`STOP`会恢复为`descript.txt`中的设置。如果`descript.txt`为 osuwari，则重新按 osuwari 坐下。
- 无法解析的选项会在错误日志中输出警告并被忽略。

## 与内置 SAORI 的关系

内置 SAORI 的`osuwari`（兼容 Osuwari.dll）也执行相同的处理。但 SAORI 的`START`为与原作保持一致，省略第7个及以后的参数时会沿用上次的值（[兼容模块](../../../spec/saori-ex/compat.md)）。

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
