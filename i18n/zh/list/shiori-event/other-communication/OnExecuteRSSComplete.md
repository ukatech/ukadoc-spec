# OnExecuteRSSComplete

**カテゴリ:** Other communication events

Occurs when retrieval completes successfully with `\![execute,rss-get/post]`.

\[2.8.92\] The number of items and which ones are included are determined by the [RSS filtering options](../../sakura-script/misc/bang-execute-rss-post-URL.note.md).

- **Reference0～**: Title \[`\1`\] URL \[`\1`\] Updated date and time (comma-separated format: year,month,day,hour,minute,second) \[`\1`\] Author name \[`\1`\] Content or summary<br />
  When there are updates, Reference0, 1, 2, etc. continue for each RSS item<br />
  \[`\1`\] is byte value 1

**対応:** SSP author name and content 2.4.10～
