# OnURLDropFailure

**カテゴリ:** URL drop event

Occurs when receiving the dropped URL fails or is canceled.<br />
This event occurs when an attempt to install a NAR fails. It does not occur for other types of installation (homeurl or feed (RSS) installation).

- **Reference0**: Local path of the files that have finished downloading.
- **Reference1**: [※Reason for failure](../network-update/caption_updateresultfailure.md)
- **Reference2**: Dropped URL.
- **Reference3**: Scope number of the character the URL was dropped on. Main character side is 0, partner is 1, and the third character onward is 2 and above.

**対応:** Materia / SSP Ref2,3 are 2.6.36 / CROW
