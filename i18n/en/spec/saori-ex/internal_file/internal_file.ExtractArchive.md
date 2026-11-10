# ExtractArchive

**カテゴリ:** internal_file

Extracts an archive (in addition to ZIP, this includes formats such as 7z and tar; see “Supported formats” below). This makes the same operation as `ExtractArchive` in [SSTP's EXECUTE](../../sstp/method_execute.md) callable through SAORI over DirectSSTP.<br />
Archive processing may take several seconds, so [`--async`](../async.md) is strongly recommended. If called synchronously, the ghost will stop while it runs.

- **Argument1**: Path to the archive to extract. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. A relative path passed in a call without a ghost results in 400 (`ghost required`). If the file does not exist (including a folder), the result is 400 (`file not found`).
- **Argument2**: Path to the folder to extract into. The format is the same as for Argument1. If the folder does not exist, it is created (if creation fails, the result is 500 `create directory failed`).

The options are as follows.

- --password=password \[SSP 2.9.26\]……Extracts a password-protected ZIP using the specified password. If a password is required but none is specified, or if the password is incorrect, extraction fails with 500 (`password mismatch`) without showing a password prompt (in \[SSP 2.9.25\], a password could not be specified, and a password prompt appeared, stopping the ghost).
- [`--async`](../async.md)

On success, the response is 200, with the number of extracted files in `Result`, the compressed size in bytes in `Value0`, and the extracted size in bytes in `Value1` (integers in decimal). These are the same values as `Reference1`–`Reference3` in [OnExtractArchiveComplete](../../../list/shiori-event/other/OnExtractArchiveComplete.md) for SSTP's EXECUTE; with [`--async`](../async.md), they are returned in `Reference1` (`Result`) and `Reference4` and `Reference5` (`Value0` and `Value1`).<br />
For archives such as 7z that do not store the compressed size for each entry, `Value0` may be 0.<br />
\[SSP 2.9.26\] ZIP archives containing multiple files also return the correct total (in \[SSP 2.9.25\], the size was that of the last file only).

Failures are as follows. 400 indicates `file not found` (the archive to extract does not exist) / `invalid parameter` (an argument is missing or a path is empty) / `ghost required` / `path not allowed` (the extraction destination is outside SSP-managed folders). 500 indicates `create directory failed` or the reason extraction failed (`open failed`, `crc`, `password mismatch`, etc.).

For security reasons, the extraction destination is restricted to locations under SSP-managed folders (locations specified in the “Folders” settings, such as ghost and balloon folders). Paths are checked after resolving `..` and similar components. Also, since this restriction may be strengthened as appropriate, it is safest to limit the destination to a folder containing the ghost's own data.

## Supported formats

The archive format is determined by the file name extension (for self-extracting `exe` files, the contents are inspected and the ZIP or 7z archive inside is extracted). If the format cannot be determined, extraction fails with 500.

- **ZIP**: `.zip` `.zipx` `.nar`
- **LZH**: `.lzh` `.lha`
- **CAB**: `.cab`
- **7z**: `.7z`
- **tar formats**: `.tar` `.tar.gz`（`.tgz`） `.tar.xz`（`.txz`） `.tar.bz2`（`.tbz2` `.tbz`） `.tar.lzma`（`.tlz`） `.tar.zst`（`.tzst`） `.tar.br`（`.tbr`） `.tar.Z`（`.taz`） `.cpio` `.deb` `.udeb` `.rpm`
- **Single-file compression**: `.gz` `.bz2` `.xz` `.lzma` `.zst` `.zstd` `.br` `.Z` (extracted as an archive containing one file)
- **Disk images**: `.iso` `.img`
- **Mail**: `.eml`
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
