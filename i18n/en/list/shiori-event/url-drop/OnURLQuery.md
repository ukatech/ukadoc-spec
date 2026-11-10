# OnURLQuery

**カテゴリ:** URL drop event

Notifies when a URL is dragged and dropped onto a character window.<br />
Returning a script for this event cancels the normal download process.<br />
Return a script only when the ghost wants to handle the URL itself.

- **Reference0**: URL path.
- **Reference1**: 0 for the main character, 1 for the partner. SSP/CROW also support 2 and higher.
- **Reference2**: MIME type of the dropped URL
- **Reference3**: The process SSP is scheduled to perform next if no response is given.<br />
  One of feed, nar, homeurl, ical, ssf, or unknown.<br />
  If unknown, the URL cannot be handled by the baseware, meaning no further processing can be done on the baseware side.<br />
  For the other values, pass this together with Reference0 to [`\![execute,dropdefault,url]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)\[2.9.10\] or [`\![execute,install,url]`](../../sakura-script/misc/bang-execute-install-url-URL.md) to continue processing.

**対応:** SSP Ref3 is 2.6.35
