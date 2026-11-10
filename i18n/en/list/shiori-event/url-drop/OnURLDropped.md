# OnURLDropped

**カテゴリ:** URL drop event

Occurs when receiving a dropped URL has finished.<br />
This event occurs immediately before a NAR installation, just after the download process finishes. It does not occur for other types of installations (homeurl or feed (RSS) installation).

- **Reference0**: Local path of the downloaded file.
- **Reference1**: Dropped URL.
- **Reference2**: Scope number of the character the URL was dropped on. Main character is 0, partner is 1, and the third character onward are 2 and higher.

**対応:** Materia / SSP Ref1,2 are 2.6.36 / CROW
