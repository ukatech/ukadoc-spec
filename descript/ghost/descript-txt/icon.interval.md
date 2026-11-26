# icon.interval,再生間隔

**カテゴリ:** descript.txt

[icon](icon.md)で指定したアニメーション画像（ANI・GIF・APNG・WebP）の、アニメーションが動くタイミング。
指定できる語は[\![set,tasktrayicon]](../../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)の --interval と同じ（always・runonce・runcount,N・never・rarely・sometimes・random,N・periodic,N）。descript.txtでは `icon.interval,random,5` のようにそのまま書ける。

指定がなければ、ファイルが持つループ回数に従う。再生が終わったら最後のコマで止まる。
タグ（`\![set,tasktrayicon]`）で指定したアイコンには使われない（タグの --interval だけが使われる）。

**既定値:** 値なし（ファイルが持つループ回数に従う）

**対応:** SSP 2.9.40
