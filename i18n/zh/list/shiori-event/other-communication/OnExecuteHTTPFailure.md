# OnExecuteHTTPFailure

**カテゴリ:** Other communication events

Occurs when execute-http fails to retrieve data. References are the same as for Complete.

\[2.8.90\] If retrieval from the same URL is already in progress, the later request is not executed and this event occurs (Reference4=downloading). Before this, the tag was silently ignored.

**対応:** SSP / Ninix
