# OnInternalSaoriComplete

**カテゴリ:** 其他事件

通过[SAORI over DirectSSTP](../../../spec/saori-ex/index.md)调用内置模块时，如果附带`--async=标识符`且处理成功，则会发送此事件。如果标识符以On开头，则会发送与该标识符同名的事件，而非本事件。<br />
详情请参阅[异步调用](../../../spec/saori-ex/async.md)。

- **Reference0**: 通过--async=指定的标识符。
- **Reference1**: 结果。（同步调用中的Result）
- **Reference2**: 模块名。（例如internal_crypto）
- **Reference3**: 函数名。（例如Digest）
- **Reference4以后**: 返回多个值的函数所返回的值。（同步调用中的Value0及以后）

**対応:** SSP 2.9.13
