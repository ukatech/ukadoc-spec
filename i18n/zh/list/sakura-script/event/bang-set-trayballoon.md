# `\![set,trayballoon,オプション,オプション,オプション...]`

**カテゴリ:** 事件命令

从托盘图标显示 balloon。<br />
点击 balloon 将触发 OnTrayBalloonClick。<br />
超时或点击关闭按钮关闭时，将触发 OnTrayBalloonTimeout。<br />
可指定以下选项。

在 Windows 10 及更高版本中，如果文件关联设置为「仅快捷方式」或更高（不包括 kiosk 模式和只读模式；更改设置后将在下次启动时生效），则会改为显示 toast 通知，并保留在通知中心中，而不是显示 balloon。此时不会在托盘图标旁显示通知。不满足条件或显示失败时，仍按原方式显示 balloon。<br />
对于 toast 通知，点击时会触发 OnTrayBalloonClick；点击关闭按钮关闭，或超时后通知移至通知中心时，会触发 OnTrayBalloonTimeout。移至通知中心后再点击不会触发事件。\[2.9.14\]

- **--text=文本**: balloon 中显示的字符串；指定多个时分多行显示。（必需）
- **--title=标题**: balloon 的标题。
- **--icon=图标设置名**: balloon 中显示的图标设置。<br />
  对于 toast 通知，图标显示在正文左侧。\[2.9.14\]
- **info**: 信息图标
- **error**: 错误图标
- **warning**: 警告图标
- **none**: 无
- **--timeout=秒数**: balloon 的显示时间（单位＝秒）。只能指定 10～30 秒。Windows 7 及更高版本中会被忽略。toast 通知中也会被忽略。\[2.9.14\]

**対応:** SSP

## 記述例

```sakurascript
\![set,trayballoon,--text=何らかのエラーにより、処理が失敗しました,--title=エラーが発生しました,--icon=error]
```
