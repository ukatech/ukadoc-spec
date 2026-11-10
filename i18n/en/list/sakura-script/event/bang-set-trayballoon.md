# `\![set,trayballoon,オプション,オプション,オプション...]`

**カテゴリ:** Event command

Displays a balloon from the tray icon.<br />
OnTrayBalloonClick is raised when the balloon is dismissed by clicking it.<br />
OnTrayBalloonTimeout is raised when it times out or is closed using the close button.<br />
The following options can be specified.

On Windows 10 and later, if file association settings are set to "Shortcuts only" or higher (excluding kiosk mode and read-only mode; setting changes take effect from the next startup), a toast notification is shown instead of a balloon and remains in the notification center. In this case, it is not displayed by the tray icon. If the conditions are not met or displaying the toast fails, it is shown as a balloon as before.<br />
For toast notifications, OnTrayBalloonClick is raised when clicked, and OnTrayBalloonTimeout is raised when closed using the close button or when it times out and moves to the notification center. No event is raised if it is clicked after moving to the notification center.\[2.9.14\]

- **--text=テキスト**: Text to display in the balloon; specify multiple values for multiple lines. (Required)
- **--title=タイトル**: Balloon title.
- **--icon=アイコン設定名**: Icon setting to use for the balloon.<br />
  In toast notifications, the icon is displayed to the left of the message.\[2.9.14\]
- **info**: Information icon
- **error**: Error icon
- **warning**: Warning icon
- **none**: None
- **--timeout=秒数**: Balloon display duration (in seconds). Only values from 10 to 30 seconds can be specified. Ignored on Windows 7 and later. Also ignored for toast notifications.\[2.9.14\]

**対応:** SSP

## 記述例

```sakurascript
\![set,trayballoon,--text=何らかのエラーにより、処理が失敗しました,--title=エラーが発生しました,--icon=error]
```
