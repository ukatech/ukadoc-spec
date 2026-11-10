# OnCompressArchiveFailure

**カテゴリ:** Other events

Occurs when archive compression fails.

If the identifier specified with the --event option in [`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md) starts with On, an event with "Failure" appended to that identifier is fired. Otherwise, this event is fired.

- **Reference0**: Event identifier specified with Sakura Script's --event option.
- **Reference1**: Error details. See [※list of error codes](caption_archive_error_codes.md).

**対応:** SSP 2.7.23
