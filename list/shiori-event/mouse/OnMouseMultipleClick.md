# OnMouseMultipleClick

**カテゴリ:** マウスイベント

3回以上連続でクリックされた際に発生。<br />
※SHIORIから同イベントに応答が無い場合、通常通りOnMouseClickとOnMouseDoubleClickの流れに戻る。

- **Reference0**: マウスカーソルの x 座標（ローカル座標）
- **Reference1**: マウスカーソルの y 座標（ローカル座標）
- **Reference2**: 常に0。
- **Reference3**: 本体の場合は0、相方の場合は1。それ以降2～
- **Reference4**: 当たり判定の識別子。
- **Reference5**: 左クリックは0、右クリックは1
- **Reference6**: マルチタッチ対応環境のタッチパネル（※タッチパッド不可）からの入力でtouch、ペンタブレットでpen、ペンタブの消しゴム側でeraser、マウスなどからの入力でmouse
- **Reference7**: 連続クリック回数

**対応:** SSP
