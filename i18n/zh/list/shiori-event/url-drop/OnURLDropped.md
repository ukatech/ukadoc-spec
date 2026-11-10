# OnURLDropped

**カテゴリ:** URL drop events

Occurs when receiving the dropped URL has finished.<br />
This event occurs immediately before NAR installation, just after the download process completes. It does not occur for other cases (such as homeurl installation or feed (RSS) installation).

- **Reference0**: Local path of the downloaded file.
- **Reference1**: Dropped URL.
- **Reference2**: Scope number of the character the URL was dropped on. Main character is 0, partner is 1, and the third character onward are 2 and above.

**対応:** Materia / SSP Ref1,2 are 2.6.36 / CROW
