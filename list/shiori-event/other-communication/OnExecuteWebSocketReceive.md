# OnExecuteWebSocketReceive

**カテゴリ:** その他通信イベント

WebSocket接続中にサーバーからデータフレームを受信するたびに発生。断片化フレームは自動的に再組み立てされてから発火する。Ping/Pong/Closeフレームでは発火しない。<br />
--asyncオプションで指定したeventIDが "On" で始まる場合はeventIDそのままがイベント名となる。

- **Reference0**: Sakura Scriptの--asyncオプションで指定されたイベント識別子。
- **Reference1**: 接続URL。
- **Reference2**: opcodeの種別。"1"=テキストフレーム (UTF-8)、"2"=バイナリフレーム。
- **Reference3**: 受信データ。テキストフレームの場合はUTF-8文字列そのまま(改行コードはバイト値1に変換)、バイナリフレームの場合はBase64エンコード文字列。

**対応:** SSP 2.8.05
