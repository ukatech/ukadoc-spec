# OnSessionReconnect

**カテゴリ:** OS状態イベント

簡易ユーザー切り替えで実行中のユーザーアカウントに戻ってきた時に発生する。<br />
Windows上ではOnSessionUnlockとセットで通知され、さらに強制最小化されたのが解除されるためOnWindowStateRestoreも発生する。<br />
この挙動はWindows特有の制約であり、他のOS上で同様の動きになるとは限らない点に注意。

**対応:** SSP 2.5.53
