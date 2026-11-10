# OnInstallComplete

**カテゴリ:** Installation events

Occurs when installation completes successfully.<br />
This event uses the old specification, so only the *first two items* installed together in a single installation are reported.<br />
If three or more items may be installed together through bundling, use [OnInstallCompleteEx](OnInstallCompleteEx.md).

- **Reference0**: [※Identifier](caption_install-identifier.md) of the installed item.
- **Reference1**: Name of the installed item (the name specified in install.txt).
- **Reference2**: Name of the second installed item (for example, the name of a balloon bundled with a ghost).

**対応:** Materia / SSP / CROW / Ninix
