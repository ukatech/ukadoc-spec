# OnInternalSaoriFailure

**カテゴリ:** Other events

Sent when a call to a built-in module using [SAORI over DirectSSTP](../../../spec/saori-ex/index.md) with `--async=identifier` fails. If the identifier starts with On, an event named "identifier + Failure" is sent instead of this event.<br />
For details, see [Asynchronous calls](../../../spec/saori-ex/async.md).

- **Reference0**: The identifier specified with --async=.
- **Reference1**: Reason for failure. (Same as ErrorDescription from a synchronous call, e.g., invalid encoding)
- **Reference2**: Module name.
- **Reference3**: Function name.

**対応:** SSP 2.9.13
