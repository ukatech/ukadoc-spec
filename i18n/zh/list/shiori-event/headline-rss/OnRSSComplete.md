# OnRSSComplete

**カテゴリ:** Headline/RSS sensing events

Occurs when headline sensing completes successfully. If this event is not handled, a suitable script is generated for display and a headline completion event is called.

- **Reference0**: When there are no updates: no update　[※Reason for ending](caption_headlinesenseresult.md)<br />
  When there are no updates, Reference0 contains only the string "no update"<br />
  When there are updates: RSS distribution site name.
- **Reference1**: Only when there are updates: RSS source URL (points to the distribution site, not the feed itself)
- **Reference2～**: Only when there are updates: title \[`\1`\] URL \[`\1`\] update date and time (format is comma-separated: year, month, day, hour, minute, second) \[`\1`\] author name \[`\1`\] content or summary<br />
  When there are updates, Reference0, 1, 2～ continue for each RSS item<br />
  \[`\1`\] is the character with byte value 1

**対応:** SSP author name・content 2.4.10～
