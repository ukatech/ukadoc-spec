# OnOtherOffscreen

**カテゴリ:** 超出範圍與重疊事件

包含其他角色在內，角色（surface）的視窗被卡在螢幕（工作區域）外，或移出螢幕時觸發。視窗超出範圍。這是OnOffscreen的全域版。<br />
超出範圍的狀態改變時會逐次通知，因此只要稍加設計，也能偵測到「不再超出範圍」。<br />
請注意，自身的資訊也會一併通知。

- **Reference0**: Sakura 名稱/ID \[`\1`\] Sakura 名稱/ID \[`\1`\] Sakura 名稱/ID ...<br />
  \[`\1`\] 是位元組值1<br />
  例：Emily/1 \[`\1`\] 所長たん/0
- **Reference1**: 以與Reference0相同的格式，通知狀態改變前（＝前一次事件觸發時的Reference0）的內容。

**対応:** SSP / Ninix
