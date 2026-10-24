# OnMouseWheel

**カテゴリ:** マウスイベント

マウスホイールが回転した際に発生。<br />
SSP2.3.53以降、タッチパネル環境であった場合に、[OnMouseGesture](OnMouseGesture.md)のReference5がupまたはdownであるようなものに対してSHIORIが何も返さなかった（204 No Contentが返された）時にも代替イベントとしてOnMouseWheelが発生する。その場合Reference2の数値は元々のOnMouseGestureの移動量とup・downの方向から変換される（upなら正数、downなら負数）。

- **Reference0**: マウスカーソルの x 座標（ローカル座標）
- **Reference1**: マウスカーソルの y 座標（ローカル座標）
- **Reference2**: マウスホイールの回転量および回転方向。
- **Reference3**: 本体の場合は0、相方の場合は1。SSP/CROWでは2以降もある。
- **Reference4**: 当たり判定の識別子。
- **Reference5**: ※SSP/NINIXのみ　常に0。
- **Reference6**: ※SSP/NINIXのみ　マルチタッチ対応環境のタッチパネル（※タッチパッド不可）からの入力でtouch、ペンタブレットでpen、ペンタブの消しゴム側でeraser、マウスなどからの入力でmouse

**対応:** Materia / SSP / CROW / Ninix
