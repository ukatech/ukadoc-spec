# descript.txt（Shellの）

## 概要

シェルの基本設定ファイル。<br />
シェル名や作者情報の他、バルーンの表示位置設定や、オーナードローメニュー（右クリックメニュー）の画像設定、着せ替えのオーナードローメニューでの表示設定などもここで行う。

## 記述例と基本の書き方

```
charset,Shift_JIS
type,shell
name,master

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

menu.background.bitmap.filename,menu_background.png
menu.foreground.bitmap.filename,menu_foreground.png
menu.sidebar.bitmap.filename,menu_sidebar.png

sakura.balloon.offsetx,0
sakura.balloon.offsety,80
kero.balloon.offsetx,-20
kero.balloon.offsety,10
sakura.balloon.alignment,none
kero.balloon.alignment,none

sakura.bindgroup0.name,服,エプロンドレス,apron
sakura.bindgroup1.name,リボン,白リボン,ribbonwhite
sakura.bindgroup2.name,服,黒服,black
sakura.bindgroup3.name,リボン,黒リボン,ribbonblack
sakura.bindgroup0.default,1
sakura.bindgroup1.default,1

kero.bindgroup0.name,ネクタイ,ネクタイ
kero.bindgroup1.name,腕章,黒腕章
kero.bindgroup2.name,腕,ドリル
kero.bindgroup0.default,1
kero.bindgroup1.default,1

sakura.menuitem0,2
sakura.menuitem1,3
sakura.menuitem2,-
sakura.menuitem3,0
sakura.menuitem4,1

kero.menuitem0,0
kero.menuitem1,1
kero.menuitem2,-
kero.menuitem3,2
```

type、nameは必須。

SSPでは、シェルに対してもhomeurlを設定しておくことで、エクスプローラなどからネットワーク更新が可能になる。

着せ替え設定の各項目については後述のそれぞれの節を参照。<br />
基本的な仕組みは、[surfaces.txt](../../shell-surfaces/index.md)で定義した、タイミングbindのanimationIDに対して、着せ替え名と着せ替えカテゴリ名を与え（sakura(kero).bindgroup\*.name,～）、またオーナードローメニュー上での配置を指定する必要がある（sakura(kero).menuitem\*,～）。

なお、\\や%で始まる文字列はさくらスクリプトや環境変数のタグと見なされ、セキュリティ上のリスクから破棄される。もし単なる文字としてそれらを含めたい場合は、\\\\や\\%などとしてエスケープする必要がある。
