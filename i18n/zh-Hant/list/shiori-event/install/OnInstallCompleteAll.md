# OnInstallCompleteAll

**カテゴリ:** Installation events

Triggered last, after OnInstallComplete/OnInstallCompleteEx, when **all** installations succeed, such as when multiple nar files are dragged and dropped.<br />
SSP versions earlier than 2.9.00 have an implementation omission, so this event does not actually occur.

- **Reference0**: [※Identifier](caption_install-identifier.md) of the installed item. For multiple items, values are separated by the character with byte value 1.
- **Reference1**: Name of the installed item. For multiple items, values are separated by the character with byte value 1.
- **Reference2**: Installation location. For multiple items, values are separated by the character with byte value 1.

**対応:** SSP 2.9.00 / Ninix
