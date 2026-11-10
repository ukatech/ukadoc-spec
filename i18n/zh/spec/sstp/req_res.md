# 请求/响应

与SHIORI等其他协议一样，这是一个仿照HTTP的自定义协议。<br />
请求必须指定Charset；如果未指定，则会出错，或被解释为OS默认字符编码。

- 换行符为CR+LF。
- 请求以空行结束（连同前一行的结尾，共为(CR+LF)x2）。
- 响应末尾可能包含EXECUTE等情况下的附加数据。标头结束后空一行，接着是附加数据，再空一行后结束。如果没有附加数据，也可能只以标头后的空行结束。
- 带附加数据的响应出于兼容性考虑，可能完全不含包括Charset在内的任何标头，只返回附加数据。这种情况下，可以假定其字符编码与请求相同。
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

### request各方法共用的标头

方法专用的标头请参阅后面的各方法说明。

- **Charset**: 请求的字符编码。最好出现在第一行。<br />
  如果没有特别理由，建议使用UTF-8。
- **Sender**: 表示发送者的字符串，例如「SSTP发送工具」。对于COMMUNICATE方法，这是发送方ghost的`\0`名称。
- **SecurityLevel**: 指定由SHIORI或Sakura Script处理时的安全级别。可指定local或external。<br />
  仅对DirectSSTP，或明显来自本地（例如127.0.0.1）的请求有效。<br />
  SSTP over HTTP始终被视为external，但从localhost提供的html等发送的情况除外。
- **SecurityOrigin \[SSP 2.6.59\]**: 表示来源服务器的类URL字符串。格式如下。其概念与[HTTP标头Origin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)相同。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme 通常为http、https或sstp之一。hostname为来源服务器名或IP。port为可接收回复的端口。<br />
  未特别指定时，视为指定了null。<br />
  SSTP over HTTP始终会设置HTTP的Origin标头内容，并忽略SSTP中的SecurityOrigin。
- **Option**: 指定SSTP执行的Sakura Script的处理选项。<br />
  可以用逗号分隔指定多个选项。可指定的字符串如下。<br />
  nodescript : 禁用在balloon中显示SSTP（禁用来自远程的SSTP）<br />
  notranslate : 不执行OnTranslate或MAKOTO的转换处理<br />
  nobreak : 不打断当前正在执行的脚本，等待其结束<br />
  strict : 将Sakura Script解析失败的位置记录到错误日志中。检查对象包括不存在的surface(`\s`)、动画(`\i`)、balloon(`\b`)指定，未知标签、`\![コマンド]`、`\&[実体参照]`、缺少必需的\[\]或数字，以及无效的`\p`、`\b`、`\n`、`\c`、`\q`值。对SEND的脚本，以及NOTIFY/GIVE中ghost返回的脚本有效 \[SSP 2.8.94\]
- **ID**: 此类请求称为"Owned SSTP"。指定通过[SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md)发送的ID，或[FMO识别ID（仅SSP）](../fmo-mutex/index.md)，即可忽略各种安全检查和锁定等，并以与ghost内部处理相同的优先级处理此SSTP。<br />
  SecurityLevel会设为local，即使处于禁止中断的状态（例如`\t`）也可以强制插入播放。
- **X-SSTP-PassThru-(任意字符串)**: 在与ghost侧通信（例如NOTIFY）时，直接传递给SHIORI的标头。<br />
  只进行字符编码转换等最低限度的处理，(任意字符串)部分及其内容会原样转发。
- **HWnd**: 仅限DirectSSTP，表示应发送response的窗口句柄。<br />
  将窗口句柄（相当于指针）的数据视为无符号十进制整数，并转换为字符串。<br />
  省略时使用WM_COMMUNICATE的wParam。
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: 仅限(Socket)SSTP，表示应发送request的ghost的`\0`窗口句柄。<br />
  指定后，待处理的ghost会被固定，通过Socket也可以进行与DirectSSTP相同的处理。<br />
  如果未找到，则立即以404 Not Found结束并报错。
- **ReceiverGhostName \[SSP 2.5.57\]**: 仅限(Socket)SSTP，表示应发送request的ghost的`\0`名称。<br />
  指定后，待处理的ghost会被固定，通过Socket也可以进行与DirectSSTP相同的处理。这是HWnd的名称版。<br />
  如果未找到，则立即以404 Not Found结束并报错。

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

### response各方法共用的标头

- **Charset**: 请求的字符编码。最好出现在第一行。<br />
  如果没有特别理由，建议使用UTF-8。<br />
  为解决兼容性问题，有时会故意省略。此时应假定字符编码与request相同。
- **X-SSTP-PassThru-(任意字符串)**: 在与ghost侧通信（例如NOTIFY）时，SHIORI直接返回的标头。<br />
  只进行字符编码转换等最低限度的处理，(任意字符串)部分及其内容会原样转发。

### response状态码

与HTTP一样，200系列表示正常受理，其他表示错误。

- **200 OK**: 正常结束（有返回值）
- **204 No Content**: 正常结束（无返回值）
- **210 Break**: 已执行，但在脚本执行过程中被中断<br />
  ※仅限带Entry的SEND/1.x等极为有限的情况，通常会立即返回200或204。
- **400 Bad Request**: 请求存在无法处理的缺陷
- **404 Not Found ※仅SSP**: 指定ghost的SSTP中，对应ghost未安装或未启动
- **408 Request Timeout**: 超时：例如无法与ghost/SHIORI通信时（通常几乎不会发生）
- **409 Conflict**: 处于禁止中断的状态（例如`\t`标签），或正在处理其他请求
- **413 Payload Too Large ※仅SSP**: SSTP请求过长，处理被拒绝
- **420 Refuse**: 因ghost侧设置而拒绝接收
- **500 Internal Server Error ※仅SSP**: 处理系统内部检测到某种问题，无法完成处理
- **501 Not Implemented**: 包含未实现的命令等，无法处理
- **503 Service Unavailable**: 因处理系统内部原因而无法接收SSTP
- **505 Version Not Supported ※仅SSP**: SSTP版本无效（例如低于1.0或高于等于3.0）
- **512 Invisible**: ghost因最小化等原因未显示，无法进行任何处理
