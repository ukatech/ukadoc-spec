# OnDressupChanged

**カテゴリ:** 啟動、結束與切換事件

dressup 切換時觸發。<br />
此事件可能會通知多次；若發生此情況，最後一次OnDressupChanged為*\[GET\]*，其餘為*\[NOTIFY\]*。<br />
另請參閱此事件後觸發的[OnNotifyDressupInfo](../notify/OnNotifyDressupInfo.md)。

**dressup 旗標變更差異過多時（目前為100個元素），會略過此通知。若要接收大量變更，請使用OnNotifyDressupInfo。**

- **Reference0**: dressup 對象的角色ID。
- **Reference1**: 部件名稱。
- **Reference2**: 啟用時為1，停用時為0。
- **Reference3**: 部件類別名稱。
- **Reference4**: 從腳本執行時為script，從選單執行時為user \[2.5.90～\]

**対応:** SSP / Ninix
