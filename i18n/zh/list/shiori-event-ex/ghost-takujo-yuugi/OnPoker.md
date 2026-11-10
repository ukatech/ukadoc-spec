# OnPoker

**カテゴリ:** ghost「桌上游技」

需要回复的事件。回复时使用 raiseother 或 notifyother。

- **Reference0**: 协议版本 (POKER/1.0)
- **Reference1**: 服务器 ghost 名称
- **Reference2**: 服务器事件名称

## POKER/1.0 中 Reference3 及之后的附加信息

- **Reference3**: hello（申请参加。也可能被拒绝。）

- **Reference3**: action（Reference4 及之后包含可用操作。）
- **Reference\***: 可用操作包括 bet、raise、allin、check、call、fold 六种中的若干种。<br />
  请注意，不回复时会自动执行 fold。<br />
  执行 bet/raise 时还必须发送加注金额。
