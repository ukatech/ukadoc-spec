# OnBalloonBreak

**カテゴリ:** Balloon event

Occurs when the balloon is interrupted by something other than SSTP.

- **Reference0**: The script that was interrupted.
- **Reference1**: The scope number of the balloon where the interruption occurred. 0 for the main character, 1 for the partner, and so on.
- **Reference2**: The interruption position, expressed as the number of characters from the start of the script. Sakura Script tags are included in the character count.<br />
  Example: If interrupted at the 「あ」 in `\s[2]`あいうえお, the value is 6

**対応:** SSP / Ninix
