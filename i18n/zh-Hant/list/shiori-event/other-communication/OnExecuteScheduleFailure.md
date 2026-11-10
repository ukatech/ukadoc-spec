# OnExecuteScheduleFailure

**カテゴリ:** 其他通訊事件

`\![execute,schedule-add/schedule-delete]`執行失敗時觸發。

若在 --event 中指定以 On 開頭的 ID，事件名稱會是在該 ID 後加上 Failure。

- **Reference0**: 操作類型。add 或 delete
- **Reference1**: 失敗原因<br />
  notauthorized：嘗試透過 SSTP 等外部傳入的 script 新增或刪除項目<br />
  invalid：缺少 --summary 或 --start、日期時間格式錯誤、UID 含有不可使用的字元，或在 schedule-delete 中未指定 UID<br />
  notfound：schedule-delete 指定的 UID 沒有對應的行程<br />
  save：儲存至檔案失敗（新增或刪除操作本身已套用）
- **Reference2**: 指定的 UID（若無則為空）

**対応:** SSP 2.8.91
