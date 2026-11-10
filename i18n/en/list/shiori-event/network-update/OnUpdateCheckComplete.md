# OnUpdateCheckComplete

**カテゴリ:** Network update event

Occurs when the network update check succeeds.

- **Reference0**: If there are files to update, the total number of files to be updated (unlike OnUpdateReady, 1 is not subtracted).<br />
  If there are no files to update, none.
- **Reference1**: A comma-separated list of updated file names.
- **Reference3**: [※Update target type](caption_updatetype.md)
- **Reference4**: SSP 2.3: Reason for running the update. Script only.

**対応:** SSP
