# OnNeedlePokeEx

**カテゴリ:** Ghost “Needle”

Occurs when Needle "pokes" another ghost (by overlapping them). Occurs before [OnNeedlePoke](OnNeedlePoke.md), and is a multi-scope version of that event which can be used for advanced processing.

- **Reference0**: A comma-separated array of the IDs of all scopes that were poked. 0 for the main character, 1 for the side character, 2 and onwards for additional characters.
- **Reference1**: The name of the shell Needle is currently using.
- **Reference2**: A list of the current dressups. This is a 2-dimensional array, where each dressup is delimited by 0xFDEF, and the category and part name of each dressup is delimited by 0x01. (Example: "Color\[0x01\]Gray\[0xFDEF\]Bow\[0x01\]Pink")
