# menu.sidebar.color,色

**カテゴリ:** descript.txt

オーナードローメニューの、サイドバーの背景色。サイドバー画像([menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md))が覆わない部分をこの色で塗る。サイドバー画像がなく、[menu.sidebar.text](menu.sidebar.text.md)または[menu.sidebar.width](menu.sidebar.width.md)だけを指定した場合は、サイドバー全体をこの色で塗る。<br />
色の指定は、色名(`red` など)、`#RRGGBB`、`#RGB`のいずれか(`#`は省略可)。<br />
`menu.sidebar.color.r` / `menu.sidebar.color.g` / `menu.sidebar.color.b` に0～255の数値を書いて、赤・緑・青を別々に指定することもできる。

ゴースト側のdescript.txtにも書ける。シェル側に書かれていればシェル側が優先され、書かれていなければゴースト側の値が使われる。

**既定値:** [menu.foreground.color](menu.foreground.color.md)と同じ色

**対応:** SSP
