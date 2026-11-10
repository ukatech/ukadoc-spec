# OnVanishButtonHold

**カテゴリ:** Vanish event

Occurs when a vanish event is canceled by double-clicking during the event.

- **Reference0**: Script where the interrupting action occurred.
- **Reference1**: Scope number of the balloon where the interrupting action occurred. Main character side is 0, partner side is 1, and subsequent scopes follow.
- **Reference2**: Position of the interruption, expressed as the number of characters from the start of the script. Sakura Script tags are included in the character count.<br />
  Example: If interruption occurs at the 「あ」 in `\s[2]`あいうえお, the value is 6

**対応:** Materia / SSP / CROW / Ninix
