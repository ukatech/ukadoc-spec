# OnOtherOverlap

**カテゴリ:** 超出範圍與重疊事件

包含其他角色在內，所有正在執行的角色（surface）視窗重疊時觸發。這是OnOverlap的全域版。<br />
重疊狀態改變時會逐次通知，因此只要稍加設計，也能偵測到「不再重疊」。<br />
請注意，自身的資訊也會一併通知。

- **Reference0**: Sakura 名稱/ID-Sakura 名稱/ID \[`\1`\] Sakura 名稱/ID-Sakura 名稱/ID \[`\1`\] Sakura 名稱/ID-Sakura 名稱/ID ...<br />
  \[`\1`\] 是位元組值1<br />
  例：Emily/0-マリ/1 \[`\1`\] マリ/0-所長たん/1
- **Reference1**: 以與Reference0相同的格式，通知狀態改變前（＝前一次事件觸發時的Reference0）的內容。

**対応:** SSP / Ninix
