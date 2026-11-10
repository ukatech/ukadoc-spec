# OnGetValues

**カテゴリ:** ghost 间通用事件

这是收到 OnRequestValues 后应返回的事件。

- **Reference0**: 发送方 ghost 名称。
- **Reference1**: key=value（key 是 OnRequestValues 中接收的变量名，value 是对应的值）。Reference2 及之后也按相同格式排列，直到所有请求的变量都返回为止。不返回不存在的变量。顺序不受 OnRequestValues 中变量发送顺序的影响。

**対応:** SSP
