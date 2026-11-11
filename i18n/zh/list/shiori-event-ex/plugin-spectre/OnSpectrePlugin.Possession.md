# OnSpectrePlugin.Possession

**カテゴリ:** plugin“Spectre”

Spectre通过此ghost显示对话15秒后发生。<br />
注意，此事件并非由plugin本身直接触发，而是通过放在对话末尾的timerraise标签从ghost侧调用。

- **Reference0**: 根据当前对话池确定的角色当前“情绪”。取以下值之一。
  - dissociated …… 非常悲伤且语无伦次的情绪
  - miserable …… 悲伤或愤怒的情绪
  - cheerful …… 愉快或放松的情绪
- **Reference1**: 播放的脚本是否为“spooky text”脚本。“spooky text”脚本例如具有唤起不安感的特殊文字效果的脚本。是则为1，否则为0。<br />
  目前“spooky text”脚本仅在Reference0为“dissociated”的情况下播放。
