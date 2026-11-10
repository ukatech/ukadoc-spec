# `\m[umsg,wparam,lparam]`

**カテゴリ:** Uncategorized command

For SSTP only.<br />
Executes<br />
postmessage(hwnd,umsg,wparam,lparam) on the window handle set in advance by the Wnd header.

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
SSTP経由でこのスクリプトを再生すると、再生したゴーストが終了する。\m[WM_CLOSE,0,0]
```
