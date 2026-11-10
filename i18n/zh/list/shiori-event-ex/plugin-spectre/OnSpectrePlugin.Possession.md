# OnSpectrePlugin.Possession

**カテゴリ:** 插件“Spectre”

Spectre通过此ghost显示对话15秒后触发。<br />
请注意，此事件不是由插件本身直接触发，而是由ghost通过放在对话末尾的timerraise标签调用。

- **Reference0**: 根据当前对话池确定的角色当前“情绪”。值为以下之一。
  - dissociated …… 极度悲伤、思绪混乱的情绪
  - miserable …… 悲伤或愤怒的情绪
  - cheerful …… 快乐或放松的情绪
- **Reference1**: 播放的脚本是否为“spooky text”脚本。“spooky text”脚本指带有引发不安感的特殊文字效果等内容的脚本。是则为1，否则为0。<br />
  目前，“spooky text”脚本只会在Reference0为“dissociated”的场景中播放。
