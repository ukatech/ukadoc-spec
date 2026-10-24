# currentghost.balloon.scope(ID).vertical

**カテゴリ:** プロパティシステム

現在のバルーンが[縦書き](../../../descript/balloon/descript-txt/vertical.md)かどうか。縦書きなら1、横書きなら0。<br />
[validwidth](currentghost.balloon.scope-ID-.validwidth.md)・[validheight](currentghost.balloon.scope-ID-.validheight.md)は縦書きでも名前どおり「画面上の向き」の値で、縦書きではvalidwidthが「列が進む方向に使える幅」、validheightが「1列の長さ」になる。[lines](currentghost.balloon.scope-ID-.lines.md)は縦横どちらでも「収まる行数」（縦書きでは列数）を示す。<br />
1行（1列）に何文字入るかを計算したい場合は、縦書きならvalidheight、横書きならvalidwidthを見ること。この判別のためにこのプロパティを使う。<br />
※SSP 2.8.83で仕様変更。2.8.80では縦書き時のvalidwidth・validheightが「文字の送り方向を基準にした向き」の値だった。

**対応:** SSP 2.8.80
