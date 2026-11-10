# `\![execute,schedule-add,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

在 ghost 專用行事曆中新增一筆行程。新增的行程會顯示在 SSP 行事曆中，並與使用者的行程一樣，列入今日行程及[OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md)的觸發對象。<br />
ghost 專用行事曆會儲存在與使用者行程、排程感測器不同的檔案（data/schedule/ghost/schedule.ics）中，並由所有 ghost 共用。也可以覆寫或刪除其他 ghost 新增的行程。<br />
使用者可以在行事曆中檢視，但無法編輯。可從行事曆的選單「全部刪除」→「ghost 新增的行程」一次刪除所有行程。<br />
結果會透過[OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md)通知，失敗時則透過[OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md)通知。從 SSTP 等外部來源傳送的 script 無法執行此命令。

選項（--summary 與 --start 為必填）<br />
--summary=標題 : 行程標題（SUMMARY）。<br />
--start=日期時間 : 開始日期時間。yyyymmdd 表示全天行程；yyyymmddThhmm 或 yyyymmddThhmmss 表示包含時間的行程（本地時間）。分隔符號 - 與 : 會被忽略。<br />
--end=日期時間 : 結束日期時間。格式與 --start 相同。省略時，行程僅持續開始日一天。<br />
--uid=UID : 行程識別碼。只能使用不含空白的半形英數字與符號。若已有相同 UID 的行程，則會取代該行程。省略時由 SSP 指派，並透過 OnExecuteScheduleComplete 傳回。<br />
--description=說明 : DESCRIPTION。<br />
--location=地點 : LOCATION。<br />
--url=URL : URL。<br />
--categories=分類 : CATEGORIES。有多個分類時以逗號分隔（會直接以 iCal 的 CATEGORIES 值儲存）。<br />
--status=狀態 : STATUS（CONFIRMED / TENTATIVE / CANCELLED）。<br />
--type=種類 : 行程種類。會放入[OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md)等事件的 Reference0。<br />
--rrule=規則 : 重複規則（RRULE 的值部分，例如 FREQ=WEEKLY;BYDAY=MO）。<br />
--exdate=日期 : 從重複行程中排除的日期（yyyymmdd）。有多個日期時以逗號分隔。<br />
--notify=分鐘 : 提前幾分鐘通知。省略時依 SSP 設定。<br />
--script=script : 附加至行程的 Sakura Script。通知時或讀取行程時會執行。<br />
--event=事件 ID : 指定以 On 開頭的 ID，結果事件名稱就會使用該 ID（失敗時則在 ID 後加上 Failure）。<br />
指定包含逗號的值（例如 --rrule、--exdate、--categories）時，請以 " " 括住整個引數。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-add,--uid=myghost-meeting,--summary=打ち合わせ,--start=20261001T1000,--end=20261001T1100,"--rrule=FREQ=WEEKLY;BYDAY=TH",--notify=10,--event=OnMyScheduleAdded]2026年10月1日から毎週木曜10時の予定を登録し、10分前に通知させる。
```

```sakurascript
\![execute,schedule-add,--summary=記念日,--start=20261224,--rrule=FREQ=YEARLY]毎年12月24日の終日予定を登録する。
```
