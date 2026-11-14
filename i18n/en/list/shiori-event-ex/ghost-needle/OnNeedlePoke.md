# OnNeedlePoke

**カテゴリ:** Ghost “Needle”

Occurs when Needle "pokes" another ghost (by overlapping them). If Needle is overlapping multiple scopes simultaneously, the event will be sent once for each scope.

- **Reference0**: The ID of the scope that was poked. 0 for the main character, 1 for the side character, 2 and onwards for additional characters.
- **Reference1**: The name of the shell Needle is currently using.
- **Reference2**: A list of the current dressups. This is a 2-dimensional array, where each dressup is delimited by 0xFDEF, and the category and part name of each dressup is delimited by 0x01. (Example: "Color\[0x01\]Gray\[0xFDEF\]Bow\[0x01\]Pink")
