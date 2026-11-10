# OnURLQuery

**カテゴリ:** URL drop events

Notifies when a URL is dragged and dropped onto a character window.<br />
Returning a script in response cancels the normal download process.<br />
Return a script only if the ghost wants to handle the URL itself.

- **Reference0**: URL path.
- **Reference1**: 0 for the main character, 1 for the partner. SSP/CROW also support 2 and above.
- **Reference2**: MIME type of the dropped URL
- **Reference3**: The action SSP plans to perform next if there is no response.<br />
  One of feed, nar, homeurl, ical, ssf, or unknown.<br />
  If unknown, the URL cannot be handled by the baseware, meaning the baseware cannot process it any further.<br />
  For any other value, pass it as-is together with Reference0 to [`\![execute,dropdefault,url]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)\[2.9.10\] or [`\![execute,install,url]`](../../sakura-script/misc/bang-execute-install-url-URL.md) to continue processing.

**対応:** SSP Ref3 is 2.6.35
