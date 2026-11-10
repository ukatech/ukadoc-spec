# balloons\*s.txt/balloonk\*s.txt

## 概要

balloon 的各个 surface（balloons0.png、balloonk0.png、……）以及输入框的单独设置文件。<br />
以 descript.txt 中的设置作为默认设置；如果在此文件中设置相同项目，则仅覆盖已设置的项目。

每个 surface 可以准备一个文件（例如，为 balloons0.png 准备 balloons0s.txt。请注意文件名末尾的 s）。

原则上可以设置所有项目，但与整个 balloon 相关的设置 name、type、craftman、craftmanurl、id、homeurl、readme 不可设置（没有意义）。<br />
此外，还添加了用于调整 shell 侧 surface 显示位置的设置 windowposition.x 和 windowposition.y（仅 SSP 也可在 descript.txt 中设置）。

对于多行输入框 balloonc5.png（SSP 2.9.10），balloonc5s.txt 中的 communicatebox.x/y/width/height 范围包含输入框及其下方的按钮行。<br />
此范围不会继承 descript.txt 中的值（适用于单行输入框）。如果未在 balloonc5s.txt 中指定，则范围为距图像四边 8 像素的内部区域。<br />
文字大小遵循 balloonc5s.txt 中的 font.height（省略时使用 descript.txt 中的 font.height），字体和颜色遵循 communicatebox.font.name/font.color/background.color。

**対応:** Materia / SSP / CROW
