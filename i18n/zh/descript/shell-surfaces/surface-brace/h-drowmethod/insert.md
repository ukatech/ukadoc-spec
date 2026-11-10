# insert,ID

**カテゴリ:** surface花括号 \> 绘制方法

在指定位置插入指定 ID（animation\* 中 \* 所代表的编号）的 dressup 组（interval 为 bind 的动画）。<br />
这是为 dressup 准备的方法，用于非 dressup 动画或 element 时未定义。<br />
例如，当某个 dressup A 与其他 dressup B 的位置关系结构为部分在前、部分在后时，可以通过 insert 将 dressup B 插入 dressup A 中位于后方的帧和位于前方的帧之间，从而自然地显示前后关系。此时，无论 dressup B 处于显示还是隐藏状态，都能保持显示的完整性。<br />
也可以在 insert 目标中继续使用 insert（嵌套）。<br />
但这仅仅是*预留 dressup A 和 B 的显示顺序*，并不会强制显示 dressup B。<br />
是否实际显示 dressup B，取决于 dressup B 的启用/禁用状态。

**対応:** Materia / SSP
