# OnBIFFComplete

**カテゴリ:** メールチェックイベント

メールチェックが成功した際に発生。

- **Reference0**: スプールされているメールの通数、１オリジン表記。
- **Reference1**: スプールされているメールのバイト数。
- **Reference2**: チェックするメールサーバ名。
- **Reference3**: メールの新着差分。
- **Reference4**: 全メールのTopResult。POP通信全ヘッダリスト。メールごとバイト値2区切りの、ヘッダごとバイト値1区切り（通常はReference7の情報を利用すればよい）。
- **Reference5**: ListResult。メールサーバ上のID。POPコマンドの「LIST」の結果に相当する内容。
- **Reference6**: UidlResult。メールを区別するためのID。POPコマンドの「UIDL」の結果に相当する内容。
- **Reference7**: バイト値1区切りの送信者とタイトル。

**対応:** Materia / SSP / CROW
