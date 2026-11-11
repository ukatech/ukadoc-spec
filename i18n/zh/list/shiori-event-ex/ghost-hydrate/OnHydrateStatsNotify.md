# OnHydrateStatsNotify

**カテゴリ:** ghost“Hydrate”

通知Hydrate的当前状态和用户的饮水统计信息。

- **Reference0**: Hydrate当前使用的shell名称。
- **Reference1**: 当前dressup的列表。这是一个二维数组，dressup之间以0xFDEF分隔，每个dressup的类别名和部件名以0x01分隔。（例："Glass shape\[0x01\]Tall\[0xFDEF\]Drink\[0x01\]Tea"）
- **Reference2**: shell当前的X方向缩放比例（百分比）。
- **Reference3**: shell当前的Y方向缩放比例（百分比）。
- **Reference4**: 今日饮水次数。
- **Reference5**: 饮水总次数。
- **Reference6**: 当前连续饮水记录（连续饮水的次数）。
- **Reference7**: 历史最高连续饮水记录（连续饮水的次数）。
- **Reference8**: 今日额外喝一口的次数。
- **Reference9**: 额外喝一口的总次数。
- **Reference10**: Hydrate是否最小化。最小化时为1，否则为0。
