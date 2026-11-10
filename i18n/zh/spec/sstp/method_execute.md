# 方法：EXECUTE

使用 EXECUTE 方法，可以获取 ghost 的各种信息，也可以执行不依赖 Sakura Script 的各种命令。<br />
执行此方法时，ghost 不会说话，但内部状态可能会被改写。

## EXECUTE 示例

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## request 专用头

- **Command 或 Command\[param1,param2...\]**: 要执行的命令。执行内容和返回信息见下文。<br />
  可在方括号后指定要传递给命令的参数。
- **Reference\* \[SSP\]**: 也可以不使用方括号指定，而通过 Reference0～的头指定参数。

Command 头中可以指定的字符串，以及在 response 的“附加数据”中返回的结果，请参见下文。

## 可在 Command 头中指定的命令及其返回的附加数据

- **GetName**: 正在运行的 ghost 的 (`\0`名称),(`\1`名称)，以逗号分隔
- **GetNames \[SSP\]**: 当前已安装的`\0`名称列表。以换行分隔，以空行结束。
- **GetFMO \[SSP 2.5.57\] \[远程受限\]**: 获取与 [FMO](../fmo-mutex/index.md) 内容相同的信息。<br />
  但仅限于通过 SSTP 通信的应用程序内部管理的部分，与供同时运行的应用程序群共享的原本 FMO 不同。<br />
  主要用于没有窗口且无法发送 Direct SSTP 的控制台应用程序等场景，通过 Socket SSTP 使用 ReceiverGhostHWnd 头，实现相当于 Direct SSTP 的功能。<br />
  以换行分隔，以空行结束。<br />
  对于来自远程的请求，会省略各路径信息，并将头和 hwnd 替换为虚拟值。
- **GetGhostName \[SSP\]**: 正在运行的 ghost 本体名称（descript.txt 的 name）
- **GetShellName \[SSP\]**: 正在运行的 ghost 当前使用的 shell 名称
- **GetBalloonName \[SSP\]**: 正在运行的 ghost 当前使用的 balloon 名称
- **GetVersion**: baseware（正在运行的软件）的版本
- **GetGhostNameList \[SSP 2.6.53\]**: SSP 识别的所有 ghost 名称（descript.txt 的 name），以换行分隔的列表
- **GetShellNameList \[SSP 2.6.53\]**: 正在运行的 ghost 识别的所有 shell 名称（descript.txt 的 name），以换行分隔的列表
- **GetBalloonNameList \[SSP 2.6.53\]**: SSP 识别的所有 balloon 名称（descript.txt 的 name），以换行分隔的列表
- **GetHeadlineNameList \[SSP 2.6.53\]**: SSP 识别的所有 headline sensor 名称（descript.txt 的 name），以换行分隔的列表
- **GetPluginNameList \[SSP 2.6.53\]**: SSP 识别的所有 plugin 名称（descript.txt 的 name），以换行分隔的列表
- **GetShortVersion \[SSP 2.6.53\]**: baseware（正在运行的软件）的版本（仅包含以句点分隔的版本号）<br />
  与 [version.json](https://ssp.shillest.net/archive/version.json) 中的 ssp.full.version 等值进行简单比较，即可检查是否为最新版本
- **GetStatus \[SSP 2.8.94\]**: 正在运行的 ghost 当前的运行状态。内容与 SHIORI/3.0 request 的 Status 头以及属性系统的 [currentghost.status](../../list/propertysystem/property-system/currentghost.status.md) 相同。<br />
  如果符合多个状态，则以逗号分隔。各值的含义请参见 [※SHIORI Status 头](../../list/propertysystem/property-system/currentghost.status.md)。<br />
  如果不符合任何状态，则没有附加数据（状态码 200）
- **Quiet \[不可远程使用\]**: 静默，直到执行 Restore 或经过 16 秒。没有附加数据（状态码为 200 系列时表示成功）
- **Restore**: 解除 Quiet。没有附加数据（状态码为 200 系列时表示成功）
- **CompressArchive \[SSP 2.7.23\] \[不可远程使用\]**: 将指定文件夹中的文件压缩为 ZIP 文件。如果压缩目标的扩展名为`.7z`，则使用 7z 格式，否则使用 ZIP 格式（即使指定`.lzh`或`.cab`，内容也仍是 ZIP）。不包括隐藏文件和隐藏文件夹。<br />
  参数0：压缩文件名（指定完整路径，不可指定相对路径）<br />
  参数1：要压缩的文件夹的完整路径<br />
  参数2 及之后：选项（可省略）<br />
  选项如下。<br />
  --event=事件标识符……指定事件标识符后，会在 response 返回后继续压缩，完成时触发事件。如果标识符以 On 开头，则触发该标识符对应的事件；否则触发 OnCompressArchiveComplete 或 OnCompressArchiveFailure。省略时，直到处理完成才会返回 response。<br />
  --password=密码……使用指定的密码启用 AES 加密 ZIP。<br />
  操作完成后事件的相关规范请参见 [OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md)・[OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 从 SAORI over DirectSSTP 也可以通过 [internal_file 的 CompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md) 调用（也可以指定相对路径或使用`/`分隔）。<br />
  \[SSP 2.9.33\] 参数1不是文件夹（例如文件路径）时，不会进行压缩，并以 400 失败（如果指定了`--event=`，则会触发失败事件（OnCompressArchiveFailure，或在标识符后添加`Failure`的事件），事件内容为`invalid parameter`）。在此之前，传入文件路径时会因压缩失败而返回（`file not found`）。<br />
  出于安全考虑，压缩目标被限制在 SSP 管理的文件夹（ghost 文件夹、balloon 文件夹等通过“文件夹”设置指定的位置）内。<br />
  此外，此限制可能会适时加强，因此最好将目标限定在存放 ghost 自身数据的文件夹内。<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **ExtractArchive \[SSP 2.7.23\] \[不可远程使用\]**: 解压指定的归档文件。除 ZIP 外，也可以解压 7z、tar 等格式（支持的格式请参见 [internal_file 的 ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式)）。<br />
  参数0：压缩文件名（指定完整路径，不可指定相对路径）<br />
  参数1：解压目标文件夹的完整路径<br />
  参数2 及之后：选项（可省略）<br />
  选项如下。<br />
  --event=事件标识符……指定事件标识符后，会在 response 返回后继续解压，完成时触发事件。如果标识符以 On 开头，则触发该标识符对应的事件；否则触发 OnExtractArchiveComplete 或 OnExtractArchiveFailure。省略时，直到处理完成才会返回 response。<br />
  --password=密码……使用指定的密码解压。\[SSP 2.9.26\] 不会显示密码输入对话框。如果需要密码但未指定，或密码错误，则不会显示对话框而是失败（response 为 500；如果指定了事件，则触发标识符＋Failure，或 [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)）。在 \[SSP 2.9.25\] 之前，此选项会被忽略，并显示对话框。<br />
  \[SSP 2.9.26\] 即使将包含`..`的绝对路径指定为解压目标，如果解析后的路径位于 SSP 管理的文件夹之外，也会被拒绝（此前可以解压到管理范围之外）。<br />
  操作完成后事件的相关规范请参见 [OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md)・[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 从 SAORI over DirectSSTP 也可以通过 [internal_file 的 ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md) 调用（也可以指定相对路径或使用`/`分隔）。<br />
  出于安全考虑，解压目标被限制在 SSP 管理的文件夹（ghost 文件夹、balloon 文件夹等通过“文件夹”设置指定的位置）内。<br />
  此外，此限制可能会适时加强，因此最好将目标限定在存放 ghost 自身数据的文件夹内。<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **DumpSurface \[SSP 2.5.98\] \[不可远程使用\]**: 将合成后的 surface 图像输出到指定目录。参数与 [`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md) 相同。<br />
  但不能指定事件 ID，参数依次为目录、scope ID、surface 列表、prefix、零位置裁剪、动画 ID \[SSP 2.9.05\]。<br />
  \[SSP 2.9.08\] 与 SakuraScript 版本相同，也可以使用 --dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation= 的形式按任意顺序指定，也可以与上述顺序的参数混用（不以 -- 开头的参数按出现顺序依次对应上述参数）。除目录外均可省略；省略 scope ID 时使用 0。--event= 会被忽略。<br />
  DumpSurface\[...\]形式的参数中不能写逗号，因此包含逗号的 surface 列表应通过 Reference0 及之后的头指定。<br />
  请注意，直到处理完成才会返回 response。<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **MoveAsync \[SSP\] \[不可远程使用\]**: 不通过 SakuraScript 执行与 [`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md) 相同的操作。参数指定方法与 SakuraScript 版本相同。<br />
  由于无法在 SSTP 超时前返回 response，且会导致死锁，因此无法执行不带 async 的 move。<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **SetTrayIcon \[SSP\] \[不可远程使用\]**: 不通过 SakuraScript 执行与 [`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md) 相同的操作。参数指定方法与 SakuraScript 版本相同。<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **SetTrayBalloon \[SSP\] \[不可远程使用\]**: 不通过 SakuraScript 执行与 [`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md) 相同的操作。参数指定方法与 SakuraScript 版本相同。<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **SetProperty \[SSP\] \[不可远程使用\]**: 将值写入[属性系统](../../list/propertysystem/index.md)。<br />
  参数0：属性名称<br />
  参数1：要设置的值<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **GetProperty \[SSP\]**: 从[属性系统](../../list/propertysystem/index.md)读取值。<br />
  参数0：属性名称<br />
  附加数据为获取到的属性值。
- **SetCookie**: 将数据写入按 Sender 指定的客户端名称分别保存的通用数据存储区。<br />
  预期用途与浏览器的“Cookie”相同。<br />
  参数0：Cookie 名称<br />
  参数1：要设置的值<br />
  没有附加数据（状态码为 200 系列时表示成功）
- **GetCookie**: 从按 Sender 指定的客户端名称分别保存的通用数据存储区读取数据。<br />
  参数0：Cookie 名称<br />
  附加数据为获取到的 Cookie 值。
