# OnURLDropFailure

**カテゴリ:** URL drop events

Occurs when receiving a dropped URL fails or is canceled.<br />
This event occurs when an attempt to install a NAR fails. It does not occur for other cases (such as homeurl installation or feed (RSS) installation).

- **Reference0**: Local path of the portion of the file that has finished downloading.
- **Reference1**: [※Reason for failure](../network-update/caption_updateresultfailure.md)
- **Reference2**: Dropped URL.
- **Reference3**: Scope number of the character the URL was dropped on. Main character is 0, partner is 1, and the third character onward are 2 and above.

**対応:** Materia / SSP Ref2,3 are 2.6.36 / CROW
