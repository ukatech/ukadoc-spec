# OnRecycleBinEmpty

**カテゴリ:** OS state event

Occurs when the Recycle Bin is emptied using [`\![execute,emptyrecyclebin]`](../../sakura-script/misc/bang-execute-emptyrecyclebin.md).<br />
OnRecycleBinEmptyFromOther is also sent to all running ghosts, not just the ghost that ran the script.

- **Reference0**: Number of files currently in the Recycle Bin (usually 0 immediately after emptying)
- **Reference1**: Size of files currently in the Recycle Bin (usually 0 immediately after emptying), in bytes
- **Reference2**: Change in the number of files currently in the Recycle Bin from the previous value (usually a negative value immediately after emptying)
- **Reference3**: Change in the size of files currently in the Recycle Bin from the previous value (usually a negative value immediately after emptying), in bytes
- **Reference4**: 1 if emptied successfully, 0 if an error occurred (also 0 if it was already empty)
- **Reference5**: Name of the main character of the ghost that ran the tag (sakuraname).

**対応:** SSP 2.6.04/Ref4 is 2.6.35
