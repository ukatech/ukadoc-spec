# OnInternalSaoriComplete

**カテゴリ:** Other events

When an internal module is called with `--async=識別子` via [SAORI over DirectSSTP](../../../spec/saori-ex/index.md), this event is sent if processing succeeds. If the identifier begins with On, an event with the same name as the identifier is sent instead of this event.<br />
See [Asynchronous calls](../../../spec/saori-ex/async.md) for details.

- **Reference0**: Identifier specified with --async=.
- **Reference1**: Result. (Result from a synchronous call)
- **Reference2**: Module name. (e.g. internal_crypto)
- **Reference3**: Function name. (e.g. Digest)
- **Reference4以降**: Values returned by a function that returns multiple values. (Value0 onward from a synchronous call)

**対応:** SSP 2.9.13
