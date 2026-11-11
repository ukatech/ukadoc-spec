# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** plugin「Spectre」

開啟 plugin 選單時，若此 ghost 尚未「校準」則會發生。使用者選擇「重新校準」此 ghost 時也會發生。<br />
回傳特定回應可完成交握，使 ghost 能夠自動完成「校準」步驟。<br />
必要的回應是以下標籤：`\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
此標籤應附帶包含表情資料的 Reference。Reference 的寫法與 OnSpectrePlugin.Surface 事件中收到的相同，順序不限。<br />
*預設只傳送 ghost 未提供的表情。* plugin 會假定清單中未列出的表情都存在。<br />
對於支援的表情較少的 ghost，可透過選項反轉此行為，讓 plugin 只使用清單中列出的表情。<br />
對於完全沒有支援表情的 ghost，有專用的 Reference。<br />
*ghost 的 shell 無法準確呈現的表情應列為此標籤的 Reference*（使用反轉行為時則應省略），因為 plugin 會將此資訊用於自身用途。

- **--option=include**: 只使用清單中列出的 surface（反轉行為）。
- **\_\_NO_EXPRESSIONS\_\_**: 不使用任何表情。必須作為 reference0 傳送。
