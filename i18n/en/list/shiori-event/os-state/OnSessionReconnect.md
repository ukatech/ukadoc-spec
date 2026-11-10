# OnSessionReconnect

**カテゴリ:** OS state event

Occurs when returning to the user account in use after switching users with Fast User Switching.<br />
On Windows, this is sent together with OnSessionUnlock, and the forced minimization is also undone, causing OnWindowStateRestore to occur.<br />
Note that this behavior is a Windows-specific constraint; other operating systems may not behave the same way.

**対応:** SSP 2.5.53
