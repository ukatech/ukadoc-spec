# OnBalloonBreak

**カテゴリ:** Balloon event

Occurs when interrupted by something other than SSTP.

- **Reference0**: Script that was interrupted.
- **Reference1**: Scope number of the balloon where the interruption occurred. The main character is 0, the partner is 1, and so on.
- **Reference2**: Interruption position, expressed as the number of characters from the start of the script. Sakura Script tags are included in the character count.<br />
  Example: If interruption occurs at the "あ" in `\s[2]`あいうえお, the value is 6

**対応:** SSP / Ninix
