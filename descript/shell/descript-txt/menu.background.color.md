# menu.background.color,色

**カテゴリ:** descript.txt

オーナードローメニューの、通常時の項目の背景色。背景画像([menu.background.bitmap.filename](menu.background.bitmap.filename.md))が覆わない部分(画像を指定しない場合は項目全体)をこの色で塗る。<br />
色の指定は色名(`red` など)、`#RRGGBB`、`#RGB`のいずれか(`#`は省略可)。<br />
`menu.background.color.r` / `menu.background.color.g` / `menu.background.color.b` に0～255の数値を書いて、赤・緑・青を別々に指定することもできる。

ゴースト側のdescript.txtにも書ける。シェル側に書かれていればシェル側が優先され、書かれていなければゴースト側の値が使われる。

**既定値:** OSのメニュー色

**対応:** SSP
