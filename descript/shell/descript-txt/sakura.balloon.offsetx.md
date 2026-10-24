# sakura.balloon.offsetx,座標

**カテゴリ:** descript.txt

本体側バルーン位置X座標。<br />
offsetx / offsety の後ろに方向を表す1文字を付けると、バルーンをどこに出すかによって違う値を使わせることができる(SSPのみ)。

- **offsetx / offsety**: 方向指定なし。下記が書かれていない時に使われる既定値。
- **offsetxl / offsetyl**: バルーンをシェルの左に出す時。
- **offsetxr / offsetyr**: バルーンをシェルの右に出す時。
- **offsetxc / offsetyc**: バルーンをシェルの頭上・足元に出す時。中央寄せになる2通りで共通。
- **offsetxb / offsetyb**: バルーンをシェルの足元に出す時。頭上と足元で違う値にしたい場合に使う。

書かれていない時に何が使われるかは以下の通り。X座標とY座標はそれぞれ独立に決まる。

- **offsetxb が無い時**: offsetxc → offsetx の順に探す。
- **offsetxc / offsetxl / offsetxr が無い時**: offsetx を使う。

どちらに出すかは、バルーンのdescript.txtの[windowposition.x](../../balloon/descript-txt/windowposition.x.md)、 シェルの[sakura.balloon.alignment](sakura.balloon.alignment.md)、 さくらスクリプトの[`\![set,balloonalign,ID]`](../../../list/sakura-script/balloon-text/bang-set-balloonalign-ID.md)で決まる。

**符号に注意。**X座標の＋はどの場合もシェルに近づく向きで、左に出す時は右方向、右に出す時は**左方向**が＋になる (頭上・足元は右方向が＋)。Y座標の＋は常に下方向。<br />
ただし0の位置(基準)が方向ごとに違う。左右はバルーンの上端とシェル画像の上端が揃う位置、頭上はバルーンの下端がシェル画像の上端に接する位置、足元はバルーンの上端がシェル画像の下端に接する位置。

**既定値:** ghostのdescript設定

**対応:** Materia / SSP / CROW
