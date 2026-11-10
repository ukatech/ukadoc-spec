# OnSpectrePlugin.Possession

**カテゴリ:** plugin「Spectre」

Spectre 透過此 ghost 顯示對話 15 秒後發生。<br />
請注意，此事件並非由 plugin 本身直接發出，而是由 ghost 透過放在對話末尾的 timerraise 標籤呼叫。

- **Reference0**: 根據目前對話池判定的角色目前「情緒」。值為下列其中之一。
  - dissociated …… 極度悲傷、思緒混亂的情緒
  - miserable …… 悲傷或憤怒的情緒
  - cheerful …… 快樂或放鬆的情緒
- **Reference1**: 播放的 script 是否為「spooky text」script。「spooky text」script 是指具有引發不安感之特殊文字效果的 script 等。若符合則為 1，否則為 0。<br />
  目前只有在 Reference0 為「dissociated」的情境下，才會播放「spooky text」script。
