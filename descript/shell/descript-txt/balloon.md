# balloon,バルーン名

**カテゴリ:** descript.txt

このシェルの標準バルーン名。ユーザーがバルーンを明示的に切り替えていないとき、このシェルに切り替えると、このバルーンに自動で切り替わる。<br />
ユーザーが明示的に切り替えたバルーンがある場合は、そちらが優先される。ゴースト側の[recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md)（推奨バルーン）がある場合も、そちらが優先される。<br />
ゴースト側のdescript.txtの[balloon](../../ghost/recommended-balloon/balloon.md)（標準バルーン）にも書ける。シェル側に書かれていればシェル側が優先され、書かれていなければゴースト側の値が使われる。<br />
標準に従って切り替わっただけでは、ユーザーが明示的に切り替えたことにはならない。そのため、別のシェルに切り替えれば、そのシェルの定義に従って再び切り替わる。<br />
複数書いた場合は、見つかった最初のバルーンが使われる([default.balloon.path](default.balloon.path.md)の指定が先)。

**既定値:** ghostのdescript設定

**対応:** SSP
