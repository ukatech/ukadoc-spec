# OnInternalSaoriComplete

**カテゴリ:** Other events

Sent when a call to a built-in module using [SAORI over DirectSSTP](../../../spec/saori-ex/index.md) with `--async=identifier` succeeds. If the identifier starts with On, an event with the same name as the identifier is sent instead of this event.<br />
For details, see [Asynchronous calls](../../../spec/saori-ex/async.md).

- **Reference0**: The identifier specified with --async=.
- **Reference1**: Result. (Result from a synchronous call)
- **Reference2**: Module name. (e.g., internal_crypto)
- **Reference3**: Function name. (e.g., Digest)
- **Reference4 and later**: Values returned by a function that returns multiple values. (Value0 and later from a synchronous call)

**対応:** SSP 2.9.13
