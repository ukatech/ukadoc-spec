# OnCompressArchiveFailure

**カテゴリ:** Other events

Occurs when archive compression fails.

If the identifier specified with the --event option in [`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md) starts with On, an event with "Failure" appended to that identifier occurs. Otherwise, this event occurs.

- **Reference0**: Event identifier specified by Sakura Script's --event option.
- **Reference1**: Error details. See [※Error code list](caption_archive_error_codes.md).

**対応:** SSP 2.7.23
