# (入力ボックス種類).defaultleft　(入力ボックス種類).defaulttop

**カテゴリ:** ゴースト情報

入力ボックスの初期スクリーンX・Y座標。leftがX、topがY。leftとtopの両方を返したときだけ有効。<br />
ユーザーが入力ボックスを動かした位置を記憶している場合は、そちらが優先される。<br />
負の値は、本体側が表示されているモニタの作業領域の右端/下端から、入力ボックスの右端/下端までの距離になる。-0で右端/下端にぴったり付く。\[2.9.13\]<br />
-を2つ重ねると負の座標そのものになる(--100は座標-100)。\[2.9.13\]<br />
ボックス種類は以下の通り：communicatebox、scriptbox、addressbar、teachbox、dateinput、timeinput、ipinput、sliderinput、passwordinput、inputbox

**対応:** SSP
