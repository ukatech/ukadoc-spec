# OnExecuteScheduleFailure

**カテゴリ:** 其他通信事件

`\![execute,schedule-add/schedule-delete]`执行失败时触发。

通过 --event 指定以 On 开头的 ID 时，事件名为在该 ID 后添加 Failure。

- **Reference0**: 操作类型。add 或 delete
- **Reference1**: 失败原因<br />
  notauthorized : 尝试通过 SSTP 等外部发送的脚本添加或删除日程<br />
  invalid : 缺少 --summary 或 --start、日期时间格式不正确、UID 中包含不可用字符、使用 schedule-delete 时未指定 UID<br />
  notfound : schedule-delete 指定的 UID 对应的日程不存在<br />
  save : 保存到文件失败（添加或删除操作本身已生效）
- **Reference2**: 指定的 UID（未指定时为空）

**対応:** SSP 2.8.91
