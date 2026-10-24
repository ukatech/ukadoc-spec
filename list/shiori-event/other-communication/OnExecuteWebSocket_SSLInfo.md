# OnExecuteWebSocket_SSLInfo

**カテゴリ:** その他通信イベント

wss://接続時にSSL/TLS接続が確立したときに発生。初回接続時のみ発火し、Upgradeの成否にかかわらず発火する。イベント名は常に固定で--asyncオプションによる変更は不可。

- **Reference0**: Sakura Scriptの--asyncオプションで指定されたイベント識別子。
- **Reference1～**: [OnExecuteHTTPSSLInfoのReference1以降と同じ](OnExecuteHTTPSSLInfo.md)。

**対応:** SSP 2.8.05
