# sakura.balloon.offsetx,座標

**カテゴリ:** surfaceブレス

そのサーフェスでのみの本体側バルーン位置X座標。<br />
offsetx / offsety の後ろに方向を表す1文字を付けると、バルーンをどこに出すかによって違う値を使わせることができる(SSPのみ)。

- **offsetx / offsety**: 方向指定なし。下記が書かれていない時に使われる既定値。
- **offsetxl / offsetyl**: バルーンをシェルの左に出す時。
- **offsetxr / offsetyr**: バルーンをシェルの右に出す時。
- **offsetxc / offsetyc**: バルーンをシェルの頭上・足元に出す時。中央寄せになる2通りで共通。
- **offsetxb / offsetyb**: バルーンをシェルの足元に出す時。頭上と足元で違う値にしたい場合に使う。

offsetxb が無ければ offsetxc、それも無ければ offsetx が使われる。 offsetxc / offsetxl / offsetxr が無い時は offsetx が使われる。X座標とY座標はそれぞれ独立に決まる。<br />
ここで書いた値は、シェルの[descript.txt](../../shell/descript-txt/sakura.balloon.offsetx.md)に書いた同名の値より優先される。

符号の向きは[descript.txtのsakura.balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md)と同じ。

**既定値:** 左右に出す時：バルーンの左右端と、サーフェスの右左端が揃う位置<br />
頭上・足元に出す時：サーフェスの中央

**対応:** Materia / SSP / CROW
