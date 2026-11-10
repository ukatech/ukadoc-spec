# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** plugin「Spectre」

如果此 ghost 尚未完成「校正」，在開啟 plugin 選單時會發生。使用者選擇此 ghost 的「重新校正」時也會發生。<br />
回傳特定回應後，即可建立握手機制，讓 ghost 自動完成「校正」程序。<br />
必要的回應如下列標籤：`\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
傳送此標籤時，需附上包含表情資料的 Reference。Reference 的寫法與 OnSpectrePlugin.Surface 事件接收的內容相同，順序不限。<br />
*預設只傳送 ghost 未提供的表情。* 未列出的表情會視為全部存在。<br />
對應表情較少的 ghost，可選擇反轉此行為，讓 plugin 僅使用清單中列出的表情。<br />
對於完全沒有對應表情的 ghost，則有專用的 Reference。<br />
*請將 ghost 的 shell 無法準確呈現的表情列在此標籤的 Reference 中*（使用反轉行為時則省略）。plugin 會將此資訊用於自身用途。

- **--option=include**: 只使用清單中的 surface（反轉行為）。
- **\_\_NO_EXPRESSIONS\_\_**: 不使用任何表情。必須以 reference0 傳送。
