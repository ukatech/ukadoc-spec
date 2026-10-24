# 概要

SSTPはゴースト間の汎用通信仕様です。単純なSakuraScriptの再生や、外部からのイベント通知等に使えます。<br />
通信は基本的にはTCP/IPで行われます。ポート9801または9821(SSPのみ)をリスニングしており、SSTPプロトコルに従ってリクエストを投げると、処理結果が返ってきます。<br />
セキュリティ上の都合で、現在は設定を変更しない限りlocalhost限定でのリスニングとなり、端末外部からは通信できません。また、昔はポート11000番もリスニングしていましたが、マルウェアによる通信と誤認されたことから現在では廃止されています。<br />
起動時に待ち受け先を一時的に指定する[--sstp-listen](https://ssp.shillest.net/ukadoc/ssphelp/option.html#general)など、SSPの起動オプションについては[SSPヘルプの起動オプション](https://ssp.shillest.net/ukadoc/ssphelp/option.html)を参照してください。<br />
[IANAのPort number registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=sakura+script)には7743と9801番が登録されていますが、実運用されているのは9801番のみです。<br />
同じ略称のプロトコルにMicrosoftが策定したVPN通信のためのSecure Socket Tunneling Protocolがありますが、技術上の関連性はありません。<br />
既定では毎回通信終了時に切断されます。頻繁に通信する場合は、HTTPと同様の[keep-alive](keepalive.md)で接続を使い回すことができます \[SSP 2.9.03\]。
