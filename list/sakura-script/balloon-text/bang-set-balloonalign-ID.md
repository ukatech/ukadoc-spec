# `\![set,balloonalign,ID]`

**カテゴリ:** バルーン、テキストコマンド

バルーンを下記IDの表示方向へ切り替える。IDは以下の方法が定義可能である。<br />
下記の位置を基準に、[シェルのdescript.txtのballoon.offsetx及びballoon.offsetyの値](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md)、[surfaces.txtのballoon.offsetx及びballoon.offsetyの値](../../../descript/shell-surfaces/surface-brace/sakura.balloon.offsetx.md)が反映される。初期値none。

ゴースト終了まで有効。

- **left**: シェルの左上座標に、バルーンの右上座標が接する。
- **center**: シェルの中央上座標に、バルーンの中央下座標が接する。
- **top**: centerと同じ。
- **right**: シェルの右上座標に、バルーンの左上座標が接する。
- **bottom**: シェルの中央下座標に、バルーンの中央上座標が接する。
- **none**: 座標によってleftとrightが入れ替わる。シェルのドラッグ移動後、バルーンが見切れる場合、スイッチする。
- **上記以外**: noneと同じ。

方向ごとに違うオフセット値を使わせることもできる。 left/rightではoffsetxl/offsetxr、center・topではoffsetxc、bottomではoffsetxb(無ければoffsetxc)が優先される。 詳しくは[sakura.balloon.offsetx](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md)を参照。

**対応:** SSP

## 記述例

```sakurascript
\0\![set,balloonalign,top]本体側バルーンを、シェルの頭上に表示。\1\![set,balloonalign,right]相方側バルーンを、シェルの右側に表示。
```
