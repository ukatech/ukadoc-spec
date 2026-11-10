# OnFileDrop2

**カテゴリ:** File drop event

Occurs when a file is dragged and dropped. This is the latest specification at present.<br />
When this event is handled, the baseware's default processing (opening the file in an image viewer, media player, or archive viewer) is not performed. To handle the event and also perform the default processing, use [`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md). \[2.9.10\]

- **Reference0**: Path of the dropped file. If multiple files/directories are present, they are separated by byte value 1.
- **Reference1**: Scope number of the character the file was dropped onto. The main character is 0, the partner is 1, and the third character onward are 2 and higher.
- **Reference2**: MIME type of the dropped file (SSP 2.7.98 and later). If multiple files/directories are present, they are separated by byte value 1.

**対応:** Materia / SSP / CROW / Ninix
