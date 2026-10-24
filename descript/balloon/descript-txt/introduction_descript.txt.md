# descript.txt（Balloonの）

## 概要

バルーンの基本設定ファイル。<br />
バルーン名や作者情報の他、パーツの表示位置や文字の表示に関することなどを設定する。

descript.txtはバルーン全体の標準設定であり、この設定の上でさらにバルーンの各サーフェスについて、それぞれの個別設定ファイルである[balloon(s/k)\*s.txt](../balloonsoption/index.md)で調整する設計になっている。

## 記述例と基本の書き方

```
charset,Shift_JIS
type,balloon
name,凡例さんの吹き出し
homeurl,http://ssp.shillest.net/ukadoc/manual/hogehoge/example/

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

origin.x,14
origin.y,14

validrect.left,0
validrect.top,0
validrect.right,0
validrect.bottom,-12

wordwrappoint.x,-20

font.color.r,0
font.color.g,0
font.color.b,0

cursor.blendmethod,mergepennot
cursor.style,square
cursor.brush.color.r,0
cursor.brush.color.g,127
cursor.brush.color.b,127
cursor.pen.color.r,0
cursor.pen.color.g,0
cursor.pen.color.b,0
cursor.font.color.r,0
cursor.font.color.g,0
cursor.font.color.b,0

arrow0.x,296
arrow0.y,8
arrow1.x,296
arrow1.y,-18

onlinemarker.x,16
onlinemarker.y,-27

sstpmarker.x,16
sstpmarker.y,-20
sstpmessage.x,28
sstpmessage.y,-21
sstpmessage.font.name,ＭＳ ゴシック
sstpmessage.font.height,7
number.font.name,Arial
number.font.height,10
number.font.color.r,0
number.font.color.g,0
number.font.color.b,0
number.xr,-28
number.y,-24

communicatebox.x,8
communicatebox.y,21
communicatebox.width,385
communicatebox.height,20
```

ゴーストやシェルのdescript.txtと比べても、設定が仕様上・事実上必須の項目が非常に多いという特徴がある。

SSPでは、バルーンに対してもhomeurlを設定しておくことで、エクスプローラなどからネットワーク更新が可能になる。

なお、\\や%で始まる文字列はさくらスクリプトや環境変数のタグと見なされ、セキュリティ上のリスクから破棄される。もし単なる文字としてそれらを含めたい場合は、\\\\や\\%などとしてエスケープする必要がある。
