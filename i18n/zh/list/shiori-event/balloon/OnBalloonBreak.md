# OnBalloonBreak

**カテゴリ:** balloon事件

非SSTP方式导致中断时触发。

- **Reference0**: 导致中断的脚本。
- **Reference1**: 被中断的balloon的scope编号。本体侧为0，搭档侧为1，之后依次递增。
- **Reference2**: 中断位置。以从脚本开头起算的字符数表示。字符数包括Sakura Script标签。<br />
  示例）`\s[2]`あいうえお　在「あ」之前中断时，数值为6

**対応:** SSP / Ninix
