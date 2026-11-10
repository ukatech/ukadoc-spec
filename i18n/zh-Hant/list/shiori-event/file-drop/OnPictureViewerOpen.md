# OnPictureViewerOpen

**カテゴリ:** File drop event

Occurs when a file is dragged and dropped, the ghost does not respond to OnFileDrop2 (or executes [`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md) \[2.9.10\]), and the image viewer opens. References are the same as for OnFileDrop2.

- **Reference0**: Path of the dropped file. If multiple files/directories are present, they are separated by byte value 1.
- **Reference1**: Scope number of the character the file was dropped on. The main character is 0, the partner is 1, and the third character onward are 2 or higher.
- **Reference2**: MIME type of the dropped file. If multiple files/directories are present, they are separated by byte value 1.

**対応:** SSP 2.8.51
