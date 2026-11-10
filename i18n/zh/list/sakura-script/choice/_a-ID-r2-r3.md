# `\_a[ID,r2,r3...]`

**カテゴリ:** 选项命令

将`\_a`之前的范围设为锚点。选项不会超时，但与普通对话一样会触发气球超时。<br />
点击跳转链接时，将触发 SHIORI 事件[OnAnchorSelect*Ex*](../../shiori-event/choice/OnAnchorSelectEx.md)。<br />
跳转链接对应的文本存入 Reference0，ID 存入 Reference1，后续参数依次存入 Reference2 及之后的项目。<br />
在 OnAnchorSelectEx 之后也会触发 OnAnchorSelect，但 Reference1 之后没有任何内容，因此这种写法下该事件没有意义。

**対応:** SSP

## 記述例

```sakurascript
\_a[CharactorName,対象テディ,年齢不詳]テディ\_aはいいやつだったのに。\_a[CharactorName,対象エミリ,0x10歳]エミリ\_aのとっておきのおやつを食べたばかりに……。アンカークリック時、OnAnchorSelectExイベントが発生する。「テディ」をクリックした場合、reference0に「テディ」、reference1に「CharactorName」、reference2に「対象テディ」、reference3に「年齢不詳」が格納されている。
```
