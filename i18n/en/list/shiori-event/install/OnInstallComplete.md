# OnInstallComplete

**カテゴリ:** Installation event

Occurs when installation completes successfully.<br />
This event uses an old specification, so only the *first two items* installed together in a single installation are reported.<br />
If bundling can result in three or more items being installed at once, use [OnInstallCompleteEx](OnInstallCompleteEx.md).

- **Reference0**: [※Identifier](caption_install-identifier.md) of the installed item.
- **Reference1**: Name of the installed item (the name specified in install.txt).
- **Reference2**: Name of the second installed item (for example, the name of the balloon when a ghost is bundled with one).

**対応:** Materia / SSP / CROW / Ninix
