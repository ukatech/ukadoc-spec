# balloon,balloon 名称

**カテゴリ:** descript.txt

此 shell 的标准 balloon 名称。切换到此 shell 时，它是可选用的 balloon 之一。<br />
切换目标 balloon 按以下顺序决定，靠前的项目优先。

1. 如果用户在使用此 shell 期间切换过 balloon，则使用该 balloon
2. ghost 侧的 [recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md)（推荐 balloon）
3. 此 shell 的标准 balloon（本项）
4. ghost 侧的 [balloon](../../ghost/recommended-balloon/balloon.md)（标准 balloon）

如果均未指定，切换 shell 时 balloon 不会改变。<br />
如果第 2～4 项决定的 balloon 与当前使用的 balloon 不同，则切换到该 balloon。<br />
第 1 项的历史记录按 shell 分别保存。除通过菜单等切换外，通过 `\![change,balloon,...]` 切换也会记录在历史中。仅因遵循标准或推荐设置而自动切换不会产生历史记录，重新加载 balloon 或重置设置也不会增加历史记录（重置设置会清除历史记录）。<br />
如果填写了多个，则使用第一个找到的 balloon（[default.balloon.path](default.balloon.path.md) 的指定优先）。

**既定値:** ghost 的 descript 设置

**対応:** SSP
