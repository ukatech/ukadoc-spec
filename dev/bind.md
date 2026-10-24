# 着せ替えの設定

## 着せ替え

伺かのシェルには*着せ替え*を持たせることができます（着せ替え自体の説明は「Shell設定 - surfaces.txt」の「[着せ替え（MAYUNA）](../descript/shell-surfaces/surface-brace/introduction_mayuna.md)」を参照）。

着せ替えを利用すれば、オーナードローメニューから選択した場合に、単一のシェル内でキャラクターの外見の一部を切り替えたり、オン・オフすることができるようになります。

SSPの場合は[さくらスクリプトの命令](../list/sakura-script/surface/bang-bind.md)からも着せ替えを切り替えることが可能です。

着せ替えはMATERIA、SSPのみ可能で、CROWでは着せ替え初期配置のみで表示されます。

ただし、MATERIAはバグにより`\0`側しか着せ替えメニューが表示されません。

従って`\1`以降も含めて完全に実装されているのは実質SSPのみとなっています。

なおこのページの解説は、アニメーションの設定自体には一定の理解がある事が前提となっています。

アニメーション設定については、「シェルの作成」のページの「[surfaces.txtを書く - アニメーション編](shell.md#surfacestxtを書く---アニメーション編)」の節を参照してください。

## 目次

1. [surfaces.txtでの設定](bind.md#surfacestxtでの設定)
2. [descript.txtでの設定](bind.md#descripttxtでの設定)

1. （準備中）SSPの着せ替えメニュー設定あれこれ
2. （準備中）動きのある着せ替え
3. （準備中）ある着せ替えが他の着せ替えの前後にまたがる三次元構造の場合

## surfaces.txtでの設定

```
surface0
{
animation0.interval,bind
animation0.pattern0,add,100,0,0,0
animation0.pattern1,add,101,0,20,35
animation0.pattern2,reduce,102,0,0,0
animation0.pattern3,add,103,0,0,0
}
```

上記のように、intervalにbindを指定したアニメーションが、着せ替えになります。

add、reduceといった描画メソッドについては後述します。

ウェイト指定は0になっていますが、intervalがbindのアニメーションの（つまり着せ替えの）設定の場合、ウェイトに何を指定しても無視されます。

X座標・Y座標のオフセット位置指定は普通のアニメーションパターンと同様に指定できます。

また、animation0の「0」と言う数字は、アニメーションのIDですが、着せ替えの場合特にこのIDが重要になります。

### 着せ替えの描画メソッドについて

本家伺かでは着せ替えは基本的にbind、add、reduce、insertの4つのメソッドを使う事になっていました。

SSPでは、それに加えてbase、overlay、overlayfast、replace、interpolate、asisなどのメソッドが、通常のアニメーションと共通して使える事になっています。

ただし、startやstop、moveなどの単純に画像を合成するのでないメソッドは使用できません。

## descript.txtでの設定

descript.txtで行う内容は、一言で言えば着せ替えをオーナードローメニューの着せ替えメニューに表示するための準備です。

以下のように記述します。

```
sakura.bindgroup0.name,服,エプロンドレス,apron.png
sakura.bindgroup1.name,リボン,白リボン,ribbonwhite.png
sakura.bindgroup2.name,服,黒服,black.png
sakura.bindgroup3.name,リボン,黒リボン,ribbonblack.png

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

上記のように記述することで本体側の着せ替えメニューに「エプロンドレス」「黒服」「白リボン」「黒リボン」

相方側のメニューに「ネクタイ」「腕章」「腕」が出現し、それらを自由に着脱することができるようになります。

?.bindgroup\*は左から順に、カテゴリ名、パーツ名、サムネイルファイル名をカンマで区切って記述します。

この時「bindgroup\*」の\*の数字は、surfaces.txtで設定した着せ替えのアニメーションIDと対応します。

従って、全サーフェス間で、同じ服（着せ替え）に同じアニメーションIDが与えられていなければならないことに注意してください。

?.bindgroup\*.defaultは、アニメーションIDが「\*」の着せ替えを、そのシェルの着せ替えの初期値としてを設定します。

上例の設定ではデフォルトでエプロンドレス＆白リボン、ネクタイ＆黒腕章になります。

0を指定もしくは省略すると着せ替えOFF状態となる。

?.menuitem\*,\* はメニュー項目の構造を表しています。

メニュー表示順に番号を割り振り、カンマで区切りbindgroup\*の\*にあたる番号を指定します（ここでの指定はアニメーションIDではないので注意）。

bindgroupIDの代わりに「-」と記述すると、メニュー内のその位置にセパレータ（区切り線）が表示されます。

上例だと本体側着せ替えメニューの表示は、上から順に黒服、黒リボン、（セパレータ）、エプロンドレス、白リボンとなります。

サムネイルはメニュー選択時のガイドとして表示されます。

不要な場合省略して構いませんが、着せ替えの数が多い場合や、名前から着せ替え内容を連想し難いような場合には指定してあると便利でしょう。

## SSPの着せ替えメニュー設定あれこれ

準備中

## 動きのある着せ替え

準備中

## ある着せ替えが他の着せ替えの前後にまたがる三次元構造の場合

準備中
