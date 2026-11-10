# OnSessionReconnect

**カテゴリ:** OS 狀態事件

透過快速使用者切換返回目前正在執行的使用者帳戶時發生。<br />
在 Windows 上會與 OnSessionUnlock 一起通知，並且會解除先前強制最小化的狀態，因此也會發生 OnWindowStateRestore。<br />
請注意，這是 Windows 特有的限制，在其他 OS 上不一定會有相同的行為。

**対応:** SSP 2.5.53
