# 基础surface

## 基础surface

每个surface的基本状态，即动画合成前的图像，称为基础surface。

动画通常绘制在基础surface的上层（屏幕前方）。

## 基础surface的实体

某个surface的基础surface由与其ID对应的surface\*.png，以及与其ID对应的surface块中的[element指定](element-star.md)定义。

对于存在surface\*.png的surface，该图像就是surface\*的基础surface。但是，如果同时定义了element0，则surface\*.png的内容会被丢弃，并由element0的定义内容替代（这是为了确保兼容性而规定的行为）。

如果定义了element1及之后的项，这些项会依次叠加合成，最终的合成结果将作为基础surface处理。
