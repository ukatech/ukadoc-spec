# OnHydrateStatsNotify

**カテゴリ:** ゴースト「Hydrate」

Hydrateの現在の状態と、ユーザーの水分補給の統計を通知する。

- **Reference0**: Hydrateが現在使っているシェルの名前。
- **Reference1**: 現在のドレスアップの一覧。2次元配列で、ドレスアップ同士は0xFDEFで、各ドレスアップのカテゴリ名とパーツ名は0x01で区切る。（例: "Glass shape\[0x01\]Tall\[0xFDEF\]Drink\[0x01\]Tea"）
- **Reference2**: シェルの現在のX方向の拡大率（パーセント）。
- **Reference3**: シェルの現在のY方向の拡大率（パーセント）。
- **Reference4**: 今日飲んだ回数。
- **Reference5**: 飲んだ回数の合計。
- **Reference6**: 現在の連続記録（連続して飲んだ回数）。
- **Reference7**: これまでの最高の連続記録（連続して飲んだ回数）。
- **Reference8**: 今日取った追加の一口の回数。
- **Reference9**: 追加の一口の合計回数。
- **Reference10**: Hydrateが最小化されているかどうか。最小化されていれば1、そうでなければ0。
