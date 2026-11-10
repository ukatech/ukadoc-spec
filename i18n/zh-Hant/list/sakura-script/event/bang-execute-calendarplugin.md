# `\![execute,calendarplugin,カレンダープラグイン名]`

**カテゴリ:** 事件指令

開始取得日曆 plugin（行程感測器）的預定事項。效果等同於從日曆選單選擇 plugin。<br />
即使未顯示日曆，也會執行。<br />
將日曆 plugin 名稱設為 random，即可隨機選擇。<br />
設為 lastinstalled，則會執行最後安裝的日曆 plugin。但若曾結束 SSP，則此設定無效。<br />
若不存在相應的日曆 plugin，則忽略。<br />
日曆 plugin 名稱會透過 [installedcalendarpluginname](../../shiori-event/notify/installedcalendarpluginname.md) 通知。

**対応:** SSP 2.8.93
