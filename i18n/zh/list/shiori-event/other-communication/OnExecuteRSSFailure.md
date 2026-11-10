# OnExecuteRSSFailure

**カテゴリ:** Other communication events

Occurs when retrieval fails with `\![execute,rss-get/post]`.

- **Reference0～**: If parsing fails, Reference4=parse. If retrieval from the same URL is already in progress, Reference4=downloading \[2.8.90\]. Otherwise, the references are [the same as for OnExecuteHTTPFailure](OnExecuteHTTPFailure.md)

**対応:** SSP
