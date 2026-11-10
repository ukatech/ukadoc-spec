# CompressArchive

**カテゴリ:** internal_file

Compresses a folder into a ZIP file (or 7z file). This makes the same operation as `CompressArchive` in [SSTP's EXECUTE](../../sstp/method_execute.md) callable via SAORI over DirectSSTP.<br />
The archive format is determined by the extension of the destination. `.7z` means 7z (compressed using LZMA); all other extensions mean ZIP (even if `.lzh` or `.cab` is specified, the contents will be ZIP).<br />
Archive processing may take several seconds, so using [`--async`](../async.md) is strongly recommended. If called synchronously, the ghost will stop during processing.

- **Argument1**: Path to the destination archive. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. If a relative path is passed when called without a ghost, the result is 400 (`ghost required`).
- **Argument2**: Path to the folder to compress (files inside are included recursively, but hidden files and hidden folders, including their contents, are excluded). Written in the same way as Argument1. If it does not exist, the result is 400 (`file not found`). This path is not limited to folders managed by SSP; folders outside its management can also be compressed (only the destination is restricted). \[SSP 2.9.33\] Passing a path that is not a folder (such as a file path) results in 400 (`invalid parameter`). Before this version, passing a file path failed with 500 (`file not found`).

The options are as follows (if the same name is specified twice, the later one takes effect).

- --password=password……Encrypts using the specified password (AES-encrypted ZIP for ZIP archives).
- --option=option……Specify the following values **together as a single comma-separated value** (for example, `--option=overwrite,lzma`. If `--option=` is specified twice, only the later one takes effect).<br />
  overwrite……Replace the destination archive if it already exists.<br />
  append……Append to the destination archive if it already exists.<br />
  lzma……Compress using LZMA (for ZIP; 7z always uses LZMA, so specifying this has no effect).<br />
  headerencrypt……Also encrypt the header (list of file names) (requires `--password=`). **Works only with 7z and has no effect with ZIP** (file names remain unencrypted in ZIP).<br />
  If the destination archive already exists and neither `overwrite` nor `append` is specified, the result is 400 (`file exists`).

On success, the result is 200, with the number of compressed files in `Result`, the compressed size in bytes in `Value0`, and the uncompressed size in bytes in `Value1` (decimal integers). These are the same values as `Reference1`–`Reference3` of SSTP's EXECUTE [OnCompressArchiveComplete](../../../list/shiori-event/other/OnCompressArchiveComplete.md). With [`--async`](../async.md), they are returned in `Reference1` (`Result`) and `Reference4` and `Reference5` (`Value0` and `Value1`).<br />
For ZIP, `Value0` is the number of bytes added to the archive (including the header and central directory; only the added amount when using `append`), so it is slightly larger than the size of the compressed data alone.<br />
\[SSP 2.9.26\] The file count and byte sizes are also returned correctly for ZIP (in \[SSP 2.9.25\], compressing to ZIP returned 0).

Failures are as follows. 400 indicates `file not found` (source does not exist) / `invalid parameter` (missing argument, empty path, invalid option, or, \[SSP 2.9.33\], source is not a folder) / `ghost required` / `file exists` / `path not allowed` (destination is outside folders managed by SSP). 500 indicates the reason compression failed, such as `open failed`.

For security reasons, the destination is restricted to locations under folders managed by SSP (locations specified in settings such as the ghost and balloon folders). The path is checked after resolving `..` and similar components. Since these restrictions may be strengthened as needed, it is safer to limit the destination to locations under the folder containing the ghost's own data.

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
