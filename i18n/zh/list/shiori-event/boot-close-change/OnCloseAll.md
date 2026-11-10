# OnCloseAll

**カテゴリ:** 启动、关闭和切换事件

SSP 本身关闭时触发。<br />
除通过 owner draw 菜单指示「全部关闭」的情况外，当唯一正在运行的 ghost 收到「关闭」指示，以及因操作系统关机而导致 SSP 关闭时，也会触发此事件。

- **Reference0**: ※仅限 SSP　关闭原因。<br />
  用户关闭时，返回 user<br />
  关机时，返回 system。
- **Reference1**: ※仅限 SSP　执行关闭操作的菜单所属角色的 scope 编号。受 popupmenu.type 影响。（主角色为 0、搭档为 1……）
- **Reference2**: ※仅限 SSP　执行关闭操作的窗口角色的 scope 编号。不受 popupmenu.type 影响。（主角色为 0、搭档为 1……）

**対応:** SSP / Ninix
