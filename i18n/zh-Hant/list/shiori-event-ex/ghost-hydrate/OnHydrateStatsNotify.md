# OnHydrateStatsNotify

**カテゴリ:** ghost「Hydrate」

通知 Hydrate 的目前狀態及使用者的水分補充統計資訊。

- **Reference0**: Hydrate 目前使用的 shell 名稱。
- **Reference1**: 目前的 dressup 清單。這是二維陣列，各 dressup 以0xFDEF分隔，每個 dressup 的類別名稱和部件名稱以0x01分隔。（例如: "Glass shape\[0x01\]Tall\[0xFDEF\]Drink\[0x01\]Tea"）
- **Reference2**: shell 目前的 X 方向縮放比例（百分比）。
- **Reference3**: shell 目前的 Y 方向縮放比例（百分比）。
- **Reference4**: 今天喝水的次數。
- **Reference5**: 喝水的總次數。
- **Reference6**: 目前的連續紀錄（連續喝水的次數）。
- **Reference7**: 歷來最高的連續紀錄（連續喝水的次數）。
- **Reference8**: 今天額外喝的一口水的次數。
- **Reference9**: 額外喝的一口水的總次數。
- **Reference10**: Hydrate 是否最小化。最小化時為1，否則為0。
