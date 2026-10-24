# SERIKOの旧定義と新定義について

## SERIKOの新定義と旧定義とは

本家伺か（MATERIA）の開発末期のバージョンで、surfaces.txtへのSERIKO（アニメーション）に関する設定書式に変更がありました。<br />
これについて[本家仕様書](http://usada.sakura.vg/contents/seriko.html)にあるSERIKO/1.x系の従来書式の事を旧定義、対する公式にドキュメント化されないままとなった新たな書式（SERIKO/2.0）のことを新定義と呼ぶ事があります。

なお、*これとは全く別に*、MATERIA開発終了後にSSPなどがsufraces.txtの書式について独自に追加した記法などがあります（例えばsurface.appendや、surface1-9といった範囲指定）。<br />
これを含めて新定義と呼ぶ人や文献があるかもしれませんが、少なくともukadocで言う新旧定義はあくまでそのような用法ではなく、SERIKOの書式についての言葉である点に注意してください。

## 新定義と旧定義の違い

新定義における書式の変更点は以下の四つです。

1. [SERIKO関連の定義行](animation-star-.interval.md)を全て「animation」の語からはじめるように変更。
2. [pattern定義行](animation-star-.pattern-star.md)のパラメータの順序が変更された（描画メソッド指定を先頭に移動）。
3. pattern定義のウェイトパラメータの単位が、10ミリ秒から1ミリ秒に変更された。
4. 描画メソッドの[alternativestart](h-drowmethod/alternativestart.md)で、ID指定の括弧が\[\]から()に変更された。

これに加え、descriptブレスを設けて「[version,1](../descript-brace/version.md)」の定義を行うことが必要です。

以下は*同じ定義内容*の旧定義と新定義の例です。

```
// 旧定義
surface1
{
0interval,rarely
0pattern0,0,0,alternativestart,[1,2]

1interval,never
1pattern0,101,70,overlay,200,100
1pattern1,102,70,overlay,200,100
1pattern2,101,70,overlay,200,100
1pattern3,-1,70,overlay,0,0

2interval,never
2pattern0,101,70,overlay,200,100
2pattern1,102,70,overlay,200,100
2pattern2,101,70,overlay,200,100
2pattern3,-1,70,overlay,0,0
2pattern4,101,70,overlay,200,100
2pattern5,102,70,overlay,200,100
2pattern6,101,70,overlay,0,0
2pattern7,-1,70,overlay,0,0
}
```

```
// 新定義
surface1
{
animation0.interval,rarely
animation0.pattern0,alternativestart,(1,2)

animation1.interval,never
animation1.pattern0,overlay,101,700,200,100
animation1.pattern1,overlay,102,700,200,100
animation1.pattern2,overlay,101,700,200,100
animation1.pattern3,overlay,-1,700,0,0

animation2.interval,never
animation2.pattern0,overlay,101,700,200,100
animation2.pattern1,overlay,102,700,200,100
animation2.pattern2,overlay,101,700,200,100
animation2.pattern3,overlay,-1,700,0,0
animation2.pattern4,overlay,101,700,200,100
animation2.pattern5,overlay,102,700,200,100
animation2.pattern6,overlay,101,700,200,100
animation2.pattern7,overlay,-1,700,0,0
}
```

- アニメーションID
- パターンID
- サーフェスID
- 描画メソッド
- ウェイト
- x座標
- y座標

先頭が「animation」から始まるようになった他、ウェイトの数値が10倍になっていること、描画メソッドの指定がパラメータの先頭に移動したことに注意してください。<br />
またalternativestartは\[\]が()に変更されているほか、alternativestartの場合無視されるパラメータである「サーフェスID」「ウェイト」について、旧定義ではダミーの数値0を書いていたのに対し、新定義では描画メソッドが先頭に移動した関係から、「合成位置x,y」含めて丸ごと省略できていることもわかるかと思います。

## 新定義で記述する利点

- SSPが独自に追加した設定（このページにある項目で![Materia](../../../assets/image/icon_m.png)の表示がなく![SSP](../../../assets/image/icon_s.png)の表示のみがあるもの）については、旧定義で書かれる事が想定されていない場合があります。<br />
  今後追加されるあらゆる設定にも同様の事がいえます。<br />
  こうした設定を利用する場合は、新定義で記述することが望ましいでしょう（旧定義だと正常動作しない可能性がある）。<br />
  その場合、新旧定義を混在させるとエラーとなるので、新定義に統一する必要があります。
- ウェイトの単位が10msから1msに変更され、より細やかな設定が可能になります。
- また上例で見た通り、描画メソッドがパラメータの先頭に移動した事で、startやalternativestartのような特殊な描画メソッドで無視されるパラメータが綺麗に省略されることも利点かもしれません。
- 他に、「animation」の語句が明示される事で、SERIKOに関する定義のまとまりが強調され、よりその行の意味が解りやすくなる面もあるかもしれませんが、およそ見やすさというものは慣れや個人差によるところが大であり、旧定義の方が親しんでいるし見やすいというのも自然な感じ方です。

以上のような点にメリットを感じない場合、SSPのみでの対応を考えるなら必ずしも移行する意味はないかもしれません。

なお、UKADOCでは基本的にSERIKOに関しては新定義で記述を行っているため、旧定義の記述で書きたい場合は上記を参考に適宜読み替えてください。
