# `\m[umsg,wparam,lparam]`

**カテゴリ:** 未分類コマンド

SSTP専用。<br />
Wndヘッダにより予めセットされたウインドウハンドルに対し<br />
postmessage(hwnd,umsg,wparam,lparam) を実行する。

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
SSTP経由でこのスクリプトを再生すると、再生したゴーストが終了する。\m[WM_CLOSE,0,0]
```
