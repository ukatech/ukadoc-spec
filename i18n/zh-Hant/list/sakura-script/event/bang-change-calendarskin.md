# `\![change,calendarskin,カレンダースキン名]`

**カテゴリ:** 事件指令

切換日曆的外觀。效果等同於從日曆選單選擇外觀。<br />
若不存在相應的日曆外觀，則忽略。<br />
若尚未開啟過日曆，只會變更設定，並在下次開啟日曆時套用。

將日曆外觀名稱設為 lastinstalled，即可切換至最後安裝的日曆外觀。但若曾結束 SSP，則此設定無效。<br />
將日曆外觀名稱設為 random，即可隨機切換。<br />
日曆外觀名稱會透過 [installedcalendarskinname](../../shiori-event/notify/installedcalendarskinname.md) 通知。

**対応:** SSP 2.8.93
