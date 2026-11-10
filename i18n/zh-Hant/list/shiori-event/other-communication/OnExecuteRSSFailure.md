# OnExecuteRSSFailure

**カテゴリ:** Other communication events

Occurs when retrieval by `\![execute,rss-get/post]` fails.

- **Reference0～**: For a parsing failure, Reference4=parse. If retrieval of the same URL is already in progress, Reference4=downloading \[2.8.90\]. Otherwise, the references are [the same as for OnExecuteHTTPFailure](OnExecuteHTTPFailure.md)

**対応:** SSP
