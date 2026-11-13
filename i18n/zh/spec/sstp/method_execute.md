# 方法：EXECUTE

通过EXECUTE方法，可以获取ghost的各种信息，以及执行不依赖Sakura Script的各种命令。<br />
执行此方法时，ghost不会说话，但内部状态可能发生变化。

## EXECUTE示例

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## request专用头部

- **Command 或 Command\[param1,param2...\]**: 要执行的命令。执行的内容和返回的信息见下文。<br />
  在方括号中指定传递给要执行的命令的参数。
- **Reference\* \[SSP\]**: 除了使用方括号，也可以通过Reference0及后续头部指定参数。

有关Command头部可指定的字符串以及response的“附加数据”中返回的结果，请参阅下文。

## Command头部可指定的命令及返回的附加数据

- **GetName**: 运行中ghost的（`\0`名称）,（`\1`名称），以逗号分隔
- **GetNames \[SSP\]**: 当前已安装的`\0`名称列表。以换行分隔，以空行结束。
- **GetFMO \[SSP 2.5.57\] \[有远程限制\]**: 获取与[FMO](../fmo-mutex/index.md)内容相同的信息。<br />
  但仅限于通过SSTP通信的应用程序内部管理的信息，与由同时运行的应用程序共同使用的原始FMO不同。<br />
  主要供没有窗口且无法发送Direct SSTP的控制台应用程序等使用，仅通过Socket SSTP利用ReceiverGhostHWnd头部实现相当于Direct SSTP的功能。<br />
  以换行分隔，以空行结束。<br />
  如果是远程请求，各路径信息会被省略，头部和hwnd会被替换为占位值。
- **GetGhostName \[SSP\]**: 运行中ghost本体的名称（descript.txt的name）
- **GetShellName \[SSP\]**: 运行中ghost当前使用的shell的名称
- **GetBalloonName \[SSP\]**: 运行中ghost当前使用的balloon的名称
- **GetVersion**: baseware（运行中的软件）的版本
- **GetGhostNameList \[SSP 2.6.53\]**: SSP识别的所有ghost名称（descript.txt的name）列表，以换行分隔
- **GetShellNameList \[SSP 2.6.53\]**: 运行中ghost识别的所有shell名称（descript.txt的name）列表，以换行分隔
- **GetBalloonNameList \[SSP 2.6.53\]**: SSP识别的所有balloon名称（descript.txt的name）列表，以换行分隔
- **GetHeadlineNameList \[SSP 2.6.53\]**: SSP识别的所有headline名称（descript.txt的name）列表，以换行分隔
- **GetPluginNameList \[SSP 2.6.53\]**: SSP识别的所有plugin名称（descript.txt的name）列表，以换行分隔
- **GetGhostUUIDList \[SSP 2.9.35\]**: SSP识别的所有ghost的[UUID](../../list/propertysystem/property-system/general-property/uuid.md)列表，以换行分隔。顺序与GetGhostNameList相同。<br />
  **GetBalloonUUIDList \[SSP 2.9.35\]**: 所有balloon的UUID。顺序与GetBalloonNameList相同。<br />
  **GetShellUUIDList \[SSP 2.9.35\]**: 运行中ghost识别的所有shell的UUID。顺序与GetShellNameList相同。<br />
  UUID按照[metainfo-standard](https://github.com/ukatech/metainfo-standard)的步骤，根据descript.txt中的值计算（与属性系统的`uuid`相同）。
- **GetGhostMetaInfoList \[SSP 2.9.35\]**: SSP识别的所有ghost的metainfo文件夹URL列表，以换行分隔。顺序与GetGhostNameList相同。<br />
  **GetBalloonMetaInfoList \[SSP 2.9.35\]**: 所有balloon的metainfo文件夹URL。顺序与GetBalloonNameList相同。<br />
  **GetShellMetaInfoList \[SSP 2.9.35\]**: 运行中ghost识别的所有shell的metainfo文件夹URL。顺序与GetShellNameList相同。<br />
  使用descript.txt的[metainfo](../../descript/ghost/descript-txt/metainfo.md)值。如果没有，则使用从[githubrepo](../../descript/ghost/descript-txt/githubrepo.md)导出的URL（默认分支视为`master`）。两者都没有时为空行。
- **GetShortVersion \[SSP 2.6.53\]**: baseware（运行中的软件）的版本（仅包含以句点分隔的版本号）<br />
  与[version.json](https://ssp.shillest.net/archive/version.json)中的ssp.full.version等直接比较，即可检查是否为最新版本
- **GetStatus \[SSP 2.8.94\]**: 运行中ghost的当前运行状态。内容与SHIORI/3.0 request的Status头部及属性系统的[currentghost.status](../../list/propertysystem/property-system/currentghost.status.md)相同。<br />
  符合多个状态时以逗号分隔。各值的含义请参阅[※SHIORI Status头部](../../list/propertysystem/property-system/currentghost.status.md)。<br />
  不符合任何状态时，没有附加数据（状态码200）
- **Quiet \[不可远程使用\]**: 保持静默，直到执行Restore或经过16秒。无附加数据（状态码为200系列表示成功）
- **Restore**: 解除Quiet。无附加数据（状态码为200系列表示成功）
- **CompressArchive \[SSP 2.7.23\] \[不可远程使用\]**: 将指定文件夹内的文件压缩为ZIP文件。压缩目标的扩展名为`.7z`时使用7z格式，否则使用ZIP格式（即使指定`.lzh`或`.cab`，内容也是ZIP）。不包含隐藏文件和隐藏文件夹。<br />
  参数0：压缩文件名（指定完整路径，不能指定相对路径）<br />
  参数1：要压缩的文件夹的完整路径<br />
  参数2及以后：选项（可省略）<br />
  选项如下。<br />
  --event=事件标识符……指定事件标识符后，响应返回后会继续压缩，完成后触发事件。如果标识符以On开头，则触发该标识符对应的事件，否则触发OnCompressArchiveComplete或OnCompressArchiveFailure。省略时，直到处理完成才返回响应。<br />
  --password=密码……使用指定密码启用AES加密ZIP。<br />
  有关操作完成后事件的规格，请参阅[OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md)和[OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 从SAORI over DirectSSTP也可以通过[internal_file的CompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md)调用（也可以指定相对路径或使用`/`分隔）。<br />
  \[SSP 2.9.33\] 参数1不是文件夹时（如文件路径），不进行压缩，以400返回失败（如果指定了`--event=`，则以`invalid parameter`触发失败事件（OnCompressArchiveFailure，或在标识符后加上`Failure`））。在此之前，传入文件路径会导致压缩失败（`file not found`）。<br />
  出于安全考虑，压缩目标仅限于SSP管理的文件夹（如在“文件夹”设置中指定的ghost文件夹、balloon文件夹等）及其子目录。<br />
  此限制也可能适时加强，因此最好限定在存放ghost自身数据的文件夹及其子目录内。<br />
  无附加数据（状态码为200系列表示成功）
- **ExtractArchive \[SSP 2.7.23\] \[不可远程使用\]**: 解压指定的归档文件。除ZIP外，也可以解压7z、tar等格式（支持的格式请参阅[internal_file的ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式)）。<br />
  参数0：压缩文件名（指定完整路径，不能指定相对路径）<br />
  参数1：解压目标文件夹的完整路径<br />
  参数2及以后：选项（可省略）<br />
  选项如下。<br />
  --event=事件标识符……指定事件标识符后，响应返回后会继续解压，完成后触发事件。如果标识符以On开头，则触发该标识符对应的事件，否则触发OnExtractArchiveComplete或OnExtractArchiveFailure。省略时，直到处理完成才返回响应。<br />
  --password=密码……使用指定密码解压。\[SSP 2.9.26\] 不显示密码输入对话框。需要密码但未指定或密码错误时，不显示对话框，直接返回失败（响应为500；如果指定了事件，则触发标识符＋Failure或[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)）。\[SSP 2.9.25\]及以前的版本会忽略此选项并显示对话框。<br />
  \[SSP 2.9.26\] 即使将包含`..`的绝对路径指定为解压目标，如果解析后的路径位于SSP管理的文件夹之外，也会被拒绝（此前可以解压到管理范围之外）。<br />
  有关操作完成后事件的规格，请参阅[OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md)和[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 从SAORI over DirectSSTP也可以通过[internal_file的ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md)调用（也可以指定相对路径或使用`/`分隔）。<br />
  出于安全考虑，解压目标仅限于SSP管理的文件夹（如在“文件夹”设置中指定的ghost文件夹、balloon文件夹等）及其子目录。<br />
  此限制也可能适时加强，因此最好限定在存放ghost自身数据的文件夹及其子目录内。<br />
  无附加数据（状态码为200系列表示成功）
- **DumpSurface \[SSP 2.5.98\] \[不可远程使用\]**: 将合成后的surface图像输出到指定目录。参数与[`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md)相同。<br />
  但不能指定事件ID，参数依次为目录、scope ID、surface列表、prefix、从零位置裁剪、动画ID \[SSP 2.9.05\]。<br />
  \[SSP 2.9.08\] 与Sakura Script版本一样，也可以使用--dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation= 的格式按任意顺序指定，并可与上述顺序指定的参数混用（不以--开头的参数按出现顺序依次分配给上述参数）。除目录外均可省略，省略scope ID时默认为0。--event=会被忽略。<br />
  由于DumpSurface\[...\]格式的参数中不能使用逗号，包含逗号的surface列表应通过Reference0及后续头部指定。<br />
  注意，处理完成之前不会返回响应。<br />
  无附加数据（状态码为200系列表示成功）
- **MoveAsync \[SSP\] \[不可远程使用\]**: 不通过Sakura Script执行与[`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md)相同的操作。参数指定方法与Sakura Script版本相同。<br />
  由于无法在SSTP超时前返回response且会导致死锁，不能执行不带async的move。<br />
  无附加数据（状态码为200系列表示成功）
- **SetTrayIcon \[SSP\] \[不可远程使用\]**: 不通过Sakura Script执行与[`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)相同的操作。参数指定方法与Sakura Script版本相同。<br />
  无附加数据（状态码为200系列表示成功）
- **SetTrayBalloon \[SSP\] \[不可远程使用\]**: 不通过Sakura Script执行与[`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md)相同的操作。参数指定方法与Sakura Script版本相同。<br />
  无附加数据（状态码为200系列表示成功）
- **SetProperty \[SSP\] \[不可远程使用\]**: 向[属性系统](../../list/propertysystem/index.md)写入值。<br />
  参数0：属性名称<br />
  参数1：要设置的值<br />
  无附加数据（状态码为200系列表示成功）
- **GetProperty \[SSP\]**: 从[属性系统](../../list/propertysystem/index.md)读取值。<br />
  参数0：属性名称<br />
  附加数据为获取到的属性值。
- **SetCookie**: 写入按Sender指定的客户端名称分别保存的通用数据存储区。<br />
  预期用法与浏览器的“Cookie”类似。<br />
  参数0：Cookie名称<br />
  参数1：要设置的值<br />
  无附加数据（状态码为200系列表示成功）
- **GetCookie**: 从按Sender指定的客户端名称分别保存的通用数据存储区读取数据。<br />
  参数0：Cookie名称<br />
  附加数据为获取到的Cookie值。
