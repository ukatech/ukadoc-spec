# OnPingComplete

**カテゴリ:** 其他通信事件

通过`\![execute,ping]`完成指定次数的ping时触发。

- **Reference0**: --event指定的字符串本身
- **Reference1**: 发送方地址 \[`\1`\] 发送总次数 \[`\1`\] 成功次数 \[`\1`\] 失败次数 \[`\1`\]为字节值1
- **Reference2**: “OK”或错误信息 \[`\1`\] 响应方地址 \[`\1`\] RTT（往返所需时间，单位为ms）\[`\1`\]为字节值1<br />
  从Reference2开始，记录已发送的每一次Ping的信息。Progress事件中的信息不完整。<br />
  错误信息请参阅[ICMP_ECHO_REPLY Structure 的 Status标头](http://msdn.microsoft.com/en-us/library/aa366053%28v=vs.85%29.aspx)。

**対応:** SSP
