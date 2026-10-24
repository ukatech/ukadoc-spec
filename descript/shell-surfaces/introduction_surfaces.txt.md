# surfaces.txt

## 概要

シェルの各種定義を行うためのファイル。基本的に全て省略可。必要なものだけ書く。<br />
例えば各サーフェス（表情・パーツ・コマ・着せ替えパーツ）へのアニメーション、当り判定、画像の合成などの設定はここで行う。<br />
またサーフェスIDに対して別名（エイリアス）を与えたい場合もここで設定できる。<br />
SSPではその他にも、当り判定にカーソルを乗せ続けた時に表示されるツールチップや、カーソル表示の変更などの設定も行える。

一方で、シェル名、シェル作者名などのシェルの基本情報に関する設定や、着せ替えのオーナードローメニュー（右クリックメニュー）の表示設定などはここではなく[descript.txt](../shell/index.md)で行うので注意。

## 基本の書式

基本的にほとんどの設定が*省略可能*であり、必要に応じて各設定を行えばよい。

設定は、書くとすれば必ず一行目に書く必要がある[charset](file/charset.md)の他は、それぞれ「\{」と「\}」で囲まれた各ブレス内に記述する（各ブレスについてはこのページ内のそれぞれの項目参照）。

「\{」および「\}」はそれのみが書かれた行として存在する必要があり、例えば「surface1 \{」のようにブレス名に続けて書く事はできない。

```
ブレス名
{
// 設定内容
}
```

ブレス名、\{\}、各設定として認識されない行はすべてコメント行として扱われる。慣例的には行頭を「//」から始める。

各行インデント可。

SSPのみ「surfaces\*\*\*.txt（\*\*\*は任意の文字列）」という名前のテキストファイルは全て読み込まれ、surfaces.txtと同様に扱われる。読み込み対象となるファイルが複数ある場合、読み込まれる順序はファイル名順となる。

なお、複数のsurfaces\*\*\*.txtを用意した場合、[descriptブレス](descript-brace/introduction_descriptbrace.md)の設定（および[charset](file/charset.md)）はそれぞれのファイルに設定する必要がある（逆に言うとそれぞれのファイルで異なる設定が可能）。

## 記述例

```
charset,Shift_JIS

descript
{
version,1
}

surface0
{
animation0.interval,sometimes
animation0.pattern0,overlay,101,100,168,67
animation0.pattern1,overlay,100,100,168,67
animation0.pattern2,overlay,101,100,168,67
animation0.pattern3,overlay,-1,100,168,67
}

surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face1.png,0,0
}

surface10
{
collision0,40,56,95,90,Head

sakura.balloon.offsetx,80
sakura.balloon.offsety,-100
kero.balloon.offsetx,-30
kero.balloon.offsety,20
}

// SSPのみで有効な記法 ←このようにコメント行は//から始める
surface.append0-9
{
collision0,188,25,252,63,Head
collision1,190,92,236,118,Face
collision2,180,191,220,222,Bust
collision3,154,311,248,362,Skirt
}
```
