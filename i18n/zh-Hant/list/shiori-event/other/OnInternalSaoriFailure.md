# OnInternalSaoriFailure

**カテゴリ:** Other events

When an internal module is called with `--async=識別子` via [SAORI over DirectSSTP](../../../spec/saori-ex/index.md), this event is sent if processing fails. If the identifier begins with On, an event named "identifier + Failure" is sent instead of this event.<br />
See [Asynchronous calls](../../../spec/saori-ex/async.md) for details.

- **Reference0**: Identifier specified with --async=.
- **Reference1**: Reason for failure. (Same as ErrorDescription from a synchronous call, e.g. invalid encoding)
- **Reference2**: Module name.
- **Reference3**: Function name.

**対応:** SSP 2.9.13
