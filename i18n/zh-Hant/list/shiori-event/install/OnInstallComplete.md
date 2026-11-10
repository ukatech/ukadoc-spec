# OnInstallComplete

**カテゴリ:** Installation events

Triggered when installation completes successfully.<br />
This event is from an older specification, so only the *first two items* installed together in a single installation are reported.<br />
If three or more items may be installed together, such as through bundling, use [OnInstallCompleteEx](OnInstallCompleteEx.md).

- **Reference0**: [※Identifier](caption_install-identifier.md) of the installed item.
- **Reference1**: Name of the installed item (the name specified in install.txt).
- **Reference2**: Name of the second installed item (for example, the balloon-side name when a balloon is bundled with a ghost).

**対応:** Materia / SSP / CROW / Ninix
