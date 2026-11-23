# nocontextmenu\*,碰撞区域名

**カテゴリ:** collisionoption块

在指定的碰撞区域上按下右键时，不显示鼠标右键上下文菜单（本体的菜单）。<br />
\*部分是在同一scope的nocontextmenu定义中不重复的编号。<br />
碰撞区域名是在collision定义中设置的名称。不区分大小写。

由于会妨碍用户操作，请勿滥用。请在cursor块中指定能向用户表明无法操作的光标。

- 是否显示菜单由按下右键位置的碰撞区域决定。
- 仅针对鼠标右键。键盘的菜单键、Shift+F10、任务栏托盘菜单仍正常显示。
- 右键的OnMouseDown、OnMouseUp、OnMouseClick和鼠标手势仍正常触发。

**既定値:** 未指定（显示上下文菜单）

**対応:** SSP 2.9.38
