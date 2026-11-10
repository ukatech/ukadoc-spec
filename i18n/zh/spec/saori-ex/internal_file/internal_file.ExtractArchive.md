# ExtractArchive

**カテゴリ:** internal_file

Extracts archives (including ZIP, 7z, tar, and others; see “Supported formats” below). This makes the same processing as `ExtractArchive` in [SSTP EXECUTE](../../sstp/method_execute.md) callable via SAORI over DirectSSTP.<br />
Archive processing may take several seconds, so [`--async`](../async.md) is strongly recommended. If called synchronously, the ghost will stop during processing.

- **Argument1**: Path to the archive to extract. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path when calling without a ghost returns 400 (`ghost required`). If the file does not exist (including when the path refers to a folder), returns 400 (`file not found`).
- **Argument2**: Path to the destination folder. The format is the same as for Argument1. If the folder does not exist, it is created (if creation fails, returns 500 `create directory failed`).

The options are as follows.

- --password=password \[SSP 2.9.26\]……Extracts a password-protected ZIP using the specified password. If a password is required but none is specified, or if the password is incorrect, extraction fails with 500 (`password mismatch`) without showing a password prompt (in \[SSP 2.9.25\], a password could not be specified, and a password prompt appeared, stopping the ghost).
- [`--async`](../async.md)

On success, returns 200, with the number of files extracted in `Result`, the number of bytes after compression in `Value0`, and the number of bytes after extraction in `Value1` (decimal integers). These are the same values as `Reference1`–`Reference3` of [OnExtractArchiveComplete](../../../list/shiori-event/other/OnExtractArchiveComplete.md) for SSTP EXECUTE; with [`--async`](../async.md), they are returned in `Reference1` (`Result`) and `Reference4` and `Reference5` (`Value0` and `Value1`).<br />
For archives such as 7z that do not store the compressed size for each entry, `Value0` may be 0.<br />
\[SSP 2.9.26\] The total for archives containing multiple files is returned correctly for ZIP as well (in \[SSP 2.9.25\], the byte count was for the last file only).

Failures are as follows. 400 is returned for `file not found` (archive to extract does not exist) / `invalid parameter` (missing argument, empty path) / `ghost required` / `path not allowed` (destination is outside folders managed by SSP). 500 indicates `create directory failed` or the reason extraction failed, such as `open failed`, `crc`, or `password mismatch`.

For security reasons, the destination is restricted to locations under folders managed by SSP (such as the ghost and balloon folders, and locations specified in the “Folders” settings). Paths are checked after resolving `..` and similar components. This restriction may be strengthened as appropriate, so it is safest to limit the destination to a location under the folder containing the ghost's own data.

## Supported formats

The archive format is determined by the file name extension (for self-extracting `exe` files, the contents are checked and the ZIP or 7z archive inside is extracted). Unrecognized formats fail with 500.

- **ZIP**: `.zip` `.zipx` `.nar`
- **LZH**: `.lzh` `.lha`
- **CAB**: `.cab`
- **7z**: `.7z`
- **tar family**: `.tar` `.tar.gz`（`.tgz`） `.tar.xz`（`.txz`） `.tar.bz2`（`.tbz2` `.tbz`） `.tar.lzma`（`.tlz`） `.tar.zst`（`.tzst`） `.tar.br`（`.tbr`） `.tar.Z`（`.taz`） `.cpio` `.deb` `.udeb` `.rpm`
- **Single-file compression**: `.gz` `.bz2` `.xz` `.lzma` `.zst` `.zstd` `.br` `.Z` (extracted as an archive containing a single file)
- **Disk images**: `.iso` `.img`
- **Email**: `.eml`
- **Self-extracting**: `.exe`

`--password=` applies only to ZIP and 7z; it is ignored for other formats.

## 記述例

```
Argument0: ExtractArchive
Argument1: save/backup.zip
Argument2: save/restore
Argument3: --async=OnRestoreDone

→ 204（結果はOnRestoreDoneイベントで届く）
　Reference0: OnRestoreDone
　Reference1: 12（展開したファイル数）
　Reference2: internal_file
　Reference3: ExtractArchive
　Reference4: 圧縮後のバイト数
　Reference5: 展開後のバイト数
```

**対応:** SSP 2.9.25
