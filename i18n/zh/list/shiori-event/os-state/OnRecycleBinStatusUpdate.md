# OnRecycleBinStatusUpdate

**カテゴリ:** OS state event

Occurs when files are added to the Recycle Bin or when it is emptied in Explorer, and is notified to all running ghosts.<br />
It is also notified via *\[NOTIFY\]* when a ghost starts.

- **Reference0**: Number of files currently in the Recycle Bin
- **Reference1**: Size of files currently in the Recycle Bin, in bytes
- **Reference2**: Difference from the previous number of files in the Recycle Bin
- **Reference3**: Difference from the previous size of files in the Recycle Bin, in bytes
- **Reference4**: Always 1 (dummy for compatibility with OnRecycleBinEmpty)
- **Reference5**: Always empty (dummy for compatibility with OnRecycleBinEmpty)

**対応:** SSP 2.6.04/Ref4 is 2.6.35
