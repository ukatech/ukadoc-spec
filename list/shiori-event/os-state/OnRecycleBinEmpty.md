# OnRecycleBinEmpty

**カテゴリ:** OS状態イベント

[`\![execute,emptyrecyclebin]`](../../sakura-script/misc/bang-execute-emptyrecyclebin.md)でゴミ箱を空にした時に発生する。<br />
スクリプトを実行したゴーストだけでなく、起動中の全ゴーストにもOnRecycleBinEmptyFromOtherが通知される。

- **Reference0**: 現在ゴミ箱に入っているファイルの数(空にした直後なのでふつうは0)
- **Reference1**: 現在ゴミ箱に入っているファイルのサイズ(空にした直後なのでふつうは0) 単位バイト
- **Reference2**: 現在ゴミ箱に入っているファイルの数の直前との差(空にした直後なのでふつうは負の値)
- **Reference3**: 現在ゴミ箱に入っているファイルのサイズの直前との差(空にした直後なのでふつうは負の値) 単位バイト
- **Reference4**: 正常に空にできたら1、何かエラーが起きたら0(もとから空っぽでも0)
- **Reference5**: タグを実行したゴーストの本体側の名前(sakuraname)。

**対応:** SSP 2.6.04/Ref4は2.6.35
