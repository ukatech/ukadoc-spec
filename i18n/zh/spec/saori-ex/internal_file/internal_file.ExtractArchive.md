# ExtractArchive

**カテゴリ:** internal_file

解压缩档案（除 ZIP 外，也包括 7z、tar 等。请参阅下方的“支持的格式”）。此功能可通过 SAORI over DirectSSTP 调用，与[SSTP 的 EXECUTE](../../sstp/method_execute.md)中的`ExtractArchive`执行相同的处理。<br />
档案处理可能需要数秒，因此强烈建议使用[`--async`](../async.md)。同步调用时，ghost 会在处理期间停止。

- **Argument1**: 要解压缩的档案路径。相对路径以 ghost 文件夹（ghost/master）为基准。路径分隔符可使用`/`或`\`。在没有 ghost 的情况下调用并传入相对路径时，会返回 400（`ghost required`）。文件不存在（包括文件夹）时，会返回 400（`file not found`）。
- **Argument2**: 解压缩目标文件夹的路径。写法与 Argument1 相同。文件夹不存在时会创建（无法创建时返回 500 `create directory failed`）。

选项如下。

- --password=密码 \[SSP 2.9.26\]……使用指定的密码解压缩带密码保护的 ZIP。如果需要密码但未指定密码，或指定的密码不正确，则不会显示密码输入对话框，而会返回 500（`password mismatch`）并失败（在\[SSP 2.9.25\]中无法指定密码，会显示密码输入对话框，并导致 ghost 停止）。
- [`--async`](../async.md)

成功时返回 200，`Result`中包含解压缩的文件数，`Value0`中包含压缩后的字节数，`Value1`中包含解压缩后的字节数（十进制整数）。这些值与 SSTP 的 EXECUTE 的[OnExtractArchiveComplete](../../../list/shiori-event/other/OnExtractArchiveComplete.md)的`Reference1`～`Reference3`相同；使用[`--async`](../async.md)时，则分别存入`Reference1`（`Result`）和`Reference4`、`Reference5`（`Value0`、`Value1`）。<br />
对于 7z 等没有各个条目压缩后大小信息的档案，`Value0`可能为 0。<br />
\[SSP 2.9.26\] ZIP 档案也能正确返回包含多个文件的档案总大小（在\[SSP 2.9.25\]中，返回的字节数会是最后一个文件的大小）。

失败时的返回值如下。400 表示`file not found`（要解压缩的档案不存在）/ `invalid parameter`（缺少参数或路径为空）/ `ghost required` / `path not allowed`（解压缩目标位于 SSP 管理文件夹之外）。500 表示`create directory failed`，或解压缩失败的原因（例如`open failed`、`crc`、`password mismatch`）。

出于安全考虑，解压目标路径仅限于 SSP 管理的文件夹（例如 ghost 文件夹、balloon 文件夹等通过「文件夹」设置指定的位置）下。检查路径时，会先解析 `..` 等路径部分。由于此限制今后可能会适时收紧，最好将目标路径限制在存放 ghost 自身数据的文件夹下。

## 支持的格式

根据文件名扩展名判断压缩包格式（对于自解压的 `exe`，会检查其内容并解压其中的 ZIP 或 7z）。无法识别的格式会以 500 错误失败。

- **ZIP**: `.zip` `.zipx` `.nar`
- **LZH**: `.lzh` `.lha`
- **CAB**: `.cab`
- **7z**: `.7z`
- **tar 系**: `.tar` `.tar.gz`（`.tgz`） `.tar.xz`（`.txz`） `.tar.bz2`（`.tbz2` `.tbz`） `.tar.lzma`（`.tlz`） `.tar.zst`（`.tzst`） `.tar.br`（`.tbr`） `.tar.Z`（`.taz`） `.cpio` `.deb` `.udeb` `.rpm`
- **单文件压缩格式**: `.gz` `.bz2` `.xz` `.lzma` `.zst` `.zstd` `.br` `.Z`（作为仅包含一个文件的压缩包解压）
- **磁盘映像**: `.iso` `.img`
- **邮件**: `.eml`
- **自解压格式**: `.exe`

`--password=` 仅对 ZIP 和 7z 有效，在其他格式中会被忽略。

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
