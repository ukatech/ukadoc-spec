# OnExtractArchiveComplete

**カテゴリ:** Other events

Occurs when an archive has been successfully extracted.

If the identifier specified with the --event option in [`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md) begins with On, an event with that identifier is triggered. Otherwise, this event is triggered.

- **Reference0**: Event identifier specified with Sakura Script's --event option.
- **Reference1**: Number of extracted files.
- **Reference2**: Compressed size (bytes).
- **Reference3**: Uncompressed size (bytes).

**対応:** SSP 2.7.23
