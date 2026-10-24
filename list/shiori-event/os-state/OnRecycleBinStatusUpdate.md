# OnRecycleBinStatusUpdate

**カテゴリ:** OS状態イベント

ゴミ箱にファイルが投げ込まれた時や、エクスプローラ上でゴミ箱を空にした時に発生し、起動中の全ゴーストに通知される。<br />
また、ゴースト起動時に*\[NOTIFY\]*で通知される。

- **Reference0**: 現在ゴミ箱に入っているファイルの数
- **Reference1**: 現在ゴミ箱に入っているファイルのサイズ 単位バイト
- **Reference2**: 現在ゴミ箱に入っているファイルの数の直前との差
- **Reference3**: 現在ゴミ箱に入っているファイルのサイズの直前との差 単位バイト
- **Reference4**: 常に1 (OnRecycleBinEmptyとの互換用のダミー)
- **Reference5**: 常に空 (OnRecycleBinEmptyとの互換用のダミー)

**対応:** SSP 2.6.04/Ref4は2.6.35
