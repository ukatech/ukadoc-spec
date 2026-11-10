# `\![execute,createupdatedata,出力先ファイル]`

**カテゴリ:** Uncategorized command

Creates an update definition file (updates2.dau/updates.txt) for the ghost that executed the script.<br />
Output file: Optional. Specify a path relative to the ghost's ghost/master folder, or an absolute path. \[2.8.98\]<br />
If specified, creates only one file at that path. If a file with the same name already exists, it is overwritten. If the filename ends in .dau, it is output in the same format as updates2.dau; otherwise, it is output in the updates.txt format.<br />
In this case, the usual output locations (the ghost root and ghost/master) are neither created nor deleted for updates2.dau/updates.txt. If the destination is inside the ghost's folder, the file itself is not included in the update definition.

**対応:** SSP 2.5.08
