# Windows 上 SSP 的 XInput 特有规格

Windows 上的 SSP 使用 XInput API 获取游戏手柄输入。因此存在以下限制。

- **支持的控制器**: 仅支持 XInput 游戏手柄（如 Xbox 系列控制器）。仅支持 DirectInput 的控制器无法识别。
- **同时连接数**: 最多4台。手柄索引范围为0～3。
- **OnGamepadAxisMove 的 Reference2（原始值）范围**: 摇杆为-32768～32767，扳机为0～255。
