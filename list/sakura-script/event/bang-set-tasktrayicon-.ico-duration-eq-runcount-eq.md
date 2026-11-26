# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数)(,--interval=再生間隔))]`

**カテゴリ:** イベントコマンド

指定したアイコンファイルを通知領域（タスクトレイ）のアイコンに適用する。<br />
ファイル名には、\[実行したゴーストのフォルダ\]から、または\[実行したゴーストのフォルダ\]/ghost/masterからの相対パスが使用可能。<br />
テキストはアイコンにマウスを重ねたときの表示、省略可。デフォルトでは「SSP/Emily/Phase4.5」など、SSP/\[起動中のゴースト名\]。<br />
--duration=待機時間(ms)を指定すると、アイコンをアニメーションさせることができる。この時、ファイル名.icoを指定すると、ファイル名00.ico・ファイル名01.ico…のように後ろの数字順に複数読み込んで、指定した待機時間（ミリ秒）ごとにアニメーション表示する。 \[SSP 2.5.58～\]<br />
さらに --runcount を指定するとアニメーションの繰り返し回数を設定できる。指定がない場合は無限に繰り返す。 \[SSP 2.5.59～\]

## アニメーション画像の指定

ファイル名には .ico のほか、アニメーション画像（ANI・GIF・APNG・WebP）や静止画（PNGなど）も指定できる。連番の.icoを用意しなくても、画像1枚でアニメーションさせられる。 \[SSP 2.9.40～\]

- アニメーション画像はファイルに入っている各コマの待ち時間とループ回数のとおりに動く。--duration は不要。
- --duration=待機時間(ms)を指定すると、全コマの待ち時間をその値に上書きする（下限は50ミリ秒）。
- コマ画像は通知領域のアイコンの大きさに縮小して使う（表示倍率100%で16px角、150%で24px角、200%で32px角。表示倍率が変わると、新しい大きさで作り直す）。正方形でない画像は比率を保ったまま中央に収める。
- .ico（連番を含む）は従来どおり、--duration を指定したときだけアニメーションする。
- この指定はSSPのみで使える。他のベースウェアは .ico しか読めない。

## 再生のしかた

--interval=再生間隔 で、アニメーションが動くタイミングを指定できる（SSPのみ）。語は surfaces.txt の[アニメーションインターバル](../../../descript/shell-surfaces/surface-brace/h-animationinterval/introduction_animationinterval.md)と同じ。 \[SSP 2.9.40～\]

| 再生間隔 | 動き |
| --- | --- |
| always | 止まらず無限に繰り返す。ファイルが持つループ回数は無視する。 |
| runonce | 1回再生して止まる。 |
| runcount,N | N回再生して止まる。--runcount=N と同じ。 |
| never | 再生しない。1コマ目で止まっている。 |
| rarely | 毎秒4分の1の確率で1回再生する。 |
| sometimes | 毎秒2分の1の確率で1回再生する。 |
| random,N | 毎秒N分の1の確率で1回再生する。Nを省略すると2。 |
| periodic,N | 再生が終わってからN秒ごとに1回再生する。Nを省略すると1。 |

- どれも再生が終わったら最後のコマで止まる（surfaces.txtのアニメーションと同じ）。random・periodic・rarely・sometimes は最初は1コマ目で止まっていて、再生のたびに1コマ目から始まる。再生のあと先頭の絵に戻したいときは、最後のコマを先頭と同じ絵にしておく。
- --interval を指定しないときは、--runcount があればそれに従い、なければファイルが持つループ回数に従う（ANI は無限。GIF は NETSCAPE 拡張が無ければ1回で止まる）。連番の.icoは無限。
- --interval と --runcount の両方を指定したら --interval が優先される。ただし random・periodic・rarely・sometimes では、1回の再生あたりの繰り返し回数として --runcount が使われる（指定がなければ1回）。
- `--interval=random,5` のようにカンマで区切って書ける（`--interval=random:5` とも書ける）。
- 指定した --duration・--runcount・--interval はゴーストの最小化・復帰のあとも保たれる。アイコンを既定に戻すときは、ファイル名を空にして `\![set,tasktrayicon,]` と実行する（テキストは戻らない）。テキストも含めて戻すときは、下の `--reset` を使う。

## 指定をすべて取り消す（--reset）

`\![set,tasktrayicon,--reset]` のように、ファイル名の代わりに --reset を書くと、このタグで指定したものをすべて取り消して、descript.txt の指定に戻す。 \[SSP 2.9.40～\]

- ファイル名・テキスト・--duration・--runcount・--interval が取り消される。
- アイコンは descript.txt の[icon](../../../descript/ghost/descript-txt/icon.md)（最小化中は[icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md)）に、テキストは既定の「SSP/\[起動中のゴースト名\]」（最小化中は「SSP\[Minimize\]/\[起動中のゴースト名\]」）に戻る。
- --reset のあとに書いた引数は無視される。
- ファイル名を空にした `\![set,tasktrayicon,]` はアイコンだけを戻し、このタグで指定したテキストはそのまま残る。

descript.txtの[icon](../../../descript/ghost/descript-txt/icon.md)・[icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md)で指定したアイコンも同じようにアニメーションさせられる（再生のしかたは[icon.interval](../../../descript/ghost/descript-txt/icon.interval.md)・[icon.minimize.interval](../../../descript/ghost/descript-txt/icon.minimize.interval.md)で指定する）。

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```

```sakurascript
\![set,tasktrayicon,alert.gif,通知あり,--interval=periodic,10]アイコンを alert.gif のアニメーションにし、再生が終わるたびに10秒待ってからもう一度再生する。
```

```sakurascript
\![set,tasktrayicon,--reset]このタグで指定したアイコンとテキストをすべて取り消して、descript.txtの指定に戻す。
```
