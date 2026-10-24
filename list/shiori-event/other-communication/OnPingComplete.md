# OnPingComplete

**カテゴリ:** その他通信イベント

`\![execute,ping]`で指定回数のping実行完了時に発生。

- **Reference0**: --eventで指定した文字列そのもの
- **Reference1**: 送信元アドレス \[`\1`\] 全送信回数 \[`\1`\] 成功回数 \[`\1`\] 失敗回数 \[`\1`\]はバイト値1
- **Reference2**: 「OK」またはエラー情報 \[`\1`\] 返答元アドレス \[`\1`\] RTT(往復にかかった時間ms) \[`\1`\]はバイト値1<br />
  Reference2以降、送信済みのPingの1回ごとの情報が記録される。Progressの場合は不完全。<br />
  エラー情報は[ICMP_ECHO_REPLY Structure の Statusヘッダ](http://msdn.microsoft.com/en-us/library/aa366053%28v=vs.85%29.aspx)を参照。

**対応:** SSP
