# OnHydrateStatsNotify

**カテゴリ:** ghost「Hydrate」

通知 Hydrate 当前的状态以及用户的水分摄入统计。

- **Reference0**: Hydrate 当前使用的 shell 名称。
- **Reference1**: 当前 dressup 列表。为二维数组，dressup 项之间用 0xFDEF 分隔，每个 dressup 的类别名称和部件名称用 0x01 分隔。（例: "Glass shape\[0x01\]Tall\[0xFDEF\]Drink\[0x01\]Tea"）
- **Reference2**: shell 当前 X 方向的缩放率（百分比）。
- **Reference3**: shell 当前 Y 方向的缩放率（百分比）。
- **Reference4**: 今天饮水的次数。
- **Reference5**: 饮水次数总计。
- **Reference6**: 当前连续记录（连续饮水的次数）。
- **Reference7**: 迄今为止的最高连续记录（连续饮水的次数）。
- **Reference8**: 今天额外喝一口的次数。
- **Reference9**: 额外喝一口的总次数。
- **Reference10**: Hydrate 是否处于最小化状态。最小化时为 1，否则为 0。
