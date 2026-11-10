# OnExtractArchiveFailure

**カテゴリ:** Other events

Occurs when archive extraction fails.

If the identifier specified with the --event option in [`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md) begins with On, an event with the suffix "Failure" appended to that identifier is triggered. Otherwise, this event is triggered.

- **Reference0**: Event identifier specified with the --event option in Sakura Script.
- **Reference1**: Error details. See [※List of error codes](caption_archive_error_codes.md).

**対応:** SSP 2.7.23
