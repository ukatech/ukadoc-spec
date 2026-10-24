# OnSessionDisconnect

**カテゴリ:** OS状態イベント

簡易ユーザー切り替えで他のユーザーアカウントへの切り替え操作を行った時に発生する。<br />
Windows上ではOnSessionLockとセットで通知され、さらに強制最小化されるためOnWindowStateMinimizeも発生する。<br />
この挙動はWindows特有の制約であり、他のOS上で同様の動きになるとは限らない点に注意。

**対応:** SSP 2.5.53
