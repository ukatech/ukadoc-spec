# currentghost.seriko.sticky-window

**カテゴリ:** 属性系统

当前[`\![set,sticky-window,～]`](../../sakura-script/surface/bang-set-sticky-window-ID-ID.md)的设置状态。<br />
组内的 scope ID 以逗号分隔，不同组之间以分号分隔。<br />
例如，将 scope 0 和 1、scope 2 和 3 分别组合在一起时，值为 `0,1;2,3`。<br />
没有任何设置时，值为空。<br />
*\[SET有效\]*

写入时，使用相同格式**完全替换当前设置**。请注意，这与 Sakura Script 标签逐步添加组的行为不同。<br />
写入空字符串会解除所有组合设置。<br />
元素少于2个的组，以及包含已在其他组中使用的 scope ID 的组，都会被忽略。

**対応:** SSP 2.8.78
