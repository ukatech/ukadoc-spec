# response

## 示例

```
SHIORI/3.0 200 OK
Charset: UTF-8
Sender: AYA
Value: \1\s[10]\0\s[0]\e
```

※换行符为CR+LF。<br />
※最后以空行结束（加上前一行的终止符，共(CR+LF)x2）。

- **状态码**: 与HTTP相同，200系列表示成功，其他表示某种失败（错误）。<br />
  当前主要使用以下状态码。

  - **200**: 200 OK<br />
    成功，有返回值(Value)。
  - **204**: 204 No Content<br />
    成功，无返回值。
  - **311**: 311 Not Enough<br />
    ID: OnTeach（SHIORI/2系列的TEACH方法）表示需要更多补充信息。<br />
    再次打开输入框询问用户，输入完成后添加包含输入字符串的Reference。
  - **312**: 312 Advice<br />
    ID: OnTeach（SHIORI/2系列的TEACH方法）表示最近输入的字符串无法解析，应予以丢弃。<br />
    丢弃最后一个Reference，再次打开输入框询问用户，输入完成后添加包含输入字符串的Reference。
  - **400**: 400 Bad Request<br />
    请求字符串无法解析。
  - **500**: 500 Internal Server Error<br />
    SHIORI内部发生某种错误，无法返回响应。

- **Charset**: 字符编码。最好放在第一行，或者至少放在任何包含非ASCII字符的行之前。

- **Sender**: 发送方。通常是SHIORI的名称。

- **Value**: 要说出的脚本。

- **ValueNotify \[SSP扩展 2.5.35\]**: *\[实验性功能\]*<br />
  即使请求方法为NOTIFY，也能执行Sakura Script的扩展功能。<br />
  通过此标头返回Sakura Script时，会立即执行。如果是GET，则会在执行Value标头中的脚本之前执行。<br />
  可执行的标签极其有限，其他标签和所有其他字符串都会被忽略。<br />
  <del>当方法不是NOTIFY或Value标头已存在时，会被忽略。</del> 2.6.76取消限制<br />
  当前可执行的标签如下：

  - `\![sound]`
  - `\![set,trayicon]`
  - `\![set,trayballoon]`
  - `\![raise]`
  - `\![raiseother]`
  - `\![raiseplugin]`
  - `\![timerraiseother]`
  - `\![timerraiseplugin]`
  - `\![notify]`
  - `\![notifyother]`
  - `\![notifyplugin]`
  - `\![get,property]` ＋2.6.82
  - `\![set,property]` ＋2.6.82

- **SecurityLevel \[SSP扩展\]**: 以下任一值。

  - **local**: 相当于来自正在运行的设备内部脚本的安全级别。
  - **external**: 相当于来自正在运行的设备外部脚本的安全级别。

  要说出的脚本的SecurityLevel。如果为external，部分脚本会因安全功能而无法执行。

- **Marker \[SSP扩展\]**: 要显示在balloon标记（balloon下方的附加信息）中的字符串。

- **ErrorLevel \[SSP扩展\]**: SHIORI内部发生的错误级别。以下任一值。要表示多个错误时，以字节值1分隔。

  - **info**: 信息。不是错误。
  - **notice**: 通知。虽难以称为错误，但存在应修正的描述等。
  - **warning**: 警告。存在描述错误等问题，处理尚未停止，但最好进行处理。
  - **error**: 一般错误。由于描述错误等原因，某项处理停止且无法继续。
  - **critical**: 致命错误。比error更严重，应立即采取某种措施。

  存在此标头时，会通知用户发生了某种错误。<br />
  通知的级别可由用户更改设置。通常为error及以上。<br />
  在SSP中，错误会记录到错误日志，并在通知区域显示错误图标。

- **ErrorDescription \[SSP扩展\]**: SHIORI内部发生错误的详细信息。仅在存在ErrorLevel时有效。<br />
  要表示多个错误时，以字节值1分隔。<br />
  ErrorLevel和ErrorDescription的元素数量必须相同。

- **BalloonOffset \[SSP扩展\]**: balloon的偏移值(X,Y)。

- **Reference0**: 要发送communicate时，ghost的`\0`侧名称。

- **Reference1～**: communicate的附加信息。<br />
  响应的Reference1＝SSTP Communicate的Reference0＝接收方OnCommunicate的Reference2<br />
  请注意，由于兼容性问题，以上对应关系会发生偏移。

- **Age \[SSP扩展\]**: communicate的世代数。初次为零。每进行一轮交互便+1。<br />
  虽然是SSP扩展，但实际上是SHIORI/2.x兼容处理。

- **MarkerSend \[SSP扩展\]**: communicate期间要显示在“对方一侧”的balloon标记字符串。<br />
  作为SSTP的Marker标头发送。

- **X-SSTP-PassThru-(任意字符串) \[SSP 2.5.03～扩展\]**: 仅当收到来自SSTP的事件通知时，此标头才会原样添加到SSTP响应中。<br />
  非SSTP情况下会被忽略。<br />
  可以指定多个标头，但要返回多个标头时，请更改标头名称。<br />
  （旧标头名称：X-SSTP-Return- 计划废止）
