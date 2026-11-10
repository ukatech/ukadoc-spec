# OnRecycleBinStatusUpdate

**カテゴリ:** OS state event

Occurs when files are added to the Recycle Bin or when it is emptied in Explorer, and is sent to all running ghosts.<br />
Also sent as *\[NOTIFY\]* when a ghost starts.

- **Reference0**: Number of files currently in the Recycle Bin
- **Reference1**: Size of files currently in the Recycle Bin, in bytes
- **Reference2**: Change in the number of files currently in the Recycle Bin from the previous value
- **Reference3**: Change in the size of files currently in the Recycle Bin from the previous value, in bytes
- **Reference4**: Always 1 (dummy value for compatibility with OnRecycleBinEmpty)
- **Reference5**: Always empty (dummy value for compatibility with OnRecycleBinEmpty)

**対応:** SSP 2.6.04/Ref4 is 2.6.35
