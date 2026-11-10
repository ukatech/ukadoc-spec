# OnMediaPlayerOpen

**カテゴリ:** File drop event

Occurs when a file is dragged and dropped, the ghost does not respond to OnFileDrop2 (or executes [`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)\[2.9.10\]), and the media player is opened. Reference is the same as OnFileDrop2.

- **Reference0**: Path of the dropped file. If there are multiple files/directories, they are separated by byte value 1.
- **Reference1**: Scope number of the character onto which the file was dropped. The main character is 0, the partner is 1, and the third and subsequent characters are 2 and above.
- **Reference2**: MIME type of the dropped file. If there are multiple files/directories, they are separated by byte value 1.

**対応:** SSP 2.8.51
