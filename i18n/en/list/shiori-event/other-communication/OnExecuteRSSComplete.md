# OnExecuteRSSComplete

**カテゴリ:** Other communication events

Occurs when `\![execute,rss-get/post]` successfully completes retrieval.

\[2.8.92\] Which items and how many are returned depends on the [RSS filtering options](../../sakura-script/misc/bang-execute-rss-post-URL.note.md).

- **Reference0～**: Title \[`\1`\] URL \[`\1`\] update date and time (comma-separated format: year,month,day,hour,minute,second) \[`\1`\] author name \[`\1`\] content or summary<br />
  When items are available, References continue as Reference0, 1, 2, etc., one for each RSS item<br />
  \[`\1`\] is byte value 1

**対応:** SSP author name/content 2.4.10～
