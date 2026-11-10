# OnExtractArchiveFailure

**カテゴリ:** Other events

Occurs when an archive extraction fails.

If the identifier specified with the --event option in [`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md) begins with On, an event with that identifier followed by "Failure" is triggered. Otherwise, this event is triggered.

- **Reference0**: Event identifier specified with Sakura Script's --event option.
- **Reference1**: Error details. See [※error code list](caption_archive_error_codes.md).

**対応:** SSP 2.7.23
