# OnURLDropped

**カテゴリ:** URL drop event

Occurs when receiving the dropped URL has finished.<br />
This event occurs immediately before NAR installation, just after the download completes. It does not occur for other types of installation (homeurl or feed (RSS) installation).

- **Reference0**: Local path of the downloaded file.
- **Reference1**: Dropped URL.
- **Reference2**: Scope number of the character the URL was dropped on. Main character side is 0, partner is 1, and the third character onward is 2 and above.

**対応:** Materia / SSP Ref1,2 are 2.6.36 / CROW
