# OnMouseGesture

**カテゴリ:** マウスイベント

マウスを右ドラッグまたはホイールをドラッグした際に発生。<br />
なおSSP2.3.53以降、タッチパネル環境でOnMouseGestureのReference5がupまたはdownであるようなものに対してSHIORIが何も返さなかった（204 No Contentが返された）場合、代替イベントとして[OnMouseWheel](OnMouseWheel.md)が発生する。詳細はOnMouseWheelの節を参照。

- **Reference0**: 本体の場合は0、相方の場合は1。SSP/CROWでは2以降もある。
- **Reference1**: マウスカーソルの xy 座標（バイト値1区切り）
- **Reference2**: 当たり判定の識別子。
- **Reference3**: 右ドラッグを開始したマウスカーソルの xy 座標（バイト値1区切り）
- **Reference4**: 右ドラッグを開始した当たり判定の識別子。
- **Reference5**: ジェスチャー方向。<br />
  left_up(左上) up(上) right_up(右上)<br />
  left(左) right(右)<br />
  left_down(左下) down(下) right_down(右下)<br />
  circle.cw(時計回り) circle.ccw(反時計回り)<br />
  end(右ボタンをはなした)
- **Reference6**: ジェスチャー移動角度。<br />
  右0度から反時計回りに360度。

**対応:** SSP
