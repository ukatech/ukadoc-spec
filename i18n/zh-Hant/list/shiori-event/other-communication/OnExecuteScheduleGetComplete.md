# OnExecuteScheduleGetComplete

**カテゴリ:** 其他通訊事件

透過 [`\![execute,schedule-get]`](../../sakura-script/misc/bang-execute-schedule-get.md)讀取 ghost 的行程表時觸發。

若在 --event 中指定以 On 開頭的 ID，該 ID 會成為事件名稱。

- **Reference0～**: [與 OnExecuteICalComplete 相同](OnExecuteICalComplete.md)。<br />
  目標僅限 ghost 的行程表，不包含使用者登錄的行程或行程感測器的行程。

**対応:** SSP 2.8.91
