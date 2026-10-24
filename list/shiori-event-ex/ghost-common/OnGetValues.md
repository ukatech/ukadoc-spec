# OnGetValues

**カテゴリ:** ゴースト間汎用イベント

OnRequestValuesを受けた際に返すべきイベント。

- **Reference0**: 送信するゴースト名。
- **Reference1**: key=value(keyはOnRequestValuesで受け取った変数名、valueはその値)。Reference2以降も同様に要求された変数がある限り続く。存在しない変数は返さない。OnRequestValuesで送られた順序に依存しない。

**対応:** SSP
