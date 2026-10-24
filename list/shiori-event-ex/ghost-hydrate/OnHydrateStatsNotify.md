# OnHydrateStatsNotify

**カテゴリ:** ゴースト「Hydrate」

Notifies information about Hydrate's current state and the user's hydration stats.

- **Reference0**: The name of the shell Hydrate is currently using.
- **Reference1**: A list of the current dressups. This is a 2-dimensional array, where each dressup is delimited by 0xFDEF, and the category and part name of each dressup is delimited by 0x01. (Example: "Glass shape\[0x01\]Tall\[0xFDEF\]Drink\[0x01\]Tea")
- **Reference2**: The current X scaling of the shell (as a percentage).
- **Reference3**: The current Y scaling of the shell (as a percentage).
- **Reference4**: The number of drinks today.
- **Reference5**: The number of drinks in total.
- **Reference6**: The current drink streak (number of drinks in a row).
- **Reference7**: The highest ever drink streak (number of drinks in a row).
- **Reference8**: The number of extra sips taken today.
- **Reference9**: The number of extra sips in total.
- **Reference10**: Whether Hydrate is minimized or not. 1 if true, 0 otherwise.
