# OnInternalSaoriComplete

**カテゴリ:** Other events

When an internal module is called via [SAORI over DirectSSTP](../../../spec/saori-ex/index.md) with `--async=identifier`, this event is sent if processing succeeds. If the identifier begins with On, an event with the same name as the identifier is sent instead of this event.<br />
See [Asynchronous calls](../../../spec/saori-ex/async.md) for details.

- **Reference0**: Identifier specified with --async=.
- **Reference1**: Result. (Same as Result for a synchronous call.)
- **Reference2**: Module name. (For example, internal_crypto.)
- **Reference3**: Function name. (For example, Digest.)
- **Reference4 onward**: Values returned by a function that returns multiple values. (Value0 onward for a synchronous call.)

**対応:** SSP 2.9.13
