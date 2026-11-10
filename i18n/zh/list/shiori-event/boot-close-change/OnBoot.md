# OnBoot

**カテゴリ:** 启动、关闭和切换事件

启动时触发。<br />
在 SSP 中，如果对 [OnGhostChanged](OnGhostChanged.md)、[OnGhostCalled](OnGhostCalled.md)、[OnFirstBoot](OnFirstBoot.md)、[OnVanished](../vanish/OnVanished.md) 没有返回脚本（204），则接着触发此事件。

- **Reference0**: 启动时的 shell 名称。
- **Reference6**: ※仅限 MATERIA、SSP　上次处理中崩溃时为 halt。
- **Reference7**: ※仅限 MATERIA、SSP　上次处理中崩溃的 ghost 名称。

**対応:** Materia / SSP / CROW / Ninix
