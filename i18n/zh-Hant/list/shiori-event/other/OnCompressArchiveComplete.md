# OnCompressArchiveComplete

**カテゴリ:** Other events

Occurs when archive compression completes successfully.

If the identifier specified with the --event option in [`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md) starts with On, an event with that identifier is fired. Otherwise, this event is fired.

- **Reference0**: Event identifier specified with Sakura Script's --event option.
- **Reference1**: Number of files compressed.
- **Reference2**: Compressed size (bytes).
- **Reference3**: Uncompressed size (bytes).

**対応:** SSP 2.7.23
