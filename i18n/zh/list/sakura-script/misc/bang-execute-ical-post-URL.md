# `\![execute,ical-post,URL,オプション,オプション,オプション...]`

**カテゴリ:** Unclassified command

Send an http post request with [※options](bang-execute-http-options-URL.note.md), parse the response as an iCalendar (RFC 5545) calendar, and then notify the parsed results as events.<br />
The parsing and notification behavior is the same as [ical-get](bang-execute-ical-get-URL.md). The parameter group is specified in the same way as for http-post.

**対応:** SSP 2.8.90
