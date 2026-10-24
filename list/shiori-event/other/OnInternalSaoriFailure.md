# OnInternalSaoriFailure

**カテゴリ:** その他イベント

[SAORI over DirectSSTP](../../../spec/saori-ex/index.md)で内蔵モジュールを`--async=識別子`付きで呼び出したとき、処理が失敗すると送られる。識別子がOnで始まる場合は、このイベントの代わりに「識別子＋Failure」という名前のイベントが送られる。<br />
詳しくは[非同期の呼び出し](../../../spec/saori-ex/async.md)を参照。

- **Reference0**: --async=で指定した識別子。
- **Reference1**: 失敗理由。(同期の呼び出しの ErrorDescription と同じ。invalid encoding など)
- **Reference2**: モジュール名。
- **Reference3**: 関数名。

**対応:** SSP 2.9.13
