# OnBIFFComplete

**カテゴリ:** 邮件检查事件

邮件检查成功时触发。

- **Reference0**: 邮件队列中的邮件数，以 1 为起始值。
- **Reference1**: 邮件队列中的邮件字节数。
- **Reference2**: 要检查的邮件服务器名称。
- **Reference3**: 新邮件差异。
- **Reference4**: 所有邮件的 TopResult。POP 通信的所有头部列表。每封邮件以字节值 2 分隔，每个头部以字节值 1 分隔（通常使用 Reference7 中的信息即可）。
- **Reference5**: ListResult。邮件服务器上的 ID。内容相当于 POP 命令「LIST」的结果。
- **Reference6**: UidlResult。用于区分邮件的 ID。内容相当于 POP 命令「UIDL」的结果。
- **Reference7**: 以字节值 1 分隔的发件人和标题。

**対応:** Materia / SSP / CROW
