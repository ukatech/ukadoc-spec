# OnExecuteICalFailure

**カテゴリ:** Other communication events

Occurs when retrieval fails with `\![execute,ical-get/ical-post]`.

- **Reference0～**: If parsing fails, Reference4=parse. If retrieval from the same URL is already in progress, Reference4=downloading. Otherwise, the references are [the same as for OnExecuteHTTPFailure](OnExecuteHTTPFailure.md) (note that the order differs from Complete).

**対応:** SSP 2.8.90
