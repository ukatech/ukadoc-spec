# 内置模块的通用规则

这是 SSP 内置的名称以`internal_`开头的模块的通用规则。（为了避免与同名的 SAORI DLL 冲突，名称以`internal_`开头。）<br />
这些模块只能通过 Direct SSTP 调用。不能将其作为 DLL 加载。

## 函数和参数

`Argument0`是函数名（不区分大小写），`Argument1`及之后是该函数的参数。未知函数名会返回 400（`unknown function`）。<br />
参数由每个函数规定数量的**位置参数**，以及其后排列的**选项**（`--名称=值`）组成。

- 位于位置参数位置的值即使以`--`开头，也不会作为选项读取，而是作为数据处理。
- 选项只能写在位置参数之后。跳过可省略的位置参数来写选项时，请放置空参数。
- 选项名称不区分大小写。同名选项写了两次时，后一个生效。
- 没有`=`的`--名称`等同于值为空的`--名称=`。也可以写值为空的选项。例如，`--aad=`表示“空的附加认证数据”。但是，将没有意义的选项（例如`--async=`、`--iv=`）设为空值会导致该函数失败（通常是 400 `invalid parameter`）。
- 接收数值的参数和选项使用十进制整数，可以带符号（`+` `-`）。不能写空白、十六进制或小数。无法读取为数值时返回 400（`invalid parameter`），超出 64 位有符号整数范围时返回 400（`out of range`）。数值的范围由各函数规定。
- 位置参数之后出现的、不以`--`开头的值，以及函数不接受的选项，都会返回 400（`invalid parameter`）。将较新 SSP 增加的选项传给旧版 SSP 时也会出现这种情况，因此可以通过[internal_system 的 Describe](internal_system/internal_system.Describe.md)查询是否支持。
- \[SSP 2.9.25\] 对于位置参数数量不固定的函数（[internal_file 的 MediaInfo](internal_file/internal_file.MediaInfo.md)和\[SSP 2.9.27\] [ImageInfo](internal_file/internal_file.ImageInfo.md)），从第二个及之后的位置起，第一个以`--`开头的值及其后的内容会作为选项读取。
- 所有函数都接受[`--async=标识符`](async.md)。

```
Argument0: Digest
Argument1: sha256
Argument2: SGVsbG8=
Argument3: --data-in=base64
Argument4: --out=base64
```

## 字节序列的输入格式

哈希等操作会处理字节序列，但通过 SAORI 传递的只能是字符串。接收字节序列的参数各自都有名称（例如`data`、`key`、`password`、`salt`、`ciphertext`、`signature`、`a`、`b`等，请参阅各函数的说明），可以通过`--名称-in=格式`更改该参数的读取方式。例如：`--key-in=hex`、`--data-in=base64`。<br />
通过选项传递的字节序列（`--aad=`、`--iv=`、`--info=`）也一样，可以通过`--aad-in=hex`之类的选项更改读取方式。

- **text**：将字符串转换为`--charset=`指定字符集的字节序列（默认是**UTF-8**）。这不是请求的`Charset`（无论发送方使用什么字符集，都能获得与 Web API 签名等相同的值）。如果有字符无法用该字符集表示，则返回 400（`invalid encoding`）。
- **hex**：十六进制。大小写均可。位数为奇数或包含非十六进制字符时，返回 400（`invalid encoding`）。
- **base64 / base64url**：可以有也可以没有填充（`=`）。两种格式都会读取 base64 和 base64url 的字符（`+ / - _`）。包含其他字符或填充有误时，返回 400（`invalid encoding`）。
- **base32**：RFC 4648。大小写和是否带填充均不限制。包含无效字符时，返回 400（`invalid encoding`）。
- **url**：还原百分号编码。`+`不会还原为空格。`%`后不是两个十六进制数字时，返回 400（`invalid encoding`）。
- **bech32**：\[SSP 2.9.14\] BIP-173 的 bech32（例如 nostr 的`npub1...` / `nsec1...`等。不支持读取 bech32m）。将数据部分转换为字节序列。不会检查`1`之前的部分（hrp，例如`npub`），因此需要确认类型时，请在脚本中检查字符串开头。可以全用大写或全用小写。大小写混用、校验和错误或包含无效字符时，返回 400（`invalid encoding`）。没有长度限制（BIP-173 的 90 个字符）。
- **file**：将值作为文件路径读取文件内容。只能用于`internal_crypto`的`Digest` / `HMAC`的`data`（用于其他函数或`data`以外的参数时，会返回 400 `invalid parameter`）。<br />
  路径规则见[文件路径](#ファイルのパス)。文件不存在时返回 400（`file not found`），读取过程中发生错误时返回 500（`file read failed`）。

默认格式由各参数分别规定（请参阅各函数的说明）。每个参数解码后的数据最多为 8MB（`too large`），但 Direct SSTP 的请求本身最多为 1MB，因此实际限制会更小。`file`会分块读取，因此没有大小上限。

## 字节序列的输出格式

返回字节序列的函数可以通过`--out=格式`更改结果的写法。默认格式由各函数规定。输出的默认格式与同名输入的默认格式一致，因此可以将输出值直接传给其他函数。

- **hex**：十六进制（小写）。
- **HEX**：十六进制（大写）。格式名称不区分大小写，但`--out=`中的`HEX`是例外，只有写成`HEX`时才会使用大写（`Hex`会输出小写十六进制）。在输入的`--名称-in=`中，`HEX`与`hex`会以相同格式读取。
- **base64**：带填充。
- **base64url**：不带填充。
- **base32**：RFC 4648。带填充。
- **url**：将所有 RFC 3986 非保留字符（`A-Z a-z 0-9 - . _ ~`）以外的字符转换为`%XX`（大写）。
- **bech32**：\[SSP 2.9.14\] BIP-173 的 bech32（小写）。使用`--hrp=`指定 hrp（例如`npub`，长度为 1～83 个字符）。只有[internal_data 的 Convert](internal_data/internal_data.Convert.md)接受`--hrp=`；其他函数使用`--out=bech32`时会返回 400（`invalid parameter`）。
- **text**：作为`--charset=`指定字符集（默认 UTF-8）的字符串返回。字节序列无法用该字符集正确还原，或包含 NUL、换行（无法写入 SAORI 标头）时，返回 500（`not text`）。<br />
  响应会以请求的`Charset`字符集返回，因此无法用该字符集表示的字符会变成`?`。为确保能接收任何字符，请使用`Charset: UTF-8`发送请求。

`--charset=`中填写字符集名称（例如`UTF-8`、`Shift_JIS`、`EUC-JP`）。未知名称以及 UTF-16、UTF-32 会返回 400（`invalid parameter`）。

## 文件路径

以下接收文件的参数（`--data-in=file`和[internal_file](internal_file/index.md)的各个函数）共用此规则。

- 相对路径以 ghost 文件夹（ghost/master）为基准。在没有 ghost 的情况下调用并传入相对路径时，会返回 400（`ghost required`）。
- 分隔符可以使用`/`或`\`。
- 将文件夹传给接收文件的参数时，会视为文件不存在，并返回 400（`file not found`）。
- \[SSP 2.9.33\] 将文件传给接收文件夹的参数（`CompressArchive`的压缩源）时，会返回 400（`invalid parameter`）。
- **读取目标不受限制。** 仅读取文件的处理（使用`--data-in=file`进行哈希、`MediaInfo` / `ImageInfo` / `IsMediaLoadable` / `IsImageLoadable`、`ExtractArchive`的压缩包、`CompressArchive`的压缩源）如果使用绝对路径，也可以读取 SSP 管理文件夹之外的文件。只有写入目标（`CompressArchive`的压缩目标、`ExtractArchive`的解压目标）会限制在 SSP 管理的文件夹内。可以通过是否返回`file not found`来判断文件是否存在，因此不要直接将用户输入等内容作为路径传入。

## 响应和失败原因

成功时返回 200，结果存入`Result`。结果为空字符串时返回 204。返回布尔值的函数会以 200 返回`1`（真）或`0`（假）。“不匹配”等情况不算失败。<br />
失败时的[ErrorDescription](directsstp.md)除了通用原因外，还可能包含以下内容。

- **unsupported algorithm**：400。未知的算法名称。
- **invalid encoding**：400。无法按`--名称-in=`指定的格式读取时，或压缩数据损坏时。
- **invalid key**：400。密钥长度与算法不匹配时，或无法读取为公钥加密密钥、密钥类型与方式不匹配时。
- **out of range**：400。数值或日期时间超出可处理范围。
- **too large**：400。数据过大。
- **file not found**：400。`--data-in=file`指定的文件不存在。
- **not text**：500。使用`--out=text`时无法还原为字符串。
- **file read failed**：500。文件读取过程中发生错误。
- **authentication failed**：500。无法解密时（例如密文被篡改或密钥不匹配）。无法验证 JWT 时也会出现。
- **expired / not yet valid**：500。JWT 已过有效期（`exp`）/ 尚未到生效时间（`nbf`）。
- **internal error**：500。baseware 内部发生预期之外的错误。
