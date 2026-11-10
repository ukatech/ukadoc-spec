# OnArchiveViewerOpen

**カテゴリ:** File drop event

Occurs when a file is dragged and dropped, the ghost does not respond to OnFileDrop2 (or executes [`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)\[2.9.10\]), and the archive viewer opens. References are the same as OnFileDrop2.

- **Reference0**: Path of the dropped file. If multiple files/directories are dropped, they are separated by byte value 1.
- **Reference1**: Scope number of the character that received the drop. 0 for the main character, 1 for the partner, and 2 or higher for the third character onward.
- **Reference2**: MIME type of the dropped file. If multiple files/directories are dropped, they are separated by byte value 1.

**対応:** SSP 2.8.57
