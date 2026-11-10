# OnGhostChanging

**カテゴリ:** 启动、关闭和切换事件

收到切换到其他 ghost 的指示时触发。<br />
在 SSP 中，如果对此事件没有返回脚本（204），则接着触发 [OnClose](OnClose.md)。

- **Reference0**: 要切换到的 ghost 的主角色名称。
- **Reference1**: 手动切换时返回 manual<br />
  由系统切换时返回 automatic<br />
  。
- **Reference2**: 要切换到的 ghost 的名称。\[仅限 SSP\]
- **Reference3**: 要切换到的 ghost 的路径。\[仅限 SSP\]

**対応:** Materia / SSP / CROW / Ninix
