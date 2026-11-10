# OnHydrateStatsNotify

**カテゴリ:** Ghost “Hydrate”

Notifies the current state of Hydrate and the user's hydration statistics.

- **Reference0**: Name of the shell currently used by Hydrate.
- **Reference1**: List of current dressups. This is a two-dimensional array, with dressups separated by 0xFDEF and each dressup's category name and part name separated by 0x01. (Example: "Glass shape\[0x01\]Tall\[0xFDEF\]Drink\[0x01\]Tea")
- **Reference2**: Current X-axis scale of the shell (percent).
- **Reference3**: Current Y-axis scale of the shell (percent).
- **Reference4**: Number of drinks today.
- **Reference5**: Total number of drinks.
- **Reference6**: Current streak (number of consecutive drinks).
- **Reference7**: Longest streak so far (number of consecutive drinks).
- **Reference8**: Number of extra sips today.
- **Reference9**: Total number of extra sips.
- **Reference10**: Whether Hydrate is minimized. 1 if minimized, otherwise 0.
