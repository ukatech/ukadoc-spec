# OnMouseDown

**カテゴリ:** マウスイベント

左・右のマウスボタンが押された際に発生。

- **Reference0**: マウスカーソルの x 座標（ローカル座標）
- **Reference1**: マウスカーソルの y 座標（ローカル座標）
- **Reference2**: 常に0。
- **Reference3**: 本体の場合は0、相方の場合は1。SSP/CROWでは2以降もある。
- **Reference4**: 当たり判定の識別子。
- **Reference5**: 左クリックは0、右クリックは1、中クリックは2(互換仕様：OnMouseClickExへの移行を推奨)。
- **Reference6**: マルチタッチ対応環境のタッチパネル（※タッチパッド不可）からの入力でtouch、ペンタブレットでpen、ペンタブの消しゴム側でeraser、マウスなどからの入力でmouse

**対応:** SSP / Ninix
