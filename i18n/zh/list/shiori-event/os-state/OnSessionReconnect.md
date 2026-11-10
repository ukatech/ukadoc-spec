# OnSessionReconnect

**カテゴリ:** OS state event

Occurs when returning to the running user account after using Fast User Switching.<br />
In Windows, it is notified together with OnSessionUnlock, and OnWindowStateRestore also occurs because the forced minimization is undone.<br />
Note that this behavior is a Windows-specific limitation and may not be the same on other operating systems.

**対応:** SSP 2.5.53
