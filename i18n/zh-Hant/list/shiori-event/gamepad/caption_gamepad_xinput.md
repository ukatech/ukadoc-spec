# XInput-specific specifications for SSP on Windows

SSP on Windows uses the XInput API to obtain gamepad input. Therefore, it has the following limitations.

- **Supported controllers**: XInput-compatible gamepads only (such as Xbox controllers). DirectInput-only controllers are not recognized.
- **Simultaneous connections**: Up to 4 devices. Pad indices range from 0 to 3.
- **Range of Reference2 (raw value) for OnGamepadAxisMove**: Sticks range from -32768 to 32767; triggers range from 0 to 255.
