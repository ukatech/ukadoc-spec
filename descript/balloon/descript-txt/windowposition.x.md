# windowposition.x,座標

**カテゴリ:** descript.txt

バルーンの基本位置からのx座標方向の位置調整。<br />
ピクセル単位で数値で指定するか、キーワードで指定する。<br />
数値指定の場合、**バルーンを左右どちらに出していても常に右方向が+**。シェルの[balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md)と違い、右に出す時も符号が反転しないので注意。<br />
center(SSPのみ top でも同じ)でシェルの中央上に固定。<br />
bottom (SSPのみ)でシェルの中央下に固定。<br />
上記以外の文字列(left、right、free など)は受け付けず、0として扱われる。SSPではエラーログに警告を出す。<br />
またSSPに限り、descript.txtにも書ける。

**既定値:** 0

**対応:** Materia / SSP / CROW
