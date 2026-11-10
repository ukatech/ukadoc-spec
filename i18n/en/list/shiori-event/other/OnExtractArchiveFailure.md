# OnExtractArchiveFailure

**カテゴリ:** Other events

Occurs when an archive extraction fails.

If the identifier specified with the --event option in [`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md) starts with On, an event with "Failure" appended to that identifier is raised. Otherwise, this event is raised.

- **Reference0**: The event identifier specified with Sakura Script's --event option.
- **Reference1**: Error details. See [※Error code list](caption_archive_error_codes.md).

**対応:** SSP 2.7.23
