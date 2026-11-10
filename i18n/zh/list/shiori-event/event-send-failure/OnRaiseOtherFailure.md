# OnRaiseOtherFailure

**カテゴリ:** 事件发送失败事件

`\![raiseother]`失败时触发。

- **Reference0**: 未找到时为 notfound。<br />
  处于 `\t` 中时为 timecritical。<br />
  处于被动模式时为 passivemode。<br />
  处于引导模式时为 inductionmode。<br />
  处于最小化状态时为 minimized。<br />
  其他情况为执行结果，例如 204。<br />
  对于 \_\_SYSTEM_ALL_GHOST\_\_ 等情况，这是以字节值 1 分隔的列表。
- **Reference1**: ghost 名称或 `\0` 名称。<br />
  对于 \_\_SYSTEM_ALL_GHOST\_\_ 等情况，这是以字节值 1 分隔的列表。
- **Reference2**: 尝试执行的事件 ID。
- **Reference3～**: 尝试执行的事件的 Reference。

**対応:** SSP
