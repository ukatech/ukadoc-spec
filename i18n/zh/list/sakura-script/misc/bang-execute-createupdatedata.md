# `\![execute,createupdatedata,出力先ファイル]`

**カテゴリ:** Uncategorized command

Creates an update definition file (updates2.dau/updates.txt) for the ghost that executed the script.<br />
Output file: Optional. Specify a path relative to the ghost's ghost/master folder, or an absolute path. \[2.8.98\]<br />
If specified, only one file is created at that path. If a file with the same name already exists, it is overwritten. If the filename ends in .dau, it is output in the same format as updates2.dau; otherwise, it is output in the updates.txt format.<br />
In this case, updates2.dau/updates.txt in the usual output locations (the ghost root and ghost/master) are neither created nor deleted. If the output file is inside the ghost's folder, that file itself is not included in the update definition.

**対応:** SSP 2.5.08
