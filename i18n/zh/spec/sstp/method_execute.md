# 方法：EXECUTE

通过EXECUTE方法，可以获取ghost的各种信息，以及执行不依赖Sakura Script的各种命令。<br />
执行此方法时，ghost不会说话，但其内部状态可能会改变。

## EXECUTE示例

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## request专用头

- **Command 或 Command\[param1,param2...\]**: 要执行的命令。执行内容和返回的信息见下文。<br />
  方括号及其后的部分用于指定传递给命令的参数。
- **Reference\* \[SSP\]**: 也可以使用Reference0及后续头指定参数，代替方括号。

有关Command头可指定的字符串和response中“附加数据”返回的结果，请参阅下文。

## Command头可指定的命令及返回的附加数据

- **GetName**: 运行中的ghost的（`\0`名）、（`\1`名），以逗号分隔
- **GetNames \[SSP\]**: 当前已安装的`\0`名列表。以换行分隔，以空行结束。
- **GetFMO \[SSP 2.5.57\] \[有远程限制\]**: 获取与[FMO](../fmo-mutex/index.md)内容等同的信息。<br />
  但仅限于通过SSTP通信的应用程序内部管理的部分，与由同时运行的应用程序共享的原始FMO不同。<br />
  主要供没有窗口、无法发送Direct SSTP的控制台应用程序等使用，仅通过Socket SSTP利用ReceiverGhostHWnd头实现相当于Direct SSTP的功能。<br />
  以换行分隔，以空行结束。<br />
  对于远程请求，各路径信息会被省略，头和hwnd会被替换为占位值。
- **GetGhostName \[SSP\]**: 运行中的ghost本体的名称（descript.txt中的name）
- **GetShellName \[SSP\]**: 运行中的ghost当前使用的shell名称
- **GetBalloonName \[SSP\]**: 运行中的ghost当前使用的balloon名称
- **GetVersion**: baseware（运行中的软件）的版本
- **GetGhostNameList \[SSP 2.6.53\]**: SSP识别的所有ghost名称（descript.txt中的name）列表，以换行分隔
- **GetShellNameList \[SSP 2.6.53\]**: 运行中的ghost识别的所有shell名称（descript.txt中的name）列表，以换行分隔
- **GetBalloonNameList \[SSP 2.6.53\]**: SSP识别的所有balloon名称（descript.txt中的name）列表，以换行分隔
- **GetHeadlineNameList \[SSP 2.6.53\]**: SSP识别的所有headline名称（descript.txt中的name）列表，以换行分隔
- **GetPluginNameList \[SSP 2.6.53\]**: SSP识别的所有plugin名称（descript.txt中的name）列表，以换行分隔
- **GetGhostUUIDList \[SSP 2.9.35\]**: SSP识别的所有ghost的[UUID](../../list/propertysystem/property-system/general-property/uuid.md)列表，以换行分隔。顺序与GetGhostNameList相同。<br />
  **GetBalloonUUIDList \[SSP 2.9.35\]**: 所有balloon的UUID。顺序与GetBalloonNameList相同。<br />
  **GetShellUUIDList \[SSP 2.9.35\]**: 运行中的ghost识别的所有shell的UUID。顺序与GetShellNameList相同。<br />
  UUID按照[metainfo-standard](https://github.com/ukatech/metainfo-standard)的步骤，从descript.txt的值计算得出（与属性系统的`uuid`相同）。
- **GetGhostMetaInfoList \[SSP 2.9.35\]**: SSP识别的所有ghost的metainfo文件夹URL列表，以换行分隔。顺序与GetGhostNameList相同。<br />
  **GetBalloonMetaInfoList \[SSP 2.9.35\]**: 所有balloon的metainfo文件夹URL。顺序与GetBalloonNameList相同。<br />
  **GetShellMetaInfoList \[SSP 2.9.35\]**: 运行中的ghost识别的所有shell的metainfo文件夹URL。顺序与GetShellNameList相同。<br />
  使用descript.txt的[metainfo](../../descript/ghost/descript-txt/metainfo.md)值。如果没有，则使用从[githubrepo](../../descript/ghost/descript-txt/githubrepo.md)推导出的URL（默认分支视为`master`）。两者都没有时为空行。
- **GetShortVersion \[SSP 2.6.53\]**: baseware（运行中的软件）的版本（仅包含以句点分隔的版本号）<br />
  与[version.json](https://ssp.shillest.net/archive/version.json)中的ssp.full.version等直接比较，即可检查是否为最新版本
- **GetStatus \[SSP 2.8.94\]**: 运行中的ghost当前的执行状态。内容与SHIORI/3.0 request的Status头及属性系统的[currentghost.status](../../list/propertysystem/property-system/currentghost.status.md)相同。<br />
  符合多个状态时以逗号分隔。各值的含义参见[※SHIORI Status头](../../list/propertysystem/property-system/currentghost.status.md)。<br />
  不符合任何状态时没有附加数据（状态码200）<br />
  \[SSP 2.9.39\] EXECUTE的GetStatus还包含`scriptbusy`（有等待播放的脚本或正在播放）。`talking`在队列中的脚本间隙以及接受脚本后到开始播放前会消失，但`scriptbusy`会保留。SEND的响应在脚本加入队列后返回，因此紧接着读取时一定能看到该状态。它不会加入SHIORI/3.0 request的Status头和`currentghost.status`（以免改变ghost侧的判断）。
- **SetTimeShift \[SSP 2.9.39\] \[不可远程执行\]**: 不通过ghost脚本，同步设置“虚拟更改当前时间”（时间机器）的时间差。用于测试依赖日期或时间的ghost。<br />
  参数0：指定时间差。格式与[`\![timemachine,set,値]`](../../list/sakura-script/misc/bang-timemachine-set-value.md)的值相同（`+秒` / `-秒` / `0` / ISO8601格式的日期时间）。不是加到当前时间差上，而是将时间差设为此值。<br />
  仅在启动SSP时指定了 `--allow-timemachine-control` 才接受此命令。未指定时不执行任何操作，以420失败，并在错误日志中记录警告。不能远程执行（420）。省略值或值无法解析时以400失败（时间差不变）。<br />
  成功时，在附加数据中返回设置后的时间差（秒，带符号整数）（状态码200）。收到响应时，时间差已生效，属性`system.os.timeshift`也会返回该值。时间差仅在本次运行期间有效，不会保存到设置中。
- **Quiet \[不可远程执行\]**: 保持静默，直到执行Restore或经过16秒。无附加数据（状态码为200系列时成功）
- **Restore**: 解除Quiet。无附加数据（状态码为200系列时成功）
- **CompressArchive \[SSP 2.7.23\] \[不可远程执行\]**: 将指定文件夹内的文件压缩为ZIP文件。如果目标文件的扩展名为`.7z`，则使用7z格式，否则使用ZIP格式（即使指定`.lzh`或`.cab`，内容也是ZIP）。不包含隐藏文件和隐藏文件夹。<br />
  参数0：压缩文件名（指定完整路径，不可使用相对路径）<br />
  参数1：要压缩的文件夹的完整路径<br />
  参数2及以后：选项（可省略）<br />
  选项如下。<br />
  --event=事件标识符……指定事件标识符后，响应返回后继续压缩，完成时触发事件。如果标识符以On开头，则触发该标识符对应的事件，否则触发OnCompressArchiveComplete或OnCompressArchiveFailure。省略时，直到处理完成才返回响应。<br />
  --password=密码……使用指定密码启用AES加密ZIP。<br />
  操作完成后的事件规格参见[OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md)和[OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 从SAORI over DirectSSTP也可以通过[internal_file的CompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md)调用（可以指定相对路径或使用`/`分隔）。<br />
  \[SSP 2.9.33\] 参数1不是文件夹（如文件路径）时，不进行压缩并以400失败（如果指定了`--event=`，则以`invalid parameter`触发失败事件（OnCompressArchiveFailure或标识符后附加`Failure`））。此前传入文件路径时，压缩会失败（`file not found`）。<br />
  出于安全考虑，压缩目标仅限于SSP管理的文件夹（ghost文件夹、balloon文件夹等在“文件夹”设置中指定的位置）及其子目录。<br />
  此外，由于该限制可能随时加强，最好将目标限定在存放ghost自身数据的文件夹及其子目录内。<br />
  无附加数据（状态码为200系列时成功）
- **ExtractArchive \[SSP 2.7.23\] \[不可远程执行\]**: 解压指定的归档文件。除ZIP外，也可以解压7z和tar等格式（支持的格式参见[internal_file的ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式)）。<br />
  参数0：压缩文件名（指定完整路径，不可使用相对路径）<br />
  参数1：解压目标文件夹的完整路径<br />
  参数2及以后：选项（可省略）<br />
  选项如下。<br />
  --event=事件标识符……指定事件标识符后，响应返回后继续解压，完成时触发事件。如果标识符以On开头，则触发该标识符对应的事件，否则触发OnExtractArchiveComplete或OnExtractArchiveFailure。省略时，直到处理完成才返回响应。<br />
  --password=密码……使用指定密码解压。\[SSP 2.9.26\] 不显示密码输入对话框。需要密码但未指定或密码错误时，不显示对话框直接失败（响应为500，如果指定了事件，则触发标识符＋Failure或[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)）。\[SSP 2.9.25\]及以前版本会忽略此选项并显示对话框。<br />
  \[SSP 2.9.26\] 即使将含有`..`的绝对路径指定为解压目标，如果解析后的路径在SSP管理的文件夹之外，也会被拒绝（此前可以解压到管理范围之外）。<br />
  操作完成后的事件规格参见[OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md)和[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 从SAORI over DirectSSTP也可以通过[internal_file的ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md)调用（可以指定相对路径或使用`/`分隔）。<br />
  出于安全考虑，解压目标仅限于SSP管理的文件夹（ghost文件夹、balloon文件夹等在“文件夹”设置中指定的位置）及其子目录。<br />
  此外，由于该限制可能随时加强，最好将目标限定在存放ghost自身数据的文件夹及其子目录内。<br />
  无附加数据（状态码为200系列时成功）
- **DumpSurface \[SSP 2.5.98\] \[不可远程执行\]**: 将合成后的surface图像输出到指定目录。参数与[`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md)相同。<br />
  但不能指定事件ID，须按目录、scope ID、surface列表、prefix、从零位置裁切、动画ID \[SSP 2.9.05\] 的顺序指定。<br />
  \[SSP 2.9.08\] 与Sakura Script版相同，也可以使用--dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation= 格式，按任意顺序指定，并可与上述按顺序指定的方式混用（不以--开头的参数按出现顺序依次分配给上述项目）。除目录外均可省略，省略scope ID时为0。--event=会被忽略。<br />
  由于DumpSurface\[...\]格式的参数中不能写逗号，包含逗号的surface列表应在Reference0及后续头中指定。<br />
  请注意，直到处理完成才会返回响应。<br />
  无附加数据（状态码为200系列时成功）
- **MoveAsync \[SSP\] \[不可远程执行\]**: 不通过Sakura Script执行与[`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md)相同的操作。参数指定方法与Sakura Script版相同。<br />
  由于无法在SSTP超时前返回response且会导致死锁，因此不能执行不带async的move。<br />
  无附加数据（状态码为200系列时成功）
- **SetTrayIcon \[SSP\] \[不可远程执行\]**: 不通过Sakura Script执行与[`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)相同的操作。参数指定方法与Sakura Script版相同。<br />
  无附加数据（状态码为200系列时成功）
- **SetTrayBalloon \[SSP\] \[不可远程执行\]**: 不通过Sakura Script执行与[`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md)相同的操作。参数指定方法与Sakura Script版相同。<br />
  无附加数据（状态码为200系列时成功）
- **SetProperty \[SSP\] \[不可远程执行\]**: 向[属性系统](../../list/propertysystem/index.md)写入值。<br />
  参数0：属性名称<br />
  参数1：要设置的值<br />
  无附加数据（状态码为200系列时成功）
- **GetProperty \[SSP\]**: 从[属性系统](../../list/propertysystem/index.md)读取值。<br />
  参数0：属性名称<br />
  附加数据为获取到的属性值。
- **SetCookie**: 写入按Sender指定的客户端名称分别保存的通用数据存储区。<br />
  其用途与浏览器的“Cookie”类似。<br />
  参数0：Cookie名称<br />
  参数1：要设置的值<br />
  无附加数据（状态码为200系列时成功）
- **GetCookie**: 从按Sender指定的客户端名称分别保存的通用数据存储区读取数据。<br />
  参数0：Cookie名称<br />
  附加数据为获取到的Cookie值。
