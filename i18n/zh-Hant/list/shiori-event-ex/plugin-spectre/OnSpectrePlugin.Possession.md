# OnSpectrePlugin.Possession

**カテゴリ:** plugin「Spectre」

Spectre 透過此 ghost 顯示對話後15秒發生。<br />
注意，此事件並非由 plugin 本身直接發出，而是透過置於對話末尾的 timerraise 標籤從 ghost 端呼叫。

- **Reference0**: 根據目前對話集決定的角色目前「心情」。值為以下其中之一。
  - dissociated …… 非常悲傷且思緒混亂的心情
  - miserable …… 悲傷或憤怒的心情
  - cheerful …… 快樂或放鬆的心情
- **Reference1**: 播放的腳本是否為「spooky text」腳本。「spooky text」腳本例如具有特殊文字效果以引發不安感的腳本。符合時為1，否則為0。<br />
  目前「spooky text」腳本只會在 Reference0 為「dissociated」的情況下播放。
