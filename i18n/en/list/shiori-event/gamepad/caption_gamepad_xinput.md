# XInput-specific behavior of SSP on Windows

SSP on Windows uses the XInput API to obtain gamepad input. This imposes the following restrictions.

- **Supported controllers**: XInput-compatible gamepads only (such as Xbox controllers). Controllers that support only DirectInput are not recognized.
- **Maximum simultaneous connections**: 4. Pad indices range from 0 to 3.
- **Range of OnGamepadAxisMove Reference2 (raw value)**: Sticks: -32768 to 32767; triggers: 0 to 255.
