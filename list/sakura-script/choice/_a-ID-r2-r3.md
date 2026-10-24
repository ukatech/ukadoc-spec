# `\_a[ID,r2,r3...]`

**カテゴリ:** 選択肢コマンド

`\_a`がくるまでの範囲をアンカーとする。選択肢タイムアウトしないが、通常トーク同様バルーンタイムアウトする。<br />
ジャンパをクリックするとSHIORIイベント[OnAnchorSelect*Ex*](../../shiori-event/choice/OnAnchorSelectEx.md)が開始される。<br />
ジャンパとなったテキストがReference0に、IDはReference1に、続く引数はReference2以降に格納される。<br />
OnAnchorSelectExに続けてOnAnchorSelectも発生するが、Reference1以降に何も入らずこの書き方では無意味。

**対応:** SSP

## 記述例

```sakurascript
\_a[CharactorName,対象テディ,年齢不詳]テディ\_aはいいやつだったのに。\_a[CharactorName,対象エミリ,0x10歳]エミリ\_aのとっておきのおやつを食べたばかりに……。アンカークリック時、OnAnchorSelectExイベントが発生する。「テディ」をクリックした場合、reference0に「テディ」、reference1に「CharactorName」、reference2に「対象テディ」、reference3に「年齢不詳」が格納されている。
```
