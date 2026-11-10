# OnFileDrop2

**カテゴリ:** File drop events

Occurs when a file is drag-and-dropped. This is the latest specification at present.<br />
When this event is handled, the baseware's default processing (opening the file in an image viewer, media player, or archive viewer) is not performed. To handle the event and also perform the default processing, use [ `\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md).\[2.9.10\]

- **Reference0**: Path of the dropped file. If there are multiple files/directories, they are separated by byte value 1.
- **Reference1**: Scope number of the character the file was dropped on. The main character is 0, the partner is 1, and the third and subsequent characters are 2 or higher.
- **Reference2**: MIME type of the dropped file (SSP 2.7.98 and later). If there are multiple files/directories, they are separated by byte value 1.

**対応:** Materia / SSP / CROW / Ninix
