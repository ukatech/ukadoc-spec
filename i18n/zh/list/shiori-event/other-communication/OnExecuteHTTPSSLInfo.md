# OnExecuteHTTPSSLInfo

**カテゴリ:** 其他通信事件

即使获取失败（HTTP响应不是200），由于SSL/TLS层面的连接已成功，仍会发送通知。

即使通过--async・--sync指定了以On开头的ID，事件名也不会被替换，始终通过本事件发送通知。请通过Reference0判断这是哪个请求的通知。

- **Reference0**: async ID（没有则为空）
- **Reference1**: 获取URL
- **Reference2**: http响应代码（即使发生错误也会发送通知）
- **Reference3**: 通信版本 目前通常为 "TLSv1/SSLv3"（由于SSP内部会拒绝SSLv2，实际上只会收到这一种）
- **Reference4**: 加密方式<br />
  示例：AES256-SHA
- **Reference5**: 颁发对象 如果想确认名称，提取/O=后面的字符串即可<br />
  面向程序员：此处是经过OpenSSL的X509_NAME_oneline处理后的结果<br />
  示例：/1.3.6.1.4.1.311.60.2.1.3=US/1.3.6.1.4.1.311.60.2.1.2=Delaware/businessCategory=Private Organization/serialNumber=4337446/C=US/postalCode=94107/ST=California/L=San Francisco/street=795 Folsom St, Suite 600/O=Twitter, Inc./OU=Twitter Operations/CN=twitter.com
- **Reference6**: 有效期开始日期时间 年,月,日,时,分,秒<br />
  示例：2011,7,7,9,0,0
- **Reference7**: 有效期结束日期时间 年,月,日,时,分,秒<br />
  示例：2012,7,28,8,59,59
- **Reference8**: 颁发者 如果想确认名称，提取/O=后面的字符串即可<br />
  面向程序员：此处是经过OpenSSL的X509_NAME_oneline处理后的结果<br />
  示例：/C=US/O=VeriSign, Inc./OU=VeriSign Trust Network/OU=Terms of use at https://www.verisign.com/rpa (c)06/CN=VeriSign Class 3 Extended Validation SSL CA
- **Reference9 (2.4.51～)**: 证书链中的CommonName(CN)，按顺序以逗号分隔列出

**対応:** SSP
