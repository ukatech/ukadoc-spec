# OnExecuteHTTPSSLInfo

**カテゴリ:** その他通信イベント

取得失敗(HTTPレスポンスが200以外)でも、SSL/TLSレベルでは接続に成功しているので通知される。

--async・--syncでOnから始まるIDを指定した場合でも、イベント名は置き換わらず常に本イベントで通知される。どのリクエストのものかはReference0で判別すること。

- **Reference0**: async ID (無ければからっぽ)
- **Reference1**: 取得URL
- **Reference2**: httpレスポンスコード (エラーでも通知される)
- **Reference3**: 通信バージョン 今時はだいたい "TLSv1/SSLv3" (SSP内部でSSLv2は蹴るので実はこれだけしか来ない)
- **Reference4**: 暗号化方法<br />
  例：AES256-SHA
- **Reference5**: 発行先 名前を確認したい場合は、/O=の後に続く文字列を抜き出すと良い<br />
  プログラマさん向け：OpenSSLのX509_NAME_onelineに通した結果が入る<br />
  例：/1.3.6.1.4.1.311.60.2.1.3=US/1.3.6.1.4.1.311.60.2.1.2=Delaware/businessCategory=Private Organization/serialNumber=4337446/C=US/postalCode=94107/ST=California/L=San Francisco/street=795 Folsom St, Suite 600/O=Twitter, Inc./OU=Twitter Operations/CN=twitter.com
- **Reference6**: 有効期限開始日時 年,月,日,時,分,秒<br />
  例：2011,7,7,9,0,0
- **Reference7**: 有効期限終了日時 年,月,日,時,分,秒<br />
  例：2012,7,28,8,59,59
- **Reference8**: 発行者 名前を確認したい場合は、/O=の後に続く文字列を抜き出すと良い<br />
  プログラマさん向け：OpenSSLのX509_NAME_onelineに通した結果が入る<br />
  例：/C=US/O=VeriSign, Inc./OU=VeriSign Trust Network/OU=Terms of use at https://www.verisign.com/rpa (c)06/CN=VeriSign Class 3 Extended Validation SSL CA
- **Reference9 (2.4.51～)**: 証明書チェーン CommonName(CN)をカンマ区切りで順番に列挙

**対応:** SSP
