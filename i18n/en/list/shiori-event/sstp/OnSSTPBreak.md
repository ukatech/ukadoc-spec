# OnSSTPBreak

**カテゴリ:** SSTP events

Occurs when SSTP is interrupted.

- **Reference0**: Script in which the interruption occurred.
- **Reference1**: Scope number of the balloon where the interruption occurred. 0 for the main character, 1 for the partner, and higher numbers for others.
- **Reference2**: Position of the interruption. Expressed as the number of characters from the start of the script. Sakura Script tags are included in the character count.<br />
  Example: If the script is interrupted at the 「あ」 in `\s[2]`あいうえお, the value is 6.

**対応:** Materia / SSP
