# request

## 示例

```
GET SHIORI/3.0
Charset: UTF-8
Sender: SSP
SenderType: internal,raise
SecurityLevel: local
Status: choosing,balloon(0=0)
ID: OnFirstBoot
BaseID: OnBoot
Reference0: 1
```

※换行符为 CR+LF。<br />
※最后以空行结束（与前一行的结束符合计为 (CR+LF)x2）。

- **方法**:

  - **GET**: 预期会在响应的 Value 头中返回某些内容的方法。
  - **NOTIFY**: 预期不返回任何值的方法。响应的 Value 头会被忽略。<br />
    主要用于受某些模式限制而“无法说话”的状态，或启动后立即发送的状态通知事件。<br />
    请注意，同一个 ID（事件名）可能同时使用 GET 和 NOTIFY。

- **Charset**: 字符编码。最好放在第一行，或至少放在任何包含 ASCII 范围以外字符的行之前。

- **Sender**: 事件发送方。

- **SenderType \[SSP 2.5.05～扩張\]**: 事件发送方的属性，如下所示。多个值以逗号连接。<br />
  对于 ID: OnTranslate，会继承被转译事件的属性。

  - **internal**: 来自应用程序内部的事件。
  - **external**: 来自应用程序外部的事件。
  - **sakuraapi**: 由 Sakura API 触发的事件。
  - **embed**: 由 `\![embed]` 标签触发的事件。
  - **raise**: 由 `\![raise]` 标签触发的事件。
  - **property**: 由属性系统的引用命令触发的事件。
  - **plugin**: 由插件触发的事件。
  - **sstp**: 由 SSTP 触发的事件。
  - **communicate**: 由 communicate 规范触发的事件。

- **SecurityLevel**: 脚本执行时的安全级别，为以下值之一。<br />
  对于 ID: OnTranslate，会继承被转译事件的属性。<br />
  尽可能在靠前的行中通知，至少会出现在 ID 头之前。

  - **local**: 来自运行设备本机的通知。
  - **external**: 来自运行设备外部的通知。

  external 表示通知来自运行机器外部，因此需要谨慎处理以确保安全。<br />
  这是与 SenderType 的 internal/external 不同的概念。即使事件来自应用程序外部，只要可视为安全，也会被判定为 local，因此 SenderType 为 external 时，SecurityLevel 也可能为 local。

- **SecurityOrigin \[SSP拡張\]**: 表示发送方服务器的类 URL 字符串，格式如下。其概念与 [HTTP 头的 Origin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin) 相同。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme 通常是 http、https 或 sstp。hostname 是发送方服务器名称或 IP。port 是可接受回复的端口。<br />
  如果 SSTP 等未指定该头，或本身不存在发送方概念等，即没有相关信息时，值为 null。<br />
  另请参阅 SSTP 规范中的 SecurityOrigin。

- **Status \[SSP拡張\]**: ghost 的运行状态，如下所示。多个值以逗号连接。

  - **talking**: 正在说话
  - **choosing**: 正在显示选项
  - **minimizing**: 正在最小化
  - **induction**: 正处于 `\![enter,inductionmode]` 中
  - **passive**: 正处于 `\![enter,passivemode]` 中
  - **timecritical**: 正处于时间关键区段（`\t`）中
  - **nouserbreak**: 正处于 `\![enter,nouserbreak]` 中
  - **online**: 正在进行网络通信
  - **opening(種類)**: 输入框等处于打开状态。<br />
    打开多个类型时，以 / 分隔列出。<br />
    "dialog" 表示文件选择器、颜色选择器等。<br />
    示例：opening(communicate/input/teach/dialog)
  - **balloon(ID群)**: balloon 处于显示状态。<br />
    按“角色 ID=balloon ID”的格式列出。<br />
    同时打开多个时，以 / 分隔列出。<br />
    示例：balloon(0=2/1=0) 表示 `\0` 正在显示较大的 balloon，`\1` 正在显示普通 balloon。

- **ID**: 事件名或文本资源的标识符。

- **BaseID \[SSP拡張\]**: 可兼容的基本事件名。<br />
  例如，OnFirstBoot 与 OnBoot 兼容，而且 OnFirstBoot 是 OnBoot 的变体，因此 OnFirstBoot 的 BaseID 为 OnBoot。

- **Reference\***: 与事件关联的附加信息。Reference 后跟数字。行数不受限制（受内存容量限制）。

- **X-SSTP-PassThru-(任意の文字列) \[SSP 2.5.05～拡張\]**: 仅当事件通知来自 SSTP 时，SSTP 请求头中以 "X-SSTP-PassThru-" 开头的字段才会原样通知。<br />
  非 SSTP 时不会添加。
