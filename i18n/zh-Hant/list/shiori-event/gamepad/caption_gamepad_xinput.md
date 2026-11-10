# Windows 上 SSP 的 XInput 特定規格

Windows 上的 SSP 使用 XInput API 取得遊戲手把輸入。因此有以下限制。

- **支援的控制器**: 僅支援 XInput 相容的遊戲手把（例如 Xbox 系列控制器）。無法辨識僅支援 DirectInput 的控制器。
- **同時連線數**: 最多 4 台。手把索引範圍為 0～3。
- **OnGamepadAxisMove 的 Reference2（原始值）範圍**: 搖桿為 -32768～32767，扳機為 0～255。
