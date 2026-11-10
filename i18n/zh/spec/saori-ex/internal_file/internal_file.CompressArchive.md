# CompressArchive

**カテゴリ:** internal_file

Compresses a folder into a ZIP file (or 7z file). This makes the same processing as `CompressArchive` in [SSTP EXECUTE](../../sstp/method_execute.md) callable via SAORI over DirectSSTP.<br />
The archive format is determined by the extension of the destination. `.7z` produces a 7z archive (compressed using LZMA); all other extensions produce ZIP archives (even if `.lzh` or `.cab` is specified, the contents will be ZIP).<br />
Archive processing may take several seconds, so [`--async`](../async.md) is strongly recommended. If called synchronously, the ghost will stop during processing.

- **Argument1**: Path to the destination archive. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path when calling without a ghost returns 400 (`ghost required`).
- **Argument2**: Path to the folder to compress (files inside are included recursively, but hidden files and hidden folders, including their contents, are excluded). The format is the same as for Argument1. If it does not exist, returns 400 (`file not found`). This path is not limited to folders managed by SSP; folders outside its management can also be compressed (only the destination is restricted). \[SSP 2.9.33\] Passing something that is not a folder (such as a file path) returns 400 (`invalid parameter`). Before this version, passing a file path failed with 500 (`file not found`).

The options are as follows (if the same name is specified twice, the latter takes effect).

- --password=password……Encrypts using the specified password (AES-encrypted ZIP for ZIP archives).
- --option=options……Specify the following values together as a **single comma-separated list** (for example, `--option=overwrite,lzma`. If you specify two separate `--option=` arguments, only the latter takes effect).<br />
  overwrite……Replaces the destination archive if it already exists.<br />
  append……Adds to the destination archive if it already exists.<br />
  lzma……Compresses using LZMA (for ZIP; 7z always uses LZMA, so this has no effect).<br />
  headerencrypt……Also encrypts the header (file name list) (requires `--password=`). **Works only for 7z and has no effect for ZIP** (file names remain unencrypted in ZIP).<br />
  If the destination archive already exists and neither `overwrite` nor `append` is specified, returns 400 (`file exists`).

On success, returns 200, with the number of files compressed in `Result`, the number of bytes after compression in `Value0`, and the number of bytes before compression (after extraction) in `Value1` (decimal integers). These are the same values as `Reference1`–`Reference3` of [OnCompressArchiveComplete](../../../list/shiori-event/other/OnCompressArchiveComplete.md) for SSTP EXECUTE; with [`--async`](../async.md), they are returned in `Reference1` (`Result`) and `Reference4` and `Reference5` (`Value0` and `Value1`).<br />
For ZIP, `Value0` is the number of bytes added to the archive (including headers and the central directory; when using `append`, only the added portion), so it is slightly larger than the size of the compressed data alone.<br />
\[SSP 2.9.26\] The file count and byte counts are returned correctly for ZIP as well (in \[SSP 2.9.25\], compression to ZIP returned 0).

Failures are as follows. 400 is returned for `file not found` (source does not exist) / `invalid parameter` (missing argument, empty path, invalid option, \[SSP 2.9.33\] source is not a folder) / `ghost required` / `file exists` / `path not allowed` (destination is outside folders managed by SSP). 500 indicates the reason compression failed, such as `open failed`.

For security reasons, the destination is restricted to locations under folders managed by SSP (such as the ghost and balloon folders, and locations specified in the “Folders” settings). Paths are checked after resolving `..` and similar components. This restriction may be strengthened as appropriate, so it is safest to limit the destination to a location under the folder containing the ghost's own data.

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
