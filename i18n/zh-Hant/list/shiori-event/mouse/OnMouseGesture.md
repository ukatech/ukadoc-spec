# OnMouseGesture

**カテゴリ:** 滑鼠事件

以滑鼠右鍵拖曳或拖曳滾輪時觸發。<br />
另外，自SSP2.3.53起，在觸控面板環境中，若SHIORI未回應Reference5為up或down的OnMouseGesture（回傳204 No Content），則會觸發[OnMouseWheel](OnMouseWheel.md)作為替代事件。詳情請參閱OnMouseWheel一節。

- **Reference0**: 本體為0，搭檔為1。SSP/CROW中也有2以上的值。
- **Reference1**: 滑鼠游標的 xy 座標（以位元組值1分隔）
- **Reference2**: 命中判定的識別碼。
- **Reference3**: 開始右鍵拖曳時滑鼠游標的 xy 座標（以位元組值1分隔）
- **Reference4**: 開始右鍵拖曳時的命中判定識別碼。
- **Reference5**: 手勢方向。<br />
  left_up(左上) up(上) right_up(右上)<br />
  left(左) right(右)<br />
  left_down(左下) down(下) right_down(右下)<br />
  circle.cw(順時針) circle.ccw(逆時針)<br />
  end(放開右鍵)
- **Reference6**: 手勢移動角度。<br />
  從右方的0度起，以逆時針方向增加至360度。

**対応:** SSP
