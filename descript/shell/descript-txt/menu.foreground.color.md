# menu.foreground.color,色

**カテゴリ:** descript.txt

オーナードローメニューの、選択中(カーソルが載っている)項目の背景色。選択中の背景画像([menu.foreground.bitmap.filename](menu.foreground.bitmap.filename.md))が覆わない部分(画像を指定しない場合は項目全体)をこの色で塗る。<br />
色の指定は色名(`red` など)、`#RRGGBB`、`#RGB`のいずれか(`#`は省略可)。<br />
`menu.foreground.color.r` / `menu.foreground.color.g` / `menu.foreground.color.b` に0～255の数値を書いて、赤・緑・青を別々に指定することもできる。

ゴースト側のdescript.txtにも書ける。シェル側に書かれていればシェル側が優先され、書かれていなければゴースト側の値が使われる。

**既定値:** OSの選択項目(ハイライト)の色

**対応:** SSP
