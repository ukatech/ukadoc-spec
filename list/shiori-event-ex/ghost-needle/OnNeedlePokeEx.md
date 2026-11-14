# OnNeedlePokeEx

**カテゴリ:** ゴースト「Needle」

Needleが他のゴーストを（重なることで）「つつく」ときに発生する。[OnNeedlePoke](OnNeedlePoke.md)より前に発生する。OnNeedlePokeの複数スコープ版のイベントで、高度な処理に使える。

- **Reference0**: つつかれたすべてのスコープのIDをカンマで区切った配列。メインキャラクターは0、サイドキャラクターは1、追加のキャラクターは2以降。
- **Reference1**: Needleが現在使っているシェルの名前。
- **Reference2**: 現在のドレスアップの一覧。2次元配列で、ドレスアップ同士は0xFDEFで、各ドレスアップのカテゴリ名とパーツ名は0x01で区切る。（例: "Color\[0x01\]Gray\[0xFDEF\]Bow\[0x01\]Pink"）
