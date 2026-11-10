# 补充

## 形状指定の方法

- **square**: 显示矩形。
- **underline**: 显示下划线。
- **square+underline**: 显示矩形和下划线。
- **none**: 不显示。
- **default**: 恢复为 balloon 设置的默认值。

## 文字色指定の方法

基本上与 HTML、CSS 中的颜色表示方式类似。<br />
\[2.8.93\] 不符合以下任一格式的值（例如非数值的 R、G、B，或包含非十六进制字符的颜色代码）将被忽略。以前有时会将其视为黑色。

- **R,G,B**: 分别以 0～255 的十进制数表示红、绿、蓝三原色的亮度，并用逗号分隔。<br />
  0,0,0 表示黑色，255,255,255 表示白色。
- **R%,G%,B%**: 分别以 0～100% 的百分比表示红、绿、蓝三原色的亮度，并用逗号分隔。<br />
  0%,0%,0% 表示黑色，100%,100%,100% 表示白色。
- **16進数カラーコード**: 如 #07f，将红、绿、蓝三原色的亮度分别以*十六进制*表示，在前面加上「#」后连接起来。<br />
  可以用红、绿、蓝各两位、共 6 位表示，也可以各一位、共 3 位表示。<br />
  十六进制字母可以使用大写或小写。<br />
  #000000 或 #000 表示黑色，#ffffff 或 #fff 表示白色。
- **定義済みキーワード**: 可以使用 red、white、black 等表示颜色名称的关键字（全部小写）。<br />
  对于所谓的 X11 color 与 W3C color 中定义不同的颜色（如 green、gray 等），采用 W3C color 的定义。<br />
  颜色示例：[CSS Color Module Level 3 Extended color keywords](http://www.w3.org/TR/css3-color/#svg-color)（外部链接）
- **default**: 在颜色指定部分写入 default，可将指定文字恢复为该文字的默认颜色。<br />
  默认颜色为 balloon 的 descript.txt 中定义的颜色等（未定义时为黑色）。
- **disable**: 在颜色指定部分写入 disable，可将颜色设为禁用显示用的颜色。
- **default.anchor**: 在颜色指定部分指定 default.anchor，可将指定文字的颜色更改为选中时锚点的默认文字颜色。<br />
  \[2.5.76 - 可用于普通字符串\]
- **default.anchornotselect**: 在颜色指定部分指定 default.anchornotselect，可将指定文字的颜色更改为未选中时锚点的默认文字颜色。<br />
  \[2.5.76 - 可用于普通字符串\]
- **default.anchorvisited**: 在颜色指定部分指定 default.anchorvisited，可将指定文字的颜色更改为已访问锚点的默认文字颜色。<br />
  \[2.5.76 - 可用于普通字符串\]
- **default.cursor**: *※仅可用于选项和锚点的文字颜色*。<br />
  在颜色指定部分指定 default.cursor，可将指定文字的颜色更改为选中时选项的默认文字颜色。
- **default.cursornotselect**: *※仅可用于选项和锚点的文字颜色*。<br />
  在颜色指定部分指定 default.anchor，可将指定文字的颜色更改为未选中时选项的默认文字颜色。
- **default.plain**: *※仅可用于选项和锚点的文字颜色*。<br />
  在颜色指定部分指定 default.plain，可将指定文字的颜色更改为普通文本的默认文字颜色。
