# OnInstallCompleteAll

**カテゴリ:** Installation event

Occurs last, after OnInstallComplete/OnInstallCompleteEx, when **all** installations complete successfully, such as when multiple nars are dragged and dropped.<br />
SSP versions earlier than 2.9.00 have an implementation omission, so this event does not actually occur.

- **Reference0**: [※Identifier](caption_install-identifier.md) of the installed item. For multiple items, separated by the character with byte value 1.
- **Reference1**: Name of the installed item. For multiple items, separated by the character with byte value 1.
- **Reference2**: Installation location. For multiple items, separated by the character with byte value 1.

**対応:** SSP 2.9.00 / Ninix
