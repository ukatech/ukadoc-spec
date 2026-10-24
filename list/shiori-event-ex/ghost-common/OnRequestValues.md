# OnRequestValues

**カテゴリ:** ゴースト間汎用イベント

他ゴーストが任意に送信した際に発生。<br />
このイベントが送られた時、\\\[raiseother\]でOnGetValuesイベントを送信する必要がある。

- **Reference0**: 送信したゴースト名。
- **Reference1**: 要求する変数名(key)。Reference2以降も同様に要求する変数がある限り続く。

**対応:** SSP
