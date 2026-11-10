# `\_a[ID,r2,r3...]`

**カテゴリ:** 選項指令

將直到`\_a`為止的範圍設為錨點。選項不會逾時，但與一般對話相同，氣球會逾時。<br />
點擊跳轉文字後，會觸發 SHIORI 事件[OnAnchorSelect*Ex*](../../shiori-event/choice/OnAnchorSelectEx.md)。<br />
跳轉文字會存入 Reference0，ID 會存入 Reference1，後續引數則會依序存入 Reference2 以後。<br />
OnAnchorSelectEx 之後也會觸發 OnAnchorSelect，但 Reference1 以後沒有資料，因此這種寫法沒有意義。

**対応:** SSP

## 記述例

```sakurascript
\_a[CharactorName,対象テディ,年齢不詳]テディ\_aはいいやつだったのに。\_a[CharactorName,対象エミリ,0x10歳]エミリ\_aのとっておきのおやつを食べたばかりに……。アンカークリック時、OnAnchorSelectExイベントが発生する。「テディ」をクリックした場合、reference0に「テディ」、reference1に「CharactorName」、reference2に「対象テディ」、reference3に「年齢不詳」が格納されている。
```
