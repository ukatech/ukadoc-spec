# OnInstallCompleteAll

**カテゴリ:** Installation events

Occurs last, after OnInstallComplete/its Ex variant, when **all** installations complete successfully, such as when multiple nar files are dragged and dropped.<br />
SSP had a missing implementation in versions earlier than 2.9.00, so this event does not actually occur.

- **Reference0**: [※Identifier](caption_install-identifier.md) of the installed item. If multiple, delimited by byte value 1.
- **Reference1**: Name of the installed item. If multiple, delimited by byte value 1.
- **Reference2**: Installation location. If multiple, delimited by byte value 1.

**対応:** SSP 2.9.00 / Ninix
