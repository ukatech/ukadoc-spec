# `\![enter,selectmode,モード(rect),左,上,右,下]\![enter,selectmode,モード(rect),当たり判定名]\![enter,selectmode,モード(rect)]`

**カテゴリ:** 未分類指令

開始選取模式。執行後會顯示透明區域，並可用滑鼠拖曳指定區域。<br />
執行後會觸發 [OnSelectModeBegin](../../shiori-event/select-region-mode/OnSelectModeBegin.md)。另請參閱 OnSelectModeMouseUp、OnSelectModeMouseDown、OnSelectModeCancel、OnSelectModeComplete。<br />
目前只能指定表示矩形選取模式的 "rect"。若未指定，則視同指定 rect。<br />
可在模式之後指定選取區域的初始位置。可指定座標，或指定要設定為相同大小的碰撞判定名稱。<br />
在此模式下不會重新繪製 surface。即使執行 Sakura Script (`\s[ID]`) 或 dressup，畫面也不會改變，但變更會套用，並在執行 `\![leave,selectmode]` 時繪製。

持續生效至 ghost 結束。

**対応:** SSP

## 記述例

```sakurascript
\![enter,selectmode,rect,head]セレクトモードを開始する。判定名headの範囲が初期選択されている。
```
