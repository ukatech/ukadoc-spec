# OnInternalSaoriComplete

**カテゴリ:** その他イベント

[SAORI over DirectSSTP](../../../spec/saori-ex/index.md)で内蔵モジュールを`--async=識別子`付きで呼び出したとき、処理が成功すると送られる。識別子がOnで始まる場合は、このイベントの代わりに識別子と同じ名前のイベントが送られる。<br />
詳しくは[非同期の呼び出し](../../../spec/saori-ex/async.md)を参照。

- **Reference0**: --async=で指定した識別子。
- **Reference1**: 結果。(同期の呼び出しの Result)
- **Reference2**: モジュール名。(internal_crypto など)
- **Reference3**: 関数名。(Digest など)
- **Reference4以降**: 複数の値を返す関数の値。(同期の呼び出しの Value0 以降)

**対応:** SSP 2.9.13
