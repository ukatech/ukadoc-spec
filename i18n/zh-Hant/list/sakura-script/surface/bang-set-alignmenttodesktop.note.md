# 關於 `\![set,alignmenttodesktop,osuwari]`

`\![set,alignmenttodesktop,osuwari,オプション,…]` \[SSP 2.9.33\]

讓 ghost 視窗「坐在」、「貼在」或「掛在」其他視窗的角落或邊緣。這是 SSP 內建了與 ukiya 的 SAORI「Osuwari.dll」相同的處理方式，選項也與其相容。無須在 shell 的 `descript.txt` 中寫入 `seriko.alignmenttodesktop,free`（指定 `osuwari` 本身就會指定對齊方式）。

## 原理

osuwari會以固定間隔重複以下動作：

> 將 ghost 視窗的左上角放在哪裡？

答案取決於要對齊「哪個視窗的」「哪個點」，以及「ghost 視窗的哪個點」，並「偏移幾像素」。涉及的項目如下。

- **ghost 視窗**: 各角色（`\0`・`\1`…）的視窗。大小與目前顯示的 surface 圖片相同，也包含透明部分。位置以左上角座標表示。surface 改變而尺寸變化時，右端、下端和中央的位置也會改變。
- **目標**: ghost 要坐上的視窗。以外觀上的邊框測量（不包含陰影等不可見邊框）。
- **基準矩形**: 無法坐上目標，或坐上後會超出螢幕時，取代目標而坐上的矩形。此矩形是目標所在螢幕的整個畫面或工作區域，由 `--area=` 和 `--side=` 決定。
- **原點**: 「目標矩形的哪個點，要對齊 ghost 視窗的哪個點」這組點。ghost 視窗一側的點由 `--origin=` 決定，目標矩形一側的點由 `--target-origin=` 決定。
- **偏移**: 對齊位置的偏移量。由 `--x=` 和 `--y=` 決定（右方、下方為正）。

位置分別依照以下公式計算 X 軸和 Y 軸座標。

```
ゴーストのウインドウの左上 = 対象の矩形の点 − ゴーストのウインドウの点 + ずれ
```

ghost 視窗上的點由 `--origin=` 決定，目標矩形上的點則由 `--target-origin=` 決定。坐上目標時，使用目標矩形；無法坐上目標時，則使用基準矩形。

各項設定與選項的對應如下。

| 設定項目 | 選項 |
|---|---|
| 要坐上哪個視窗 | `--target=` |
| 要對齊 ghost 視窗上的哪個點 | `--origin=` |
| 要對齊目標矩形上的哪個點 | `--target-origin=` |
| 要偏移多少 | `--x=` `--y=` |
| 無法坐上或超出螢幕時，要坐到哪裡 | `--area=` `--side=` `--margin=` `--noclip` |
| 可透過拖曳移動的範圍 | `--xmove` `--ymove` |
| 要顯示在目標的前方或後方 | `--zorder=` |
| 以多長的間隔追蹤 | `--interval=` |

## 位置的決定方式

每隔 `--interval=` 指定的時間，依照以下順序決定位置。不過，如果目標、目標矩形、ghost 視窗矩形、surface 的基準位置和坐姿位置都與上次相同，就不會重新計算。

1. 尋找目標（`--target=`）。
   - `active`: 前景視窗。若前景視窗無法坐上（如下所述），則使用最近一次成功坐上的視窗。若尚未有成功坐上的視窗，則沒有目標。
   - `@文字列`: 標題包含此字串且可坐上的視窗。若有多個，則選擇 Z 順序中位於前方的視窗。
   - `#数値`: 視窗控制代碼為此數值（十進位）的視窗。若無法坐上，則沒有目標。
   - `fix`: 一律沒有目標。
2. 決定要坐上的矩形。有目標且可坐上時，使用目標矩形；沒有目標時，使用基準矩形（`--area=` 和 `--side=`）。
3. 將 `--origin=`（ghost 視窗上的點）和 `--target-origin=`（目標矩形上的點）指定的兩個點重合，計算 ghost 視窗的左上角位置，再加上 `--x=` 和 `--y=` 的值。
4. 對於指定 `--xmove`・`--ymove` 的方向，如果 ghost 視窗的位置被移離上次的配置結果（例如透過拖曳），就將該位置限制在目標內側，並記錄其在可移動範圍中的比例。如果已有記錄的比例，就以目標矩形中該比例的位置取代步驟 3 算出的位置（[可透過拖曳移動的範圍](bang-set-alignmenttodesktop.note.md#ドラッグで動かせる範囲)）。
5. 檢查 ghost 視窗是否超出螢幕（裁切判定）。若超出螢幕，就將步驟 2 的目標換成基準矩形，再執行一次步驟 3～4。重做後不再檢查。指定 `--target=fix`・`--noclip` 或沒有目標時，不進行檢查。
6. 將 ghost 視窗移至計算出的位置，並調整前後順序（`--zorder=`）。

即使在步驟 5 重做，步驟 3 所選的兩個點和偏移量仍使用相同的值。只有要坐上的矩形會改變。

## 選項

選項使用 `--名稱=值` 的格式，皆可省略。省略的選項會使用預設值，而不是上次呼叫時指定的值。無法解讀的選項會忽略。

| 選項 | 預設值 | 說明 |
|---|---|---|
| `--target=` | `active` | 要追蹤的目標。`active`: 前景視窗 / `fix`: 固定於螢幕（工作區域）/ `@文字列`: 視窗標題包含此字串（不區分大小寫）的視窗 / `#数値`: 視窗控制代碼為此數值的視窗 |
| `--origin=` | `osuwari` | ghost 視窗上要對齊目標的點（原點）。使用 `左右.上下` 的格式（見下方「原點的寫法」）。也可以像 `tl` `tr` `bl` `br` 一樣，以兩個字元表示角落 |
| `--target-origin=` | 省略（自動） | \[SSP 2.9.34\] 目標矩形上要對齊 ghost 視窗的點。格式與 `--origin=` 相同，但不可使用 `base` 和 `osuwari`（見下方「目標矩形上的點」）。省略時，會使用與 `--origin=` 相同的一側（`left` 為左端、`right` 為右端、`center`・`base`・`osuwari` 為中央） |
| `--x=` `--y=` | `0` | 從原點算起的偏移量（像素）。指定 `--xmove` `--ymove` 的方向，在移動前會使用此預設值 |
| `--interval=` | `100` | 檢查位置的間隔（毫秒）。小於 10 時使用 10 |
| `--xmove` `--ymove` | 無 | 允許向該方向拖曳移動（直到目標矩形內側）。移動後的位置會以其在可移動範圍中的比例記錄（見下方「可透過拖曳移動的範圍」）。未指定的方向即使拖曳，也會回到坐姿位置。也可以寫成 `--xmove=false` |
| `--noclip` | 無 | 不進行裁切判定 |
| `--area=` | `workarea` | 無法坐上或超出螢幕時使用的基準。`desktop`: 整個畫面 / `workarea`: 工作區域（扣除工作列等部分） |
| `--side=` | `center` | 無法坐上或超出螢幕時，「虛擬視窗」相對於基準的位置。`center`: 基準本身 / `top` `left` `right` `bottom`: 在基準的上、左、右、下側放置厚度為 100 像素的虛擬視窗 |
| `--margin=` | `0_0_0_0` | 裁切判定的容許範圍（像素）。依序為 `左_上_右_下`，以空白或 `_` 分隔。例如 `0_50_0_100` 表示超出上方 50 像素、下方 100 像素以內時，不會判定為裁切 |
| `--zorder=` | `front` | 與目標視窗的前後順序。`front`: 顯示在目標正上方（前方）/ `back`: 顯示在目標正後方（緊鄰其後）。未坐在目標上時（無法坐上或指定 `--target=fix`）不做任何處理 |

- `--origin=` 和 `--area=` 在標籤和 `descript.txt` 中的預設值分別為 `osuwari` 和 `workarea`。內建 SAORI 的 `osuwari`（與 Osuwari.dll 相容）則為配合原作，維持 `tl` 和 `desktop`。\[SSP 2.9.34\] 在 2.9.33 中，標籤和 `descript.txt` 的預設值也為 `tl` 和 `desktop`。
- 無法坐上目標時（指定 `--target=fix`、目標視窗不存在、前景視窗無法坐上且最近一次成功坐上的視窗也不存在），以及發生裁切時（照原位置坐上會超出螢幕），會將由 `--area` 和 `--side` 決定的基準矩形作為「虛擬目標」坐上。指定 `--target=fix` 時不進行裁切判定。
- 視窗矩形以外觀上的邊框測量（不包含 Windows 10 以後的不可見邊框）。作為基準的螢幕，是目標視窗所在的螢幕（沒有目標時，則是 ghost 所在的螢幕；拖曳期間則是游標所在的螢幕）。裁切則以所有螢幕合併後的範圍判定。
- 無法坐上最小化或隱藏的視窗、其他虛擬桌面的視窗、對話框等擁有者視窗，以及 SSP 本身的視窗（指定 `--target=active` 時）。指定 `--target=active` 時，也無法坐上明顯不適合坐上的 shell 視窗（桌面、Alt+Tab・工作檢視、開始・搜尋・IME 面板等 shell 顯示的 UWP 視窗、Windows 8 的 Metro 全螢幕視窗）。前景是這類視窗時，會繼續坐在最近一次成功坐上的視窗上。透過 `@文字列`・`#数値` 自行指定的視窗不受此排除規則限制。
- 坐在目標上時，ghost 會顯示在目標視窗上方。只有目標是最前方視窗（例如工作列）時，osuwari 才會將 ghost 設為最前層（永遠顯示在其他視窗前方）；若非如此，ghost 不會位於最前層。不過，設定為「永遠顯示在最前方」的 ghost，會依照該設定維持在最前層，不受目標影響。即使目標是最前方視窗，ghost 仍會顯示在目標上方（每當目標回到前景時，ghost 也會回到上方）。
- 指定 `--zorder=back` 時，ghost 會顯示在目標視窗的正後方（Z 順序中緊鄰其後）。可用於讓角色從目標遮住的位置探出頭來。即使其他應用程式的視窗插入兩者之間，下次檢查位置時（每隔 `--interval=` 指定的時間）也會立即回到目標正後方。目標是最前方視窗（例如工作列）時，ghost 也會位於最前層，並在最前層視窗的排列中緊鄰目標之後。設定為「永遠顯示在最前方」的 ghost 坐在非最前層視窗後方時，會優先遵守該設定並維持在最前層（指定顯示在後方的效果不會生效）。
- 如果只想坐在工作列正上方（不追蹤視窗），請使用 `--target=fix` 固定在螢幕上，並使用工作區域的下端（例如：`--target=fix,--origin=bl,--area=workarea,--side=center`。若要坐在右端，則使用 `--origin=br`）。工作區域會扣除工作列等部分，因此只有工作列位於螢幕下方時，才會坐在工作列正上方。工作列位於螢幕上方或左右側時，會坐在螢幕下端（工作區域下端）。若設定為自動隱藏工作列，工作區域會是整個畫面，因此會坐在螢幕下端。
- 透過指定其他對齊方式（`top` `bottom` `left` `right` `free`）或變更 shell 等方式，osuwari 會停止。`default` 會恢復 ghost 的預設設定（`descript.txt`，後述）。視窗模式期間會停止，返回一般模式後會重新啟動。
- 坐在目標上時的位置不會儲存為站立位置。
- 使用 sticky window 連動的視窗中，非父視窗的一側（連動的子視窗）會遵循父視窗，因此即使指定 osuwari 也不會生效。父視窗坐上目標時，子視窗也會一起移動。
- `\0` 和 `\1` 可以分別指定。不過，ghost 視窗的前後順序以 ghost 為單位，因此多個角色坐上目標時，由編號較小的角色所指定的目標決定。

## How to specify the origin \[SSP 2.9.34\]

`--origin=` aligns a point on the top of the ghost window with a point on the top of the target rectangle. Specify it in the form `left.right`, with the X-axis before `.` and the Y-axis after it. Each axis can use the following terms (case-insensitive).

| Term | Point on the ghost window | Point on the target rectangle (when `--target-origin=` is omitted) |
|---|---|---|
| `left` (for X) / `top` (for Y) | Left edge / top edge | Left edge / top edge |
| `right` (for X) / `bottom` (for Y) | Right edge / bottom edge | Right edge / bottom edge |
| `center` | Center | Center |
| `base` | Surface base position (`point.basepos.x`・`point.basepos.y`; center of the feet by default) | Center |
| `osuwari` | Surface sitting position (`point.osuwaripos.x`・`point.osuwaripos.y`; same as `base` by default) | Center |

- If `base` or `osuwari` is specified as a single term without `.`, it applies to both the X and Y axes (`--origin=osuwari` is equivalent to `osuwari.osuwari`). If any other term is specified as a single term, it applies only to the X axis, and the Y axis is set to `top`.
- `tl` is equivalent to `left.top`, `tr` to `right.top`, `bl` to `left.bottom`, and `br` to `right.bottom`.
- Unrecognized formats are ignored (the origin remains unchanged).
- The target rectangle does not have `base` or `osuwari`, so the center is used when `--target-origin=` is omitted. For example, the default `--origin=osuwari` places the ghost's sitting position at the center of the target rectangle. Adjust the sitting position with `--x=` and `--y=`, or change the point on the target side with `--target-origin=`.
- Example: `--origin=center.bottom` aligns the ghost's center (X) and bottom edge (Y) with the target's center (X) and bottom edge (Y). `--origin=right.osuwari` aligns the ghost's right edge (X) and `point.osuwaripos.y` (Y) with the target's right edge (X) and center (Y).

## Point on the target rectangle \[SSP 2.9.34\]

`--target-origin=` specifies the point on the target rectangle to which the point on the ghost window is aligned. It uses the same format as `--origin=` (`left.right`・`tl` `tr` `bl` `br`・a single term), and accepts only `left` `right` `top` `bottom` and `center`. The target rectangle does not have `base` or `osuwari`, so specifying either is treated as an unrecognized format and ignored.

- If omitted, the point is on the same side as the point specified by `--origin=`. `left`・`top` mean the left edge・top edge, `right`・`bottom` mean the right edge・bottom edge, and `center`・`base`・`osuwari` mean the center (the right-hand column in the table above).
- If specified as a single term, it applies only to the X axis, and the Y axis is set to `top`. `--target-origin=center` means `center.top` (the center of the target's top edge).
- Unrecognized formats are ignored (the point on the target rectangle remains unchanged).
- If the target is the reference rectangle (when sitting is not possible), the point is on the reference rectangle (including the virtual window).
- Example: `--origin=osuwari --target-origin=center.top` aligns the surface's sitting position with the center of the target's top edge. `--origin=center.bottom --target-origin=center.top` aligns the ghost's center (X) and bottom edge (Y) with the target's center (X) and top edge (Y). The ghost's feet rest on the target's top edge, regardless of the ghost's height.
- The built-in SAORI `osuwari` (compatible with Osuwari.dll) has no corresponding argument. As before, it aligns the same corners of the ghost and target.

## Surface sitting position \[SSP 2.9.34\]

You can specify a sitting position with `point.osuwaripos.x`・`point.osuwaripos.y` in a shell's `surfaces.txt` surface brace ([point.osuwaripos.x](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.x.md)・[point.osuwaripos.y](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.y.md)). This is the point used by `osuwari` in `--origin=`. If not specified, it is the same as `point.basepos.x`・`point.basepos.y` (or their defaults if they are not specified).

For example, to place the sitting position at the waist on a surface that is 200 pixels wide and 300 pixels high, write the following.

```
surface0
{
point.osuwaripos.x,100
point.osuwaripos.y,250
}
```

This position is measured in pixels from the top left of the surface, and scales with the surface. It is separate from the feet's base position (`point.basepos`; the default is the center of the bottom edge (100,300)). `--origin=base` uses the base position, while `--origin=osuwari` uses the sitting position.

## Positioning examples

The example below shows the surface above sitting on a window whose top-left corner is (400,400) and bottom-right corner is (1000,900). `--origin=osuwari --target-origin=center.top` places the ghost's sitting position at the center of the target's top edge.

![Position of the ghost window relative to the target when sitting with --origin=osuwari --target-origin=center.top](../../../assets/image/osuwari-origin.svg)

The sitting position (100,250) is aligned with the center of the target's top edge (700,400), so the ghost's top-left corner is at (700−100,400−250)=(600,150). The feet's base position (the center of the bottom edge by default) is 50 pixels below the sitting position, at (700,450), inside the top edge of the window. The ghost is displayed in front of the target, so it appears to be sitting on the window's edge.

- If you specify `point.osuwaripos` for each surface, the ghost will reposition itself when switching surfaces so that its sitting position remains on the edge.
- If `--target-origin=` is omitted, the sitting position is aligned with the center of the target. To make the ghost sit on the edge, specify a point on the target side, such as `--target-origin=center.top`.
- You can also align a corner or edge of the ghost without using the sitting position. `--origin=center.bottom --target-origin=center.top` aligns the center of the ghost's bottom edge with the center of the target's top edge (so the feet rest on it).
- If `--target-origin=` is omitted, the point on the target side is always on the same side as the ghost's point, so you cannot align the bottom edge with the top edge. In that case, align the top edges and offset the ghost, for example with `--origin=tr --y=-300`. This offset is based on the ghost's height, so the feet will shift if its height changes.

## 無法坐上目標或超出範圍時

無法坐上目標，或坐上後會超出範圍時，會改坐在基準矩形上。基準矩形依照以下順序建立。

1. 使用 `--area=` 選擇目標所在螢幕的整體範圍（`desktop`）或工作區（`workarea`）。沒有目標時，使用 ghost 視窗所在的螢幕（拖曳期間則使用游標所在的螢幕）。
2. 使用 `--side=` 選擇直接使用 1 的範圍（`center`），或使用放在其外側的虛擬視窗（`top` `left` `right` `bottom`）。虛擬視窗的長度與基準邊相同，厚度為 100 像素。

![--side=所建立的虛擬視窗與基準矩形的位置關係](../../../assets/image/osuwari-side.svg)

選擇 `bottom` 時，虛擬視窗的上緣會與基準的下緣重疊。若搭配 `--origin=osuwari --target-origin=center.top`，坐姿位置會落在基準下緣的中央（若為工作區，則會坐在工作列的上緣）。若使用 `--origin=center.bottom --target-origin=center.top`，則 ghost 的下緣會落在基準下緣上，腳邊會站在基準下緣。

坐在基準矩形上時，`--origin=`、`--target-origin=`、`--x=` `--y=`的用法與坐在目標上一樣。

!!! note "備註"
    若將 `--origin=osuwari --target-origin=center.top` 與 `--side=center`（預設值）搭配使用，掉到基準矩形上時，會坐在基準（整個工作區）的上緣中央。坐姿位置 (100,250) 會與 (960,0) 重疊，因此 ghost 的左上角會位於 (860,-250)，大部分會跑到畫面外。掉到基準矩形上後不會進行超出判定，因此不會被拉回。若要讓 ghost 坐在畫面下緣，請搭配 `--side=bottom`。

**超出判定**會檢查 ghost 的整個視窗（包括透明部分）是否位於包住所有螢幕的矩形內。

- `--margin=`是將該矩形向外擴大的量。若設為 `--margin=0_0_100_0`，在向右超出 100 像素之前都不會判定為超出。當只有表面透明的留白超出畫面就會被判定為超出時，可使用此設定。
- `--noclip`不會進行超出判定。依目標的位置而定，ghost 可能會停留在畫面外。
- `--target=fix`時，以及沒有目標時，不會進行超出判定（原本就坐在基準矩形上）。

## 可透過拖曳移動的範圍

預設情況下，即使拖曳 ghost 視窗，也不能離開坐姿位置。`--xmove`允許水平拖曳，`--ymove`允許垂直拖曳。未指定的方向即使移動，也會回到坐姿位置。

只能在坐姿對象矩形的內側移動。

- `--xmove`: ghost 視窗的左緣須大於或等於對象的左緣，右緣須小於或等於對象的右緣。
- `--ymove`: ghost 視窗的上緣須大於或等於對象的上緣，下緣須小於或等於對象的下緣。

坐姿對象在坐在目標上時是目標；未坐在目標上時（`--target=fix`、掉到基準矩形上時）則是基準矩形（包括虛擬視窗）。例如，`--target=fix --origin=bl --xmove`會讓 ghost 站在工作區下緣，只能水平移動。

移動位置會依各方向記錄為可移動範圍內的比例。比例 0 表示 ghost 視窗的左緣（上緣）與對象的左緣（上緣）重疊的位置；比例 1 表示右緣（下緣）與對象的右緣（下緣）重疊的位置。

- 移動之前，會坐在由 `--origin=` `--target-origin=` `--x=` `--y=`決定的位置。這些是坐姿的預設值。
- 移動一次後，該方向會以比例為優先，不再使用 `--origin=`等設定。即使對象或 ghost 視窗的大小改變，也會坐在相同比例的位置。更換目標或切換表面時也相同。
- 只有在 ghost 視窗從上次配置的位置移動時（例如拖曳或 `\![move]`），才會更新比例。只有目標移動或大小改變時，不會更新。
- 無法移動的方向會維持原本的規則，由原點、目標側的點和位移決定。
- 重新指定 `osuwari` 時，已記錄的比例會清除並恢復預設值。
- 可移動範圍僅限對象內側，因此移動一次後，便無法回到對象外側的位置（例如坐在目標上緣的位置）。若要回到該位置，請重新指定 `osuwari`。
- 當 ghost 視窗大於對象時（可移動範圍為 0 以下），比例無法確定。移動時不會記錄比例；若已有記錄的比例，則會對齊對象的左緣（上緣）坐下。若尚未移動，則維持預設位置。

例如，目標的左上角為 (300,400)、右下角為 (1100,1000)，ghost 視窗寬 200、高 300，且使用 `--origin=tl --xmove`時，最初的左上角位置為 (300,400)。

- 透過拖曳將左緣移至 600 時（範圍為 300 到 900，位於正中央），比例會變成 0.5。
- 目標寬度變為 600（左上角 (300,400)、右下角 (900,1000)）時，範圍會變成 300 到 700，左緣會移至 500。
- 另一個視窗（左上角 (1000,100)、右下角 (1400,800)）移至前景時，範圍會變成 1000 到 1200，左緣會移至 1100。

## 前後順序

坐在目標上時，ghost 視窗會維持與目標的前後順序。使用 `--zorder=`選擇顯示在目標前方，或緊接在目標後方。此設定不會影響位置計算。

![--zorder=front 與 --zorder=back 的 ghost 視窗和目標之前後順序](../../../assets/image/osuwari-zorder.svg)

- `front`: 只有在 ghost 位於目標後方時，才會將 ghost 移到目標正前方。若已在目標前方則不移動（即使兩者之間有其他視窗也一樣。這是為了避免和坐在同一視窗上的其他 ghost 爭奪排列順序）。
- `back`: 維持在目標緊後方（正下方）。若其他應用程式的可見視窗出現在兩者之間，則會在下次確認位置時（依 `--interval=`的間隔）移回正下方。

若目標是最前方的視窗（例如工作列），或 ghost 設定為「永遠顯示在最前方」，請參閱「選項」中的補充說明。

## Numerical examples

The following shows where the top-left corner of the ghost window will be under these conditions.

- Ghost window: 200 wide × 300 high. The surface's reference position is the default center of the feet (100,300). The sitting position is (100,250), specified in `surfaces.txt` as `point.osuwaripos.x,100` and `point.osuwaripos.y,250`.
- Screen: 1920×1080. Work area: 1920×1040 (the taskbar is at the bottom and is 40 pixels high).
- Target: unless otherwise noted, top-left (400,400) and bottom-right (1000,900).

Values for specifications that omit `--origin=` and `--area=` are calculated using the defaults (`osuwari` and `workarea`) from SSP 2.9.34 onward. In 2.9.33, the defaults are `tl` and `desktop`, so the results differ.

| Specification | Top-left | Details |
|---|---|---|
| `--origin=osuwari` (default) | (600,400) | The sitting position (100,250) overlaps the center of the target (700,650). |
| `--origin=osuwari --target-origin=center.top` | (600,150) | The sitting position overlaps the center of the target's top edge (700,400). The ghost sits on the window's edge (diagram above). |
| `--origin=tr --x=-20 --y=-300` | (780,100) | Align the top-right corner with the target's top-right corner, then move 20 pixels left and 300 pixels up. The bottom edge (400) overlaps the target's top edge, so the ghost stands on the top edge of the window. |
| `--origin=bl` | (400,600) | Align the bottom-left corner with the target's bottom-left corner. The bottom edge (900) overlaps the target's bottom edge. |
| `--origin=center.bottom --target-origin=center.top` | (600,100) | Align the center of the ghost's bottom edge with the center of the target's top edge (700,400). The ghost stands on the top edge of the window, regardless of its height. |
| `--target=fix --origin=osuwari --target-origin=center.top --side=bottom` | (860,790) | The sitting position overlaps the center of the top edge (960,1040) of the virtual window below the work area. The ghost sits on the bottom edge of the work area. |
| `--target=fix --origin=center.bottom --target-origin=center.top --side=bottom` | (860,740) | Align the center of the ghost's bottom edge with the same point. The ghost stands on the bottom edge of the work area. |
| With the specification from the third row, the target is maximized (top-left (0,0), bottom-right (1920,1040)). Add `--side=bottom` | (1700,740) | The top edge would be outside the screen (-300), so the ghost would be clipped. It falls to the virtual window below the work area and sits using the same `--origin=`, `--x=`, and `--y=` values. The bottom edge is at 1040 (the bottom edge of the work area). |
| Remove `--side=bottom` from the row above | (1700,-300) | The ghost falls to the work area itself. Clipping is not checked, so it sits outside the screen. |
| `--target=fix --origin=bl` | (0,740) | The ghost stands at the bottom-left of the work area. With `--origin=br`, it is at (1720,740). |
| `--target=fix` | (860,270) | The sitting position overlaps the center of the work area (960,520). |
| The target is (1500,400)-(2000,900). `--origin=tr --y=-300 --side=bottom` | (1720,740) | The right edge, 2000, exceeds the right edge of the screen, 1920, so the ghost would be clipped. It falls to the virtual window below the work area. |
| Add `--margin=0_0_100_0` or `--noclip` to the row above | (1800,100) | Since an overhang of 100 pixels to the right is allowed (or clipping is not checked), the ghost remains seated on the target. |

## Specify in descript.txt

You can also specify `osuwari` as the value of `seriko.alignmenttodesktop` in a ghost or shell's `descript.txt` (including entries prefixed with `sakura.`, `kero.`, or `char*.`). After the value, list options matching the tag's `--` options, separated by commas ([※ display position information](../../../descript/ghost/descript-txt/note-1.md#補足)).

```
sakura.seriko.alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom
```

- The priority order is the same as for other values (entire ghost < individual ghost scope < entire shell < individual shell scope).
- When the ghost starts or the shell changes, tracking begins with these settings.
- `\![set,alignmenttodesktop,default]` and `STOP` for the built-in SAORI `osuwari` restore the settings in `descript.txt`. If `descript.txt` specifies osuwari, the ghost sits down in the osuwari position again.
- Unrecognized options are ignored, with a warning written to the error log.

## Relationship with the built-in SAORI

The built-in SAORI `osuwari` (compatible with Osuwari.dll) performs the same processing. However, to match the original, `START` for SAORI carries over the previous values if the seventh and subsequent arguments are omitted ([compatibility module](../../../spec/saori-ex/compat.md)).

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
