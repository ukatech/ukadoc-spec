# OnInternalSaoriComplete

**カテゴリ:** 其他事件

透過 [SAORI over DirectSSTP](../../../spec/saori-ex/index.md) 呼叫內建模組，並附上 `--async=識別子` 時，處理成功後會送出此事件。若識別碼以 On 開頭，則會改為送出與識別碼同名的事件。<br />
詳細資訊請參閱[非同步呼叫](../../../spec/saori-ex/async.md)。

- **Reference0**: 以 --async= 指定的識別碼。
- **Reference1**: 結果。（等同於同步呼叫的 Result）
- **Reference2**: 模組名稱。（例如 internal_crypto）
- **Reference3**: 函式名稱。（例如 Digest）
- **Reference4 以後**: 回傳多個值的函式所回傳的值。（等同於同步呼叫的 Value0 以後）

**対応:** SSP 2.9.13
