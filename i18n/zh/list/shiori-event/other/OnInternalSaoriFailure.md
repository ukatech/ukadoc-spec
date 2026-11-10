# OnInternalSaoriFailure

**カテゴリ:** 其他事件

通过[SAORI over DirectSSTP](../../../spec/saori-ex/index.md)调用带有`--async=标识符`的内置模块时，如果处理失败，则会发送此事件。如果标识符以On开头，则会发送名为“标识符＋Failure”的事件，而不是此事件。<br />
详情请参阅[异步调用](../../../spec/saori-ex/async.md)。

- **Reference0**: 通过--async=指定的标识符。
- **Reference1**: 失败原因。（与同步调用的 ErrorDescription 相同，例如 invalid encoding）
- **Reference2**: 模块名。
- **Reference3**: 函数名。

**対応:** SSP 2.9.13
