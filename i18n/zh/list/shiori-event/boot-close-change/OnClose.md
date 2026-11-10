# OnClose

**カテゴリ:** 启动、关闭和切换事件

收到关闭指示时触发。<br />
在 SSP 中，如果对 [OnGhostChanging](OnGhostChanging.md)、[OnCloseAll](OnCloseAll.md) 没有返回脚本（204），则接着触发此事件。

- **Reference0**: ※仅限 SSP　关闭原因。<br />
  用户关闭时，返回 user<br />
  关机时，返回 system。
- **Reference1**: ※仅限 SSP　执行关闭操作的菜单所属角色的 scope 编号。受 popupmenu.type 影响。（主角色为 0、搭档为 1……）
- **Reference2**: ※仅限 SSP　执行关闭操作的窗口角色的 scope 编号。不受 popupmenu.type 影响。（主角色为 0、搭档为 1……）

**対応:** Materia / SSP / CROW / Ninix
