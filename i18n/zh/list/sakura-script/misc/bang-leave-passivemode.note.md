# PassiveMode

处于被动模式时，会施加以下限制。<br />
这些限制针对用户操作；通过 Sakura Script 执行时仍可进行相应操作。

- 可在 owner draw 菜单中选择的项目受到限制。
- 不检查邮件。
- 不运行 headline sensor。
- 不自动切换。
- 不会中断脚本。
- 选项不会超时。
- 气泡不会随时间经过而消失。
- 忽略拖放到窗口中的文件。
- 忽略双击 nar 文件进行安装（SSP 中仍会安装，但 ghost 不会收到事件）。
- 不会收到 OnSurfaceRestore。
- cantalk 始终为 false。（仍会收到 OnSecondChange 和 OnMinuteChange 事件本身）
- 无法切换 ghost。
- （仅限 Materia：）Communicate 框会关闭，且无法再次打开。
- 无法最小化。
- 无法退出。
- 无法进行 network update。
- 无法卸载。
