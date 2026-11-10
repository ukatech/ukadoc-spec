# OnInstallReroute

**カテゴリ:** Install event

Occurs when the file being installed specifies another ghost, and the specified ghost is running at the same time. Subsequent install events are sent to the specified ghost.

- **Reference0**: The specified ghost's baseware-side name (the [accept](../../../descript/install/install-txt/accept.md) entry in install.txt; that is, the intended recipient).
- **Reference1**: The [identifier](caption_install-identifier.md) of the installed item.
- **Reference2**: The name of the installed item.

**対応:** SSP 2.4 / Ref1 and later: 2.4.85
