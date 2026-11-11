# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** plugin「Spectre」

當此 ghost 尚未「校準」時，開啟 plugin 選單會觸發此事件。使用者選擇「重新校準」此 ghost 時也會觸發。<br />
回傳特定回應會完成交握，讓 ghost 能夠自動完成「校準」步驟。<br />
必要的回應是以下標籤：`\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
此標籤應附帶包含表情資料的 Reference。Reference 的寫法與 OnSpectrePlugin.Surface 事件收到的相同，順序不限。<br />
*預設只需傳送 ghost 未提供的表情。* plugin 會假定未列出的表情都存在。<br />
對於相容表情較少的 ghost，可使用選項反轉此行為，讓 plugin 只使用清單中列出的表情。<br />
對於沒有任何相容表情的 ghost，另有專用的 Reference。<br />
*ghost 的 shell 無法精確呈現的表情，應列為此標籤的 Reference*（若使用反轉行為則應省略），因為 plugin 會將此資訊用於自身用途。

- **--option=include**: 只使用清單中列出的 surface（反轉行為）。
- **\_\_NO_EXPRESSIONS\_\_**: 不使用任何表情。必須作為 reference0 傳送。
