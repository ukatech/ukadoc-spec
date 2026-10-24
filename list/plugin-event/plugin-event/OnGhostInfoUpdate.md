# OnGhostInfoUpdate

**カテゴリ:** PLUGIN Event

ゴーストの情報が変更されたときに発生。<br />
ロード時にも発生する事がある。*\[NOTIFY\]*

- **Reference0**: バイト値1区切りで、変更があったゴーストの`\0`以降各キャラクターウィンドウのHWND。<br />
  未構築の場合等、0が入る場合がある。
- **Reference1**: 変更があったゴースト名。
- **Reference2**: 変更があったゴーストの現在のシェル名。
- **Reference3**: 変更があったゴーストのID (Owned SSTPで送られるものと同じ）。
- **Reference4**: 変更があったゴーストのフルパス。

**対応:** SSP
