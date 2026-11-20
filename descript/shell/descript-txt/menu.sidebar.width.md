# menu.sidebar.width,数値

**カテゴリ:** descript.txt

オーナードローメニューの、サイドバーの幅(ピクセル)。0は指定なしと同じ扱いになる。<br />
サイドバー画像([menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md))より大きい値を指定すると、余った部分を[menu.sidebar.color](menu.sidebar.color.md)で塗る。画像も[menu.sidebar.text](menu.sidebar.text.md)もなく、この値だけを指定した場合は、その幅のサイドバーが色だけで表示される。

ゴースト側のdescript.txtにも書ける。シェル側に書かれていればシェル側が優先され、書かれていなければゴースト側の値が使われる。

**既定値:** サイドバー画像の幅(画像がなく[menu.sidebar.text](menu.sidebar.text.md)だけがある場合は、文字の高さに合わせた幅)

**対応:** SSP
