# request/response

与SHIORI等其他协议一样，这是模仿HTTP的自定义协议。<br />
请求必须指定Charset，未指定时会报错，或被按OS默认指定的字符编码解释。

- 换行符为CR+LF。
- 请求以空行结束（与前一行的行尾合计为(CR+LF)x2）。
- 响应末尾在EXECUTE等情况下可能包含附加数据。头部结束后隔一个空行，再写入附加数据，最后再以一个空行结束。没有附加数据时，可能仅以头部后的空行结束。
- 包含附加数据的响应出于兼容性考虑，可能完全不返回包括Charset在内的头部，而只返回附加数据。此时可以假定其字符编码与请求相同。
- 请求和响应的SSTP版本可能不同。不要依赖版本号进行解释。

## request

### request示例

```
SEND SSTP/1.0
Charset: UTF-8
Sender: SSTPクライアント
Script: \h\s0テストー。\u\s[10]テストやな。
Option: notranslate
```

### request中各方法共有的头部

方法特有的头部请参阅后面各方法的说明。

- **Charset**: 请求的字符编码。建议出现在第一行。<br />
  除非有特殊原因，推荐使用UTF-8。
- **Sender**: 表示发送者的字符串。例如“SSTP发送工具”。对于COMMUNICATE方法，为发送源ghost的`\0`名称。
- **SecurityLevel**: 指定由SHIORI或Sakura Script处理时的安全级别。取local或external。<br />
  仅对DirectSSTP或来自127.0.0.1等明显为本地的请求有效。<br />
  SSTP over HTTP始终视为external，除非请求来自由localhost提供的html等。
- **SecurityOrigin \[SSP 2.6.59\]**: 表示发送源服务器的类URL字符串。格式如下。其理念与[HTTP头部的Origin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)相同。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme通常为http、https、sstp之一。hostname为发送源服务器名或IP。port为可接收回复的端口。<br />
  未指定时，视为指定了null。<br />
  SSTP over HTTP始终使用HTTP的Origin头部内容，忽略SSTP中的SecurityOrigin。
- **Option**: 指定SSTP执行的Sakura Script的处理方式。<br />
  可以用逗号分隔指定多个选项。可指定的字符串如下。<br />
  nodescript : 禁用balloon中的SSTP显示（禁用来自远程的SSTP）<br />
  notranslate : 不执行OnTranslate或MAKOTO的翻译处理<br />
  nobreak : 不中断当前执行的脚本，等待其结束<br />
  strict : 将Sakura Script解释失败的位置记录到错误日志。包括指定不存在的surface（`\s`）、动画（`\i`）或balloon（`\b`），未知的标签、`\![コマンド]`、`\&[実体参照]`，缺少必要的\[\]或数字，以及`\p`、`\b`、`\n`、`\c`、`\q`的无效值。对SEND的脚本以及NOTIFY/GIVE中ghost返回的脚本有效 \[SSP 2.8.94\]
- **ID**: 称为“Owned SSTP”的机制。指定由[SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md)发送的ID或[FMO的识别ID（仅SSP）](../fmo-mutex/index.md)后，将忽略各种安全检查和锁定等，以与ghost内部处理相同的优先级处理此SSTP。<br />
  SecurityLevel将设为local，并且即使处于`\t`等禁止中断的状态，也能强制中断并播放。
- **X-SSTP-PassThru-(任意の文字列)**: 在NOTIFY等与ghost侧的通信中直接传递给SHIORI的头部。<br />
  只进行字符编码转换等最低限度的处理，任意字符串部分和内容均原样转发。
- **HWnd**: 仅限DirectSSTP，表示应接收response的窗口句柄。<br />
  将窗口句柄（相当于指针）数据作为无符号十进制整数处理，再转换为字符串。<br />
  省略时使用WM_COMMUNICATE的wParam。
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: 仅限(Socket)SSTP，表示应接收request的ghost的`\0`窗口句柄。<br />
  指定后，待处理的ghost将被固定，即使通过Socket也能进行与DirectSSTP相同的处理。<br />
  未找到时，立即以404 Not Found结束并报错。
- **ReceiverGhostName \[SSP 2.5.57\]**: 仅限(Socket)SSTP，表示应接收request的ghost的`\0`名称。<br />
  指定后，待处理的ghost将被固定，即使通过Socket也能进行与DirectSSTP相同的处理。是HWnd的名称版。<br />
  \[SSP 2.9.35\] 也可以填写UUID代替名称，从而指定该UUID对应的ghost（与专用的ReceiverGhostUUID相同）。<br />
  未找到时，立即以404 Not Found结束并报错。
- **ReceiverGhostUUID \[SSP 2.9.35\]**: 仅限(Socket)SSTP，表示应接收request的运行中ghost的[UUID](../../list/propertysystem/property-system/general-property/uuid.md)。<br />
  指定后，待处理的ghost将被固定，即使通过Socket也能进行与DirectSSTP相同的处理。是HWnd的UUID版，可以避免混淆同名ghost。<br />
  如果有多个相同UUID的ghost正在运行，则选择正在显示的ghost；如果没有，则选择运行中ghost列表的第一个。<br />
  如果运行中的ghost没有匹配的UUID，则立即以404 Not Found结束并报错（不符合UUID格式的值也一样）。<br />
  如果同时指定了ReceiverGhostHWnd、ReceiverGhostUUID和ReceiverGhostName中的多个，则按此顺序求值，使用第一个找到的ghost。

## response

### response示例（无数据）

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。
```

### response示例（有数据）

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。

追加データはここ
```

### response中各方法共有的头部

- **Charset**: 请求的字符编码。建议出现在第一行。<br />
  除非有特殊原因，推荐使用UTF-8。<br />
  为解决兼容性问题，有时会有意省略。此时应假定字符编码与request相同。
- **X-SSTP-PassThru-(任意の文字列)**: 在NOTIFY等与ghost侧的通信中由SHIORI直接返回的头部。<br />
  只进行字符编码转换等最低限度的处理，任意字符串部分和内容均原样转发。

### response的状态码

与HTTP一样，200系列表示正常受理，其他表示错误。

- **200 OK**: 正常结束（带返回值）
- **204 No Content**: 正常结束（无返回值）
- **210 Break**: 已执行，但在脚本执行过程中被中断<br />
  ※仅限带Entry的SEND/1.x等极少数情况，通常立即返回200或204。
- **400 Bad Request**: 请求存在某种无法处理的错误
- **404 Not Found ※仅SSP**: 在指定ghost的SSTP中，指定的ghost未安装或未运行
- **408 Request Timeout**: 超时：无法与ghost/SHIORI侧通信等情况（通常几乎不会发生）
- **409 Conflict**: 处于`\t`标签等禁止中断的状态，或正在处理其他请求
- **413 Payload Too Large ※仅SSP**: SSTP请求过长，拒绝处理
- **420 Refuse**: 因ghost侧的设置而拒绝接收
- **500 Internal Server Error ※仅SSP**: 因处理系统内部检测到的某种问题而无法完成处理
- **501 Not Implemented**: 包含未实现的命令等，无法处理
- **503 Service Unavailable**: 因处理系统内部原因，处于无法接受SSTP的状态
- **505 Version Not Supported ※仅SSP**: SSTP版本异常（低于1.0、3.0及以上等）
- **512 Invisible**: ghost因最小化等原因未显示，处于无法进行任何处理的状态
