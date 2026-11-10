# CompressArchive

**カテゴリ:** internal_file

Compresses a folder into a ZIP file (or 7z file). This makes the same processing as `CompressArchive` in [SSTP EXECUTE](../../sstp/method_execute.md) available through SAORI over DirectSSTP.<br />
The archive format is determined by the extension of the destination path. `.7z` produces a 7z archive (compressed using LZMA); all other extensions produce ZIP archives (specifying `.lzh` or `.cab` still produces a ZIP archive).<br />
Archive processing may take several seconds, so [`--async`](../async.md) is strongly recommended. If called synchronously, the ghost stops during processing.

- **Argument1**: Path to the destination archive. Relative paths are based on the ghost folder (ghost/master). Both `/` and `\` can be used as separators. If a relative path is passed in a call without a ghost, the result is 400 (`ghost required`).
- **Argument2**: Path to the folder to compress (files inside it are included recursively, but hidden files and hidden folders, including their contents, are excluded). Written the same way as Argument1. If it does not exist, the result is 400 (`file not found`). This path is not limited to folders managed by SSP; folders outside its management can also be compressed (only the destination is restricted). \[SSP 2.9.33\] Passing something that is not a folder (such as a file path) results in 400 (`invalid parameter`). Before this version, passing a file path failed with 500 (`file not found`).

The options are as follows (if the same name is specified twice, the later one takes effect).

- --password=password……Encrypts using the specified password (for ZIP, this is an AES-encrypted ZIP).
- --option=option……Specify the following values together as a **single comma-separated value** (for example, `--option=overwrite,lzma`. If you specify `--option=` twice, only the later one takes effect).<br />
  overwrite……Replaces the destination archive if it already exists.<br />
  append……Adds to the destination archive if it already exists.<br />
  lzma……Compresses using LZMA (for ZIP only. 7z always uses LZMA, so this has no effect).<br />
  headerencrypt……Also encrypts the header (the list of filenames; requires `--password=`). **Works only for 7z and has no effect on ZIP** (filenames remain unencrypted in ZIP).<br />
  If the destination archive already exists and neither `overwrite` nor `append` is specified, the result is 400 (`file exists`).

On success, the result is 200. `Result` contains the number of files compressed, `Value0` contains the size in bytes after compression, and `Value1` contains the size in bytes before compression (after extraction); all are decimal integers. These are the same values as `Reference1` through `Reference3` in [OnCompressArchiveComplete](../../../list/shiori-event/other/OnCompressArchiveComplete.md) for SSTP EXECUTE. With [`--async`](../async.md), they are returned in `Reference1` (`Result`) and `Reference4` and `Reference5` (`Value0` and `Value1`).<br />
For ZIP, `Value0` is the number of bytes added to the archive (including the header and central directory; with `append`, only the additional data). It is slightly larger than the size of the compressed data alone.<br />
\[SSP 2.9.26\] The file count and byte counts are also returned correctly for ZIP (in \[SSP 2.9.25\], they were 0 when compressing to ZIP).

Failures are as follows. 400 indicates `file not found` (source does not exist) / `invalid parameter` (insufficient arguments, empty path, invalid option, or, in \[SSP 2.9.33\], source is not a folder) / `ghost required` / `file exists` / `path not allowed` (destination is outside folders managed by SSP). 500 indicates the reason for compression failure, such as `open failed`.

For security reasons, the destination is restricted to locations under folders managed by SSP (such as the ghost folder, balloon folder, and locations specified by the “Folder” settings). The path is checked after resolving `..` and similar components. This restriction may be tightened as needed, so it is safest to limit the destination to a folder under the one containing the ghost's own data.

## 記述例

```
Argument0: CompressArchive
Argument1: save/backup.zip
Argument2: save/data
Argument3: --option=overwrite
Argument4: --async=OnBackupDone

→ 204（結果はOnBackupDoneイベントで届く）
```

**対応:** SSP 2.9.25
