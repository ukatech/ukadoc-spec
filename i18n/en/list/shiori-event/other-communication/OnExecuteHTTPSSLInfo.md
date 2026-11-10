# OnExecuteHTTPSSLInfo

**カテゴリ:** Other communication events

This event is sent even if retrieval fails (the HTTP response is not 200), because the connection succeeded at the SSL/TLS level.

Even if an ID beginning with On is specified with --async or --sync, the event name is not replaced; this event is always sent. Use Reference0 to identify which request it is for.

- **Reference0**: async ID (empty if not specified)
- **Reference1**: Retrieval URL
- **Reference2**: HTTP response code (sent even in case of an error)
- **Reference3**: Communication protocol version. These days, this is usually "TLSv1/SSLv3" (SSP rejects SSLv2 internally, so this is actually the only value you will receive)
- **Reference4**: Encryption method<br />
  Example: AES256-SHA
- **Reference5**: Issuer. To check the name, extract the string following /O=<br />
  For programmers: contains the result of passing it through OpenSSL's X509_NAME_oneline<br />
  Example: /1.3.6.1.4.1.311.60.2.1.3=US/1.3.6.1.4.1.311.60.2.1.2=Delaware/businessCategory=Private Organization/serialNumber=4337446/C=US/postalCode=94107/ST=California/L=San Francisco/street=795 Folsom St, Suite 600/O=Twitter, Inc./OU=Twitter Operations/CN=twitter.com
- **Reference6**: Validity start date and time: year, month, day, hour, minute, second<br />
  Example: 2011,7,7,9,0,0
- **Reference7**: Validity end date and time: year, month, day, hour, minute, second<br />
  Example: 2012,7,28,8,59,59
- **Reference8**: Issuer. To check the name, extract the string following /O=<br />
  For programmers: contains the result of passing it through OpenSSL's X509_NAME_oneline<br />
  Example: /C=US/O=VeriSign, Inc./OU=VeriSign Trust Network/OU=Terms of use at https://www.verisign.com/rpa (c)06/CN=VeriSign Class 3 Extended Validation SSL CA
- **Reference9 (2.4.51～)**: Certificate chain CommonNames (CN), listed in order and separated by commas

**対応:** SSP
