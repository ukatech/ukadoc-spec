# OnDesktopWallpaperChange

**カテゴリ:** OS状态事件

OS侧桌面壁纸发生更改时触发。*\[启动时NOTIFY/其他GET\]*<br />
除用户在个性化设置等位置更改壁纸外，幻灯片放映、Windows 聚焦自动更换壁纸以及切换主题时也会触发。<br />
幻灯片放映和聚焦最短每隔1分钟自动切换一次，因此由这两者触发时，即使在启动后也会通过NOTIFY(无法说话)通知。<br />
这是一个不同于通过图像文件DnD更改壁纸时触发的[OnWallpaperChange](../file-drop/OnWallpaperChange.md)的事件；SSP 自身更改壁纸时(Reference1为self)，两个事件都会触发。如果同时响应这两个事件，请注意避免重复处理。<br />
在[窗口模式](OnWindowModeChange.md)下，对于ghost而言，壁纸就是容器背景。OS侧更改壁纸时，只有容器背景为「桌面」才会触发；背景为白色、灰色、黑色或图像时不会触发。作为替代，在容器背景切换时(容器菜单、[`\![set,wallpaper]`](../../sakura-script/event/bang-set-wallpaper.md)、[`\![restore,wallpaper]`](../../sakura-script/event/bang-restore-wallpaper.md))，以及窗口模式切换导致ghost可见的背景发生变化时，会触发此事件。仅重新选择相同背景时不会触发。<br />
在perghost(每个ghost各有一个容器)模式下，只有自身所在容器的背景发生变化时才会触发。

- **Reference0**: init (启动时通知) 或 update (启动后的更改)
- **Reference1**: 更改的原因。<br />
  user：用户更改<br />
  slideshow：幻灯片放映自动切换<br />
  spotlight：Windows 聚焦自动更新<br />
  theme：随主题切换而更改<br />
  self：SSP自身更改(通过图像DnD更改或从配置文件恢复)<br />
  unknown：确定发生了更改，但无法判断原因<br />
  在窗口模式下，通过容器菜单或切换窗口模式导致的更改为user，通过`\![set,wallpaper]`・`\![restore,wallpaper]`导致的更改为self。启动时通知(init)时，如果容器背景不是「桌面」，则为unknown。
- **Reference2**: 当前壁纸图像的完整路径。纯色背景或无法获取时为空。<br />
  由于Windows的规格，返回的路径可能不是用户选择的原始图像文件，而是OS创建的缓存(TranscodedWallpaper或聚焦缓存)的路径。<br />
  在窗口模式下，容器背景为「桌面」时返回OS侧壁纸的路径；为图像时返回该图像的完整路径；为白色、灰色、黑色或未指定图像的纯色时为空。
- **Reference3**: 上一张壁纸图像的完整路径。Reference0为init时为空。
- **Reference4**: 显示样式。取值为center / tile / stretch / fit / fill / span之一。<br />
  在窗口模式下，容器背景为图像时也可能为stretch-x / stretch-y。为白色、灰色或黑色时为center。
- **Reference5**: 桌面背景色。显示在壁纸留白处的颜色。以半角逗号分隔的R,G,B。<br />
  在窗口模式下，容器背景为图像时为其底色(若指定了颜色则为该颜色，否则为根据图像计算出的颜色)；为白色、灰色或黑色时为对应颜色。
- **Reference6～**: 后续按以下格式附加与显示器数量相同的各显示器壁纸信息。\[`\1`\]是字节值1。<br />
  显示器编号\[`\1`\]壁纸图像的完整路径\[`\1`\]显示样式<br />
  显示器编号的顺序与[OnDisplayChangeEx](OnDisplayChangeEx.md)的Reference1～相对应(Reference1为显示器编号0)。<br />
  OS不会为每台显示器分别保存显示样式，因此目前所有值都相同(与Reference4相同)。<br />
  在无法处理各显示器壁纸的环境(Windows 7及更早版本)中，不会附加Reference6及之后的内容。<br />
  在窗口模式下，无论容器背景类型如何，都只会附加一条记录，并将容器作为一个屏幕(显示器编号0)。

**対応:** SSP 2.8.86
