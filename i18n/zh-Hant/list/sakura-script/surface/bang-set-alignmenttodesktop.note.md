# 關於 `\![set,alignmenttodesktop,osuwari]`

`\![set,alignmenttodesktop,osuwari,オプション,…]` \[SSP 2.9.33\]

讓 ghost 的視窗「坐在」「貼在」其他視窗的角落或邊緣，或從其上「垂掛」。SSP 內建了與 ukiya 的 SAORI「Osuwari.dll」相同的處理，選項也與其對應。不需要在 shell 的 `descript.txt` 中寫入 `seriko.alignmenttodesktop,free`（指定 `osuwari` 本身就是一種對齊設定）。

## 運作概念

osuwari 會以固定間隔反覆決定下列事項。

> 將 ghost 視窗的左上角放在畫面的哪個位置。

答案取決於將「ghost 視窗的哪個點」對齊「哪個視窗的」「哪個點」，以及「偏移多少像素」。涉及的項目如下。

- **ghost 視窗**：每個角色（`\0`、`\1`…）各自的視窗。大小與目前顯示的 surface 圖像相同，也包含透明部分。位置以左上角座標表示。surface 改變而使大小改變時，右邊緣、下邊緣及中央的位置也會改變。
- **目標**：ghost 所坐在的視窗。以可見邊框測量（不包含陰影等不可見邊框）。
- **基準矩形**：無法坐在目標上，或坐上去會超出畫面時，取代目標供 ghost 坐的矩形。由目標所在螢幕的整個畫面或工作區決定，透過 `--area=` 和 `--side=` 設定。
- **原點**：「將 ghost 視窗的哪個點對齊目標矩形的哪個點」的組合。ghost 視窗側的點由 `--origin=` 決定，目標矩形側的點由 `--target-origin=` 決定。
- **偏移**：相對於對齊位置的偏移量。由 `--x=` 和 `--y=` 決定（向右、向下為正）。

位置分別以 X 軸、Y 軸的下列公式求得。

```
ゴーストのウインドウの左上 = 対象の矩形の点 − ゴーストのウインドウの点 + ずれ
```

ghost 視窗的點由 `--origin=` 決定，目標矩形的點由 `--target-origin=` 決定。坐在目標上時使用目標矩形，無法坐在目標上時使用基準矩形。

各項設定與選項的對應如下。

| 設定事項 | 選項 |
|---|---|
| 坐在哪個視窗上 | `--target=` |
| 對齊 ghost 視窗的哪個點 | `--origin=` |
| 對齊目標矩形的哪個點 | `--target-origin=` |
| 從該處偏移多少 | `--x=` `--y=` |
| 無法坐上去或超出畫面時，坐在哪裡 | `--area=` `--side=` `--margin=` `--noclip` |
| 可透過拖曳移動的範圍 | `--xmove` `--ymove` |
| 位於目標前方或後方 | `--zorder=` |
| 追蹤的間隔 | `--interval=` |

## 位置的決定方式

每隔 `--interval=` 指定的時間，依下列順序決定位置。不過，如果目標、目標矩形、ghost 視窗矩形、surface 的基準位置和坐姿位置均未與上次不同，就不重新計算。

1. 尋找目標（`--target=`）。
   - `active`：前景視窗。無法坐上的視窗（見下文）位於前景時，使用最近一次可坐上的視窗。如果尚無可坐上的視窗，則沒有目標。
   - `@文字列`：標題包含該字串且可坐上的視窗。如果有多個，使用 Z 順序中較前方的視窗。
   - `#数値`：視窗控制代碼為該數值（十進位）的視窗。無法坐上去時，則沒有目標。
   - `fix`：一律沒有目標。
2. 決定供 ghost 坐的矩形。有目標且可坐上去時使用目標矩形。沒有目標時使用基準矩形（`--area=` 和 `--side=`）。
3. 將 `--origin=`（ghost 視窗的點）和 `--target-origin=`（供 ghost 坐的矩形上的點）選出的兩點重合，求出 ghost 視窗的左上角位置，再加上 `--x=` 和 `--y=`。
4. 對指定了 `--xmove`、`--ymove` 的方向，若 ghost 視窗已從上次配置結果移動（例如拖曳），則將該位置限制在對方矩形內，並以可移動範圍中的比例記住。如果已有記住的比例，就使用對方矩形中該比例的位置，取代步驟 3 求得的位置（[可透過拖曳移動的範圍](bang-set-alignmenttodesktop.note.md#ドラッグで動かせる範囲)）。
5. 檢查 ghost 視窗是否超出畫面（超出畫面判定）。如果超出，將步驟 2 的矩形改為基準矩形，僅再執行一次步驟 3～4。重新執行後不再檢查。`--target=fix`、`--noclip` 或沒有目標時，不進行檢查。
6. 將 ghost 視窗移動至求得的位置，並調整前後順序（`--zorder=`）。

步驟 5 重新執行時，步驟 3 的兩點選擇和偏移量仍使用相同的值。只有供 ghost 坐的矩形會改變。

## 選項

選項格式為 `--名前=値`，全部都可以省略。省略的選項會使用預設值，而非上次呼叫時指定的值。無法解析的選項會被忽略。

| 選項 | 預設 | 內容 |
|---|---|---|
| `--target=` | `active` | 追蹤的目標。`active`：前景視窗 / `fix`：固定於畫面（工作區） / `@文字列`：視窗標題包含該字串的視窗（不區分大小寫） / `#数値`：視窗控制代碼為該數值的視窗 |
| `--origin=` | `osuwari` | 將 ghost 視窗的哪個點對齊目標（原點）。以 `左右.上下` 的格式指定（見下方「原點的寫法」）。也可以用 `tl` `tr` `bl` `br` 這樣的兩個字元指定角落 |
| `--target-origin=` | 省略（自動） | \[SSP 2.9.34\] 將 ghost 視窗的點對齊目標矩形的哪個點。格式與 `--origin=` 相同，但不能指定 `base` 和 `osuwari`（見下方「目標矩形的點」）。省略時，使用與 `--origin=` 的點相同的一側（`left` 為左邊緣、`right` 為右邊緣、`center`、`base`、`osuwari` 為中央） |
| `--x=` `--y=` | `0` | 從原點的偏移量（像素）。在指定了 `--xmove` `--ymove` 的方向上，這是在移動前使用的預設值 |
| `--interval=` | `100` | 檢查位置的間隔（毫秒）。小於 10 時使用 10 |
| `--xmove` `--ymove` | 無 | 允許在該方向透過拖曳移動（限於目標矩形內）。移動後的位置以可移動範圍中的比例記住（見下方「可透過拖曳移動的範圍」）。未指定的方向即使拖曳也會回到坐的位置。也可以寫成 `--xmove=false` |
| `--noclip` | 無 | 不進行超出畫面判定 |
| `--area=` | `workarea` | 無法坐上去或超出畫面時的基準。`desktop`：整個畫面 / `workarea`：工作區（排除工作列等的部分） |
| `--side=` | `center` | 無法坐上去或超出畫面時，相對於基準放置「虛擬視窗」的位置。`center`：基準本身 / `top` `left` `right` `bottom`：在基準的上、左、右、下側放置厚度為 100 像素的虛擬視窗 |
| `--margin=` | `0_0_0_0` | 超出畫面判定的容許範圍（像素）。依 `左_上_右_下` 的順序，以空格或 `_` 分隔。若為 `0_50_0_100`，向上超出 50、向下超出 100 像素以內都不視為超出畫面 |
| `--zorder=` | `front` | 與目標視窗的前後順序。`front`：顯示在目標正上方（前方） / `back`：顯示在目標緊後方（正下方）。未坐在目標上時（無法坐上去或 `--target=fix`）不做任何處理 |

- `--origin=` 和 `--area=` 在標籤及 `descript.txt` 中的預設值為 `osuwari` 和 `workarea`。內建 SAORI 的 `osuwari`（相容 Osuwari.dll）則配合原作，維持 `tl` 和 `desktop`。\[SSP 2.9.34\] 在 2.9.33 中，標籤和 `descript.txt` 的預設值也是 `tl` 和 `desktop`。
- 無法坐在目標上時（`--target=fix`、沒有目標視窗，或前景視窗無法坐上去且也沒有最近一次可坐上的視窗）以及超出畫面時（直接坐上去會超出畫面），會將 `--area` 和 `--side` 決定的基準矩形當作「虛擬目標」坐上去。`--target=fix` 不會進行超出畫面判定。
- 視窗矩形以可見邊框測量（不包含 Windows 10 以後的不可見邊框）。作為基準的畫面是目標視窗所在的螢幕（沒有目標時為 ghost 所在的螢幕；拖曳時為游標所在的螢幕）。超出畫面判定使用所有螢幕合併的區域。
- 無法坐在最小化或隱藏的視窗、其他虛擬桌面的視窗、對話方塊等有擁有者的視窗，以及 SSP 自身的視窗（`--target=active` 時）上。`--target=active` 時，也無法坐在明顯不應坐上的系統 shell 視窗上（桌面、Alt+Tab、工作檢視、開始、搜尋、IME 面板等由系統 shell 顯示的 UWP 視窗，以及 Windows 8 的 Metro 全螢幕視窗）。這類視窗位於前景時，會繼續坐在最近一次可坐上的視窗。透過 `@文字列`、`#数値` 自行指定的視窗不受此排除規則影響。
- 坐在目標上時，ghost 會顯示在目標視窗上方。只有當目標是最上層視窗（例如工作列）時，osuwari 才會讓 ghost 置頂（始終顯示在其他視窗前方），否則 ghost 不會置頂。不過，設定為「總是在前方顯示」的 ghost 會因該設定而保持置頂，不受目標影響。目標是最上層視窗時，ghost 也會顯示在目標上方（每次目標移至前景時，ghost 也會回到其上方）。
- 使用 `--zorder=back` 時，ghost 會顯示在目標視窗緊後方（Z 順序中正下方）。可用於從被目標遮住的位置探出頭等用途。即使其他應用程式的視窗插入其間，下次確認位置時（依 `--interval=` 的間隔）也會回到緊後方。目標是最上層視窗（例如工作列）時，ghost 也會置頂，並在最上層視窗的順序中排在目標正下方。設定為「總是在前方顯示」的 ghost 坐在非最上層視窗後方時，會優先遵循該設定而保持置頂（後方的指定不生效）。
- 若只要坐在工作列正上方（不追蹤視窗），可用 `--target=fix` 固定於畫面，並使用工作區下邊緣（例：`--target=fix,--origin=bl,--area=workarea,--side=center`。若要使用右邊緣，則指定 `--origin=br`）。由於工作區排除了工作列等部分，只有工作列位於畫面下方時，才會坐在其正上方。工作列位於畫面上方或左右兩側時，會坐在畫面下邊緣（工作區下邊緣）。設定自動隱藏工作列時，工作區會涵蓋整個畫面，因此會坐在畫面下邊緣。
- 指定其他對齊方式（`top` `bottom` `left` `right` `free`）、變更 shell 等操作會停止 osuwari。`default` 會還原為 ghost 的預設設定（`descript.txt`，詳見下文）。視窗模式期間會停止，回到一般模式後會恢復。
- 坐著時的位置不會儲存為站立位置。
- 在透過 sticky window 連動的視窗中，非父視窗的一側（連動的子視窗）會跟隨父視窗，因此即使指定 osuwari 也不生效。父視窗坐下時，子視窗會一起移動。
- `\0` 和 `\1` 可以分別指定。不過，ghost 視窗的前後順序以 ghost 為單位共用一組，因此多個角色坐下時，會由編號較小者的目標決定。

## 原點的寫法 \[SSP 2.9.34\]

`--origin=`會將 ghost 視窗上的點對齊目標矩形上的點。格式為`左右.上下`，`.`前面是 X 軸，後面是 Y 軸。各軸可填入下列詞語（不區分大小寫）。

| 詞語 | ghost 視窗上的點 | 目標矩形上的點（省略`--target-origin=`時） |
|---|---|---|
| `left`（X 軸）/ `top`（Y 軸） | 左端 / 上端 | 左端 / 上端 |
| `right`（X 軸）/ `bottom`（Y 軸） | 右端 / 下端 | 右端 / 下端 |
| `center` | 中央 | 中央 |
| `base` | surface 的基準位置（`point.basepos.x`、`point.basepos.y`；預設為腳下中央） | 中央 |
| `osuwari` | surface 的坐姿位置（`point.osuwaripos.x`、`point.osuwaripos.y`；預設與`base`相同） | 中央 |

- `base`和`osuwari`不加`.`而只寫一個詞時，會同時用於 X 軸和 Y 軸（`--origin=osuwari`等同於`osuwari.osuwari`）。其他詞只寫一個時，僅指定 X 軸，Y 軸為`top`。
- `tl`等同於`left.top`，`tr`等同於`right.top`，`bl`等同於`left.bottom`，`br`等同於`right.bottom`。
- 無法解析的寫法會被忽略（原點不變）。
- 目標矩形沒有`base`和`osuwari`，因此省略`--target-origin=`時會使用中央。例如，預設的`--origin=osuwari`會將 ghost 的坐姿位置對齊目標矩形的中央。可用`--x=`和`--y=`偏移坐姿位置，或用`--target-origin=`更改目標側的點。
- 例如：`--origin=center.bottom`會將 ghost 的中央（X）和下端（Y）對齊目標的中央（X）和下端（Y）。`--origin=right.osuwari`會將 ghost 的右端（X）和`point.osuwaripos.y`（Y）對齊目標的右端（X）和中央（Y）。

## 目標矩形上的點 \[SSP 2.9.34\]

`--target-origin=`用來決定與 ghost 視窗上的點重合的目標矩形側的點。格式與`--origin=`相同（`左右.上下`、`tl` `tr` `bl` `br`、單一詞語），但只能填入`left` `right` `top` `bottom` `center`。目標矩形沒有`base`和`osuwari`，因此填入這些詞時會視為無法解析的寫法而忽略。

- 省略時，會使用與`--origin=`的點相同的一側。`left`、`top`對應左端、上端，`right`、`bottom`對應右端、下端，`center`、`base`、`osuwari`對應中央（上表的右欄）。
- 只寫一個詞時，僅指定 X 軸，Y 軸為`top`。`--target-origin=center`等同於`center.top`（目標上端的中央）。
- 無法解析的寫法會被忽略（目標矩形上的點不變）。
- 坐下的對象是基準矩形時（無法坐下時），會使用基準矩形（包括虛擬視窗）上的點。
- 例如：`--origin=osuwari --target-origin=center.top`會將 surface 的坐姿位置對齊目標上端的中央。`--origin=center.bottom --target-origin=center.top`會將 ghost 的中央（X）和下端（Y）對齊目標的中央（X）和上端（Y）。ghost 的腳下會落在目標上端，不受 ghost 高度影響。
- 內建 SAORI 的`osuwari`（相容於 Osuwari.dll）沒有對應的引數。與以往一樣，會將 ghost 的角落對齊目標的同一個角落。

## surface 的坐姿位置 \[SSP 2.9.34\]

可在 shell 的`surfaces.txt`中的 surface 大括號區塊內，用`point.osuwaripos.x`、`point.osuwaripos.y`指定坐姿位置（[point.osuwaripos.x](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.x.md)、[point.osuwaripos.y](../../../descript/shell-surfaces/surface-brace/point.osuwaripos.y.md)）。這是`--origin=`的`osuwari`所使用的點；若未設定，則與`point.basepos.x`、`point.basepos.y`相同（若未設定這兩者，則使用其預設值）。

例如，對於寬度為 200、高度為 300 的 surface，若要將坐姿位置設在腰部，寫法如下。

```
surface0
{
point.osuwaripos.x,100
point.osuwaripos.y,250
}
```

此位置以從 surface 左上角起算的像素表示，並隨 surface 的縮放而縮放。它是與腳下的基準位置（`point.basepos`；未設定時為下端中央 (100,300)）不同的點，`--origin=base`使用基準位置，`--origin=osuwari`使用坐姿位置。

## 對齊範例

以下範例顯示上述 surface 坐在左上角為 (400,400)、右下角為 (1000,900) 的視窗上。`--origin=osuwari --target-origin=center.top`會將 ghost 的坐姿位置與目標上端的中央重合。

![使用 --origin=osuwari --target-origin=center.top 坐下時，ghost 視窗與目標的位置關係](../../../assets/image/osuwari-origin.svg)

由於坐姿位置 (100,250) 與目標上端的中央 (700,400) 重合，ghost 的左上角為 (700−100,400−250)=(600,150)。腳下的基準位置（預設為下端中央）位於坐姿位置下方 50 像素的 (700,450)，進入視窗上端以內。由於 ghost 顯示在目標前方，因此呈現坐在視窗邊緣的樣子。

- 若為每個 surface 設定`point.osuwaripos`，切換 surface 時也會重新調整坐姿，使坐姿位置落在邊緣上。
- 省略`--target-origin=`時，坐姿位置會與目標中央重合。若要讓 ghost 坐在邊緣，請以`--target-origin=center.top`等方式指定目標側的點。
- 也可以不使用坐姿位置，而以 ghost 的角落或邊緣對齊。`--origin=center.bottom --target-origin=center.top`會將 ghost 下端的中央對齊目標上端的中央（腳下會落在目標上）。
- 省略`--target-origin=`時，目標側的點一律與 ghost 側位於同一側，因此無法指定將下端對齊上端的組合。此時可使用`--origin=tr --y=-300`等方式，先將上端彼此對齊再偏移。此偏移量依 ghost 的高度設定，因此高度改變時腳下位置也會偏移。

## 無法坐在對象上及超出畫面時

無法坐在對象上，或坐上去會超出畫面時，會改為坐在基準矩形上。基準矩形依下列順序建立。

1. 使用 `--area=` 選擇對象所在螢幕的全域（`desktop`）或工作區域（`workarea`）。沒有對象時，使用 ghost 視窗所在的螢幕（拖曳時則使用游標所在的螢幕）。
2. 使用 `--side=` 選擇直接使用第 1 步的矩形（`center`），或使用置於其外側的虛擬視窗（`top` `left` `right` `bottom`）。虛擬視窗與基準的邊等長，厚度為 100 像素。

![--side= 建立的虛擬視窗與基準矩形的位置關係](../../../assets/image/osuwari-side.svg)

選擇 `bottom` 時，虛擬視窗的上緣會與基準的下緣重疊。若搭配 `--origin=osuwari --target-origin=center.top`，坐下位置就會落在基準下緣的中央（若基準是工作區域，就會坐在工作列的上緣）。若使用 `--origin=center.bottom --target-origin=center.top`，則 ghost 的下緣會落在該處，腳底站在基準的下緣。

坐在基準矩形上時，`--origin=`、`--target-origin=` 和 `--x=` `--y=` 的用法與坐在對象上時相同。

!!! note "註"
    如果使用 `--origin=osuwari --target-origin=center.top`，但 `--side=center` 保持不變（預設值），在退回基準矩形時，會坐在基準（整個工作區域）上緣的中央。坐下位置 (100,250) 會與 (960,0) 重疊，因此 ghost 的左上角會位於 (860,-250)，大部分會超出畫面。退回基準矩形後不會進行超出畫面判定，因此不會被拉回。若要讓 ghost 坐在畫面下緣，請搭配 `--side=bottom`。

**超出畫面判定**會檢查 ghost 的整個視窗（包含透明部分）是否容納於包圍所有螢幕的矩形內。

- `--margin=` 是將該矩形向外擴展的量。若為 `--margin=0_0_100_0`，向右超出 100 像素以內都不視為超出畫面。當 surface 的透明邊距只要超出畫面就會被判定為超出時，可使用此選項。
- `--noclip` 完全不進行超出畫面判定。視對象的位置而定，ghost 可能會一直停留在畫面外。
- 使用 `--target=fix` 或沒有對象時，不進行超出畫面判定（因為原本就坐在基準矩形上）。

## 可拖曳移動的範圍

預設情況下，即使拖曳 ghost 視窗，也無法使其離開坐下位置。`--xmove` 允許水平方向拖曳，`--ymove` 允許垂直方向拖曳。未指定的方向即使移動，也會回到坐下位置。

只能在所坐對象的矩形內移動。

- `--xmove`：ghost 視窗的左緣不小於對象的左緣，右緣不大於對象的右緣。
- `--ymove`：ghost 視窗的上緣不小於對象的上緣，下緣不大於對象的下緣。

坐在目標上時，所坐對象就是該目標；未坐在目標上時（使用 `--target=fix` 或退回基準矩形時），所坐對象就是基準矩形（包含虛擬視窗）。例如，`--target=fix --origin=bl --xmove` 會站在工作區域的下緣，且只能水平移動。

移動後的位置會依各方向，以可移動範圍內的比例記錄。比例 0 是 ghost 視窗的左緣（上緣）與對象的左緣（上緣）重疊的位置；比例 1 是右緣（下緣）與對象的右緣（下緣）重疊的位置。

- 移動之前，會坐在由 `--origin=` `--target-origin=` `--x=` `--y=` 決定的位置。這些是坐下時的預設值。
- 一旦移動，該方向就會優先使用比例，不再使用 `--origin=` 等設定。即使對象或 ghost 視窗的大小改變，仍會坐在相同比例的位置。切換對象或 surface 時也是如此。
- 只有 ghost 視窗從前次配置結果的位置被移動時（透過拖曳或 `\![move]`），才會更新比例。僅因對象移動或大小改變，不會更新比例。
- 無法移動的方向仍與以往相同，由原點、對象側的點及偏移量決定。
- 重新指定 `osuwari` 時，記錄的比例會被清除，並恢復預設值。
- 由於可移動範圍僅限於對象內側，一旦移動，就不會回到偏移至對象外側的位置（例如坐在對象上緣的位置）。若要回到該位置，請重新指定 `osuwari`。
- ghost 視窗大於對象時（可移動範圍為 0 或負值），無法確定比例。即使移動也不會記錄比例；若已有記錄的比例，則會對齊對象的左緣（上緣）坐下。若尚未移動過，則維持預設位置。

例如，對象的左上角為 (300,400)、右下角為 (1100,1000)，ghost 視窗寬 200、高 300，且使用 `--origin=tl --xmove` 時，初始左上角為 (300,400)。

- 拖曳左緣至 600 時（範圍為 300 到 900，正好是中間），比例為 0.5。
- 對象寬度變為 600（左上角為 (300,400)、右下角為 (900,1000)）時，範圍變為 300 到 700，左緣變為 500。
- 另一個視窗（左上角為 (1000,100)、右下角為 (1400,800)）移至最前方時，範圍變為 1000 到 1200，左緣變為 1100。

## 前後順序

坐下期間，ghost 視窗會維持與對象之間的前後順序。使用 `--zorder=` 選擇置於對象前方，或緊鄰對象後方。此選項與位置計算無關。

![使用 --zorder=front 與 --zorder=back 時，ghost 視窗與對象的前後順序](../../../assets/image/osuwari-zorder.svg)

- `front`：僅在 ghost 位於對象下方時，將其移至對象正上方。如果已位於對象上方則不移動（即使中間有其他視窗也一樣，以免與坐在同一視窗上的其他 ghost 爭奪順序）。
- `back`：保持在對象緊後方（正下方）。若中間出現其他應用程式的可見視窗，會在下次位置檢查時（依 `--interval=` 的間隔）移回正下方。

當對象是最前面的視窗（例如工作列）時，以及 ghost 設定為「永遠顯示於最前方」時，請參閱「選項」中的補充說明。

## 數值範例

以下顯示在指定條件下，ghost 視窗的左上角位置。

- ghost 視窗：寬度200、高度300。surface 的基準位置是預設的腳底中央(100,300)。坐姿位置是在`surfaces.txt`中寫入`point.osuwaripos.x,100`、`point.osuwaripos.y,250`所指定的(100,250)。
- 畫面：1920×1080。工作區域為1920×1040（工作列位於下方，高度40）。
- 目標：除非另有註明，左上角為(400,400)、右下角為(1000,900)。

省略`--origin=`和`--area=`的指定值，是以 SSP 2.9.34以後的預設值（`osuwari`和`workarea`）計算。2.9.33的預設值為`tl`和`desktop`，因此結果不同。

| 指定 | 左上角 | 內容 |
|---|---|---|
| `--origin=osuwari`（預設） | (600,400) | 坐姿位置(100,250)與目標的中央(700,650)重合。 |
| `--origin=osuwari --target-origin=center.top` | (600,150) | 坐姿位置與目標上緣的中央(700,400)重合。坐在視窗邊緣（上圖）。 |
| `--origin=tr --x=-20 --y=-300` | (780,100) | 將右上角對齊目標的右上角，再向左移20、向上移300。下緣(400)與目標的上緣重合，站在視窗上緣。 |
| `--origin=bl` | (400,600) | 將左下角對齊目標的左下角。下緣(900)與目標的下緣重合。 |
| `--origin=center.bottom --target-origin=center.top` | (600,100) | 將 ghost 的下緣中央對齊目標的上緣中央(700,400)。無論 ghost 的高度為何，都會站在視窗上緣。 |
| `--target=fix --origin=osuwari --target-origin=center.top --side=bottom` | (860,790) | 將坐姿位置與工作區域下方的虛擬視窗上緣中央(960,1040)重合。坐在工作區域的下緣。 |
| `--target=fix --origin=center.bottom --target-origin=center.top --side=bottom` | (860,740) | 將 ghost 的下緣中央對齊同一點。站在工作區域的下緣。 |
| 第3列的指定，目標最大化（左上角(0,0)、右下角(1920,1040)）。加上`--side=bottom` | (1700,740) | 上緣位於畫面外(-300)，因此超出畫面。回退至工作區域下方的虛擬視窗，以相同的`--origin=` `--x=` `--y=`坐下。下緣為1040（工作區域的下緣）。 |
| 從上列移除`--side=bottom` | (1700,-300) | 回退至工作區域本身。由於不判定是否超出畫面，因此坐在畫面外。 |
| `--target=fix --origin=bl` | (0,740) | 站在工作區域的左下角。若為`--origin=br`則是(1720,740)。 |
| `--target=fix` | (860,270) | 坐姿位置與工作區域的中央(960,520)重合。 |
| 目標為(1500,400)-(2000,900)。`--origin=tr --y=-300 --side=bottom` | (1720,740) | 右緣2000超過畫面的右緣1920，因此超出畫面。回退至工作區域下方的虛擬視窗。 |
| 在上列加上`--margin=0_0_100_0`或`--noclip` | (1800,100) | 由於允許向右超出100像素（或不進行判定），因此仍坐在目標上。 |

## 寫入 descript.txt

ghost、shell 的`descript.txt`中的`seriko.alignmenttodesktop`（包括帶有`sakura.`、`kero.`、`char*.`的項目）也可以寫入`osuwari`作為值。在值之後，以逗號分隔並排列與標籤相同的`--`選項（[※顯示位置資訊](../../../descript/shell/descript-txt/note-1.md#補足)）。

```
sakura.seriko.alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom
```

- 優先順序與其他值相同（ghost 端全域＜ghost 端個別 scope＜shell 端全域＜shell 端個別 scope）。
- 啟動 ghost、切換 shell 時，會依該設定開始追蹤。
- `\![set,alignmenttodesktop,default]`和內建 SAORI 的`osuwari`的`STOP`會還原為`descript.txt`的設定。若`descript.txt`為osuwari，則會重新以osuwari坐下。
- 無法解析的選項會在錯誤日誌中顯示警告並忽略。

## 與內建 SAORI 的關係

內建 SAORI 的`osuwari`（相容於 Osuwari.dll）也執行相同處理。不過，SAORI 的`START`會依照原作，在省略第7個以後的引數時沿用上次的值（[相容模組](../../../spec/saori-ex/compat.md)）。

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
