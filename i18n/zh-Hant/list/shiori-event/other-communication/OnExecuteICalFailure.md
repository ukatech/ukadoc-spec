# OnExecuteICalFailure

**カテゴリ:** Other communication events

Occurs when retrieval by `\![execute,ical-get/ical-post]` fails.

- **Reference0～**: For a parsing failure, Reference4=parse. If retrieval of the same URL is already in progress, Reference4=downloading. Otherwise, the references are [the same as for OnExecuteHTTPFailure](OnExecuteHTTPFailure.md) (note that the order differs from Complete).

**対応:** SSP 2.8.90
