# このページの書式について

このページでは、SHIORI/3.0および3.1（SSP拡張定義）において発行されるSHIORI Eventの各IDについての解説しています。<br />
ここに載っていないイベントについては、[SHIORI Resource](../shiori-resource/index.md)または[外部からのSHIORI Event](../shiori-event-ex/index.md)のページにある可能性があります。

SHIORI Event自体についての解説が必要な場合は、「[補足: SHIORI Eventとは](../../memo/shiori-event.md)」のページを参考にしてください。

## Reference一覧について

ReferenceがあるSHIORI Eventについては、それぞれReferenceの一覧が設けられています。<br />
もしReferenceの番号部分が「\*」となっている場合、それは不定数のReferenceである事を意味します。<br />
すなわち、そのReferenceは*動作環境によって数が異なるものを扱っているために番号が不定*であり、またその不定数のReferenceは*全て同じ形式の内容*だということです。<br />
この場合でもReferenceには0から始まる通し番号が与えられる原則は変わらないので、例えばReference一覧に番号が\*のものしかない場合は、0から不定の番号まで同じ形式のReferenceが（その環境に応じた数だけ）並び、もし一覧にReference2までがあってその次の行がReference\*ならば、3から不定の番号まで同じ形式のReferenceが並びます。

## \[NOTIFY\]表示について

説明文中に*\[NOTIFY\]*と記載があるSHIORI Eventは、普通NOTIFYコマンドで発行されます。<br />
何も記載がない場合は普通GETコマンドで発行されます。
