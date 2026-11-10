# ExtractArchive

**カテゴリ:** internal_file

Extracts an archive (including ZIP, 7z, tar, and other formats; see “Supported formats” below). This makes the same operation as `ExtractArchive` in [SSTP's EXECUTE](../../sstp/method_execute.md) callable via SAORI over DirectSSTP.<br />
Archive processing may take several seconds, so using [`--async`](../async.md) is strongly recommended. If called synchronously, the ghost will stop during processing.

- **Argument1**: Path to the archive to extract. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. If a relative path is passed when called without a ghost, the result is 400 (`ghost required`). If the file does not exist (including if it is a folder), the result is 400 (`file not found`).
- **Argument2**: Path to the destination folder. Written in the same way as Argument1. If the folder does not exist, it will be created (if it cannot be created, the result is 500 `create directory failed`).

The options are as follows.

- --password=password \[SSP 2.9.26\]……Extracts a password-protected ZIP using the specified password. If a password is required but none is specified, or if the password is incorrect, extraction fails with 500 (`password mismatch`) without showing a password-entry dialog (in \[SSP 2.9.25\], a password could not be specified, and a password-entry dialog appeared, stopping the ghost).
- [`--async`](../async.md)

On success, the result is 200, with the number of extracted files in `Result`, the compressed size in bytes in `Value0`, and the extracted size in bytes in `Value1` (decimal integers). These are the same values as `Reference1`–`Reference3` of SSTP's EXECUTE [OnExtractArchiveComplete](../../../list/shiori-event/other/OnExtractArchiveComplete.md). With [`--async`](../async.md), they are returned in `Reference1` (`Result`) and `Reference4` and `Reference5` (`Value0` and `Value1`).<br />
For archives such as 7z that do not store the compressed size for each entry, `Value0` may be 0.<br />
\[SSP 2.9.26\] The total size of archives containing multiple files is also returned correctly for ZIP (in \[SSP 2.9.25\], the byte size was that of the last file only).

Failures are as follows. 400 indicates `file not found` (archive to extract does not exist) / `invalid parameter` (missing argument or empty path) / `ghost required` / `path not allowed` (destination is outside folders managed by SSP). 500 indicates `create directory failed` or the reason extraction failed (such as `open failed`, `crc`, or `password mismatch`).

For security reasons, the destination is restricted to locations under folders managed by SSP (locations specified in settings such as the ghost and balloon folders). The path is checked after resolving `..` and similar components. Since these restrictions may be strengthened as needed, it is safer to limit the destination to locations under the folder containing the ghost's own data.

## Supported formats

The archive format is determined by the file name extension (for self-extracting `exe` files, the contents are examined and the ZIP or 7z archive inside is extracted). Unsupported formats fail with 500.

- **ZIP**: `.zip` `.zipx` `.nar`
- **LZH**: `.lzh` `.lha`
- **CAB**: `.cab`
- **7z**: `.7z`
- **tar-based**: `.tar` `.tar.gz` (`.tgz`) `.tar.xz` (`.txz`) `.tar.bz2` (`.tbz2` `.tbz`) `.tar.lzma` (`.tlz`) `.tar.zst` (`.tzst`) `.tar.br` (`.tbr`) `.tar.Z` (`.taz`) `.cpio` `.deb` `.udeb` `.rpm`
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
