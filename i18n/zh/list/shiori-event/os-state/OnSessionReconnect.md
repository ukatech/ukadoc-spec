# OnSessionReconnect

**カテゴリ:** OS 状态事件

通过快速用户切换返回正在运行的用户帐户时发生。<br />
在Windows上会与OnSessionUnlock一起通知，并且由于强制最小化状态被解除，也会发生OnWindowStateRestore。<br />
请注意，这是Windows特有的限制，在其他OS上不一定会有相同的行为。

**対応:** SSP 2.5.53
