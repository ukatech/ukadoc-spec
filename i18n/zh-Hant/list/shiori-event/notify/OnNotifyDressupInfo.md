# OnNotifyDressupInfo

**カテゴリ:** Notify 事件

通知 dressup 資訊。<br />
僅在啟動時以 *\[NOTIFY\]* 傳送；若是從選單切換等使用者操作，則以 *\[GET\]* 傳送。<br />
也請參閱此事件之前發生的 [OnDressupChanged](../boot-close-change/OnDressupChanged.md)。

- **Reference\***: 以下資訊以位元組值 1 分隔：\[角色 ID、類別名稱、部件名稱、選項、啟用 1／停用 0、縮圖路徑\]<br />
  選項可能有多個，以逗號分隔。<br />
  會依 dressup 定義的數量重複。<br />
  ghost 端若處理與上次通知相比的啟用／停用差異，即可掌握變更內容。

**対応:** SSP
