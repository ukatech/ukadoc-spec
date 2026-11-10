# OnWindowModeChange

**カテゴリ:** OS 状态事件

SSP的窗口模式切换时发生。*\[启动时NOTIFY/其他情况GET\]*<br />
窗口模式是指不将ghost显示在桌面上，而是显示在SSP提供的窗口（容器）中的模式。容器内部就是ghost的屏幕。<br />
由于切换会改变ghost屏幕的大小，因此此事件之后也会发生[OnDisplayChange](OnDisplayChange.md)。<br />
当前模式也可以通过[baseware.windowmode](../../propertysystem/property-system/baseware.windowmode.md)获取。

- **Reference0**: init（启动时通知）或 update（启动后的切换）
- **Reference1**: 当前模式。<br />
  normal：普通模式（将ghost显示在桌面上）<br />
  shared：窗口模式。所有ghost共用一个容器<br />
  perghost：窗口模式。每个ghost使用一个容器
- **Reference2**: 上一个模式。值的种类与Reference1相同。如果Reference0为init，则为空。

**対応:** SSP 2.8.93
