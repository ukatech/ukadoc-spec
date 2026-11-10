# CompressArchive

**カテゴリ:** internal_file

将文件夹压缩为 ZIP 文件（或 7z 文件）。此功能与[SSTP 的 EXECUTE](../../sstp/method_execute.md)中的`CompressArchive`执行相同的处理，并可通过 SAORI over DirectSSTP 调用。<br />
压缩包格式由目标文件的扩展名决定。扩展名为`.7z`时使用 7z（以 LZMA 打包并压缩），其他情况均使用 ZIP（即使指定`.lzh`或`.cab`，内容也会是 ZIP）。<br />
压缩包处理可能需要数秒，因此强烈建议使用[`--async`](../async.md)。同步调用时，ghost 会在处理期间停止响应。

- **Argument1**: 目标压缩包的路径。相对路径以 ghost 文件夹（ghost/master）为基准。分隔符可使用`/`或`\`。在没有 ghost 的情况下调用并传入相对路径时，会返回 400（`ghost required`）。
- **Argument2**: 要压缩的文件夹路径（递归包含其中的文件，但不包含隐藏文件和隐藏文件夹（包括其中的内容））。写法与 Argument1 相同。路径不存在时会返回 400（`file not found`）。此路径不限于 SSP 管理的文件夹，也可以压缩管理范围之外的文件夹（仅目标路径受限）。\[SSP 2.9.33\]如果传入的不是文件夹（例如文件路径），会返回 400（`invalid parameter`）。在此版本之前，传入文件路径会返回 500（`file not found`）并失败。

选项如下（同名选项写入两次时，后写入的选项生效）。

- --password=密码……使用指定的密码加密（ZIP 使用 AES 加密）。
- --option=选项……将以下值用逗号分隔，**合并为一个值**指定（例如`--option=overwrite,lzma`。如果分开写两个`--option=`，只有后一个生效）。<br />
  overwrite……如果目标压缩包已存在，则替换它。<br />
  append……如果目标压缩包已存在，则追加内容。<br />
  lzma……使用 LZMA 压缩（适用于 ZIP。7z 始终使用 LZMA，因此指定此选项不会产生变化）。<br />
  headerencrypt……同时加密头部（文件名列表）（需要`--password=`）。**仅对 7z 生效，对 ZIP 不起作用**（ZIP 中的文件名仍会以未加密的形式保留）。<br />
  如果目标压缩包已存在，且未指定`overwrite`或`append`，则会返回 400（`file exists`）。

成功时返回 200，`Result`中包含压缩的文件数，`Value0`中包含压缩后的字节数，`Value1`中包含压缩前（解压后）的字节数（均为十进制整数）。这些值与 SSTP 的 EXECUTE 的[OnCompressArchiveComplete](../../../list/shiori-event/other/OnCompressArchiveComplete.md)中的`Reference1`～`Reference3`相同；使用[`--async`](../async.md)时，值会放入`Reference1`（`Result`）以及`Reference4`、`Reference5`（`Value0`、`Value1`）。<br />
ZIP 的`Value0`表示压缩包增加的字节数（包含头部和中央目录；使用`append`时仅包含追加部分），因此会比压缩数据本身的大小略大。<br />
\[SSP 2.9.26\] ZIP 格式下也会正确返回文件数和字节数（\[SSP 2.9.25\]中，压缩为 ZIP 时这些值为 0）。

失败时的返回值如下。400 表示`file not found`（压缩源不存在）/ `invalid parameter`（参数不足、路径为空、选项无效、\[SSP 2.9.33\] 压缩源不是文件夹）/ `ghost required` / `file exists` / `path not allowed`（目标路径位于 SSP 管理文件夹之外）。500 表示`open failed`等压缩失败原因。

出于安全考虑，目标路径仅限于 SSP 管理的文件夹（ghost 文件夹、balloon 文件夹等通过“文件夹”设置指定的位置）之下。检查时会先解析`..`等路径部分。此外，此限制可能会适时加强，因此最好将目标路径限制在存放 ghost 自身数据的文件夹之下。

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
