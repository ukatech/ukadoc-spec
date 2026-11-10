# OnInternalSaoriFailure

**カテゴリ:** 其他事件

透過 [SAORI over DirectSSTP](../../../spec/saori-ex/index.md) 呼叫內建模組，並附上 `--async=識別子` 時，處理失敗後會送出此事件。若識別碼以 On 開頭，則會改為送出名稱為「識別碼＋Failure」的事件。<br />
詳細資訊請參閱[非同步呼叫](../../../spec/saori-ex/async.md)。

- **Reference0**: 以 --async= 指定的識別碼。
- **Reference1**: 失敗原因。（與同步呼叫的 ErrorDescription 相同，例如 invalid encoding）
- **Reference2**: 模組名稱。
- **Reference3**: 函式名稱。

**対応:** SSP 2.9.13
