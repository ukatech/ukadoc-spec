# OnOtherSurfaceChange

**カテゴリ:** サーフェスイベント

（自分以外の）他のゴーストのサーフェス（表情）が変わった際に通知されます。<br />
負荷対策のため、標準では無効のイベントです。このイベントを使用するためには、事前に `\![set,othersurfacechange,true]` で有効化する必要があります。

- **Reference0**: ゴースト名
- **Reference1**: ゴーストSakura名
- **Reference2**: サーフェスが切り替わったウインドウID(Sakura=0)
- **Reference3**: 新サーフェスID
- **Reference4**: 旧サーフェスID
- **Reference5**: 新しいサーフェスの大きさ(座標：左,上,右,下)

**対応:** SSP / Ninix
