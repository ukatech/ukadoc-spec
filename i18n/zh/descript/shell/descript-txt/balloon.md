# balloon,balloon名称

**カテゴリ:** descript.txt

此shell的默认balloon名称。切换到此shell时，它是候选balloon之一。<br />
切换目标balloon按以下顺序确定，越靠上优先级越高。

1. 如果用户在使用此shell期间曾切换过balloon，则使用该balloon
2. ghost侧的[recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md)（推荐balloon）
3. 此shell的默认balloon（本项）
4. ghost侧的[balloon](../../ghost/recommended-balloon/balloon.md)（默认balloon）

如果均未指定，切换shell时balloon不会改变。<br />
如果按第2～4项确定的balloon与当前使用的balloon不同，则切换到该balloon。<br />
第1项的历史记录按shell分别保存。除了通过菜单等方式切换，使用 `\![change,balloon,...]` 切换也会计入历史记录。仅因遵循默认或推荐设置而自动切换不会计入历史记录，重新加载balloon或重置设置也不会增加历史记录（重置设置会清除历史记录）。<br />
如果指定了多个，则使用最先找到的balloon（先处理[default.balloon.path](default.balloon.path.md)的指定）。

**既定値:** ghost的descript设置

**対応:** SSP
