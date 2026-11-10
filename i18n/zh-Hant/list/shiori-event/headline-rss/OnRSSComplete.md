# OnRSSComplete

**カテゴリ:** Headline/RSS sensing events

Triggered when headline sensing completes successfully. If this event is not handled, an appropriate script is generated for display and a headline completion event is called.

- **Reference0**: When there are no updates: no update　[※Reason for completion](caption_headlinesenseresult.md)<br />
  When there are no updates, only Reference0 is sent, and its value is the string "no update".<br />
  When there are updates: RSS feed site name.
- **Reference1**: Only when there are updates: RSS source URL (points to the feed site, not the feed itself)
- **Reference2～**: Only when there are updates: title \[`\1`\] URL \[`\1`\] update date and time (comma-separated format: year, month, day, hour, minute, second) \[`\1`\] author name \[`\1`\] content or summary<br />
  When there are updates, Reference0, 1, 2～ are repeated for each RSS item.
  \[`\1`\] is the character with byte value 1.

**対応:** SSP author name/content 2.4.10～
