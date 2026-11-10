# OnSessionDisconnect

**カテゴリ:** OS state event

Occurs when switching to another user account using Fast User Switching.<br />
On Windows, this is sent together with OnSessionLock, and the window is also forcibly minimized, causing OnWindowStateMinimize to occur.<br />
Note that this behavior is a Windows-specific constraint; other operating systems may not behave the same way.

**対応:** SSP 2.5.53
