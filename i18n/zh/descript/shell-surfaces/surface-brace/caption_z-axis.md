# 各要素的上下层级

## 上层与下层

以下将屏幕前方称为上层，将屏幕后方称为下层。

## 各部件的上下层级

在element和dressup（间隔为bind的动画）中，elementID・patternID较小的一方位于下层，较大的一方位于上层。

## 基础surface与各动画的上下层级

基础surface基本上是所有合成图像中位于最底层的图像，但指定了SSP的[background选项](animation-star-.option-2.md)的动画会合成在基础surface的下层（背面）。

包括dressup在内的各动画之间的上下层级通常按动画ID从大到小依次位于上层（编号较大的动画放置在屏幕前方）。但在SSP中，可以通过在descript大括号中定义[animation-sort](../descript-brace/animation-sort.md)，改为升序排列。

## 碰撞判定（collision）的上下层级

某个surface的碰撞判定中，基本上在surfaces.txt里先出现的collision定义位于上层。但在SSP中，可以通过在descript大括号中定义[collision-sort](../descript-brace/collision-sort.md)，按collisionID设置为升序或降序排列。

此外，在SSP中，可以通过设置[animation\*.collision](animation-star-.collision-star.md)，使碰撞判定仅在特定动画显示时有效。此时，会先考虑各动画的上下层级，再按通常顺序分别评估动画和基础surface的碰撞判定。

以animation-sort设置为descend为例，从上层到下层依次如下：

1. ID较大的普通动画中，较上层的碰撞判定
2. ID较大的普通动画中，较下层的碰撞判定
3. ID较小的普通动画中，较上层的碰撞判定
4. ID较小的普通动画中，较下层的碰撞判定
5. 基础surface中，较上层的碰撞判定
6. 基础surface中，较下层的碰撞判定
7. 带有background选项且ID较大的动画中，较上层的碰撞判定
8. 带有background选项且ID较大的动画中，较下层的碰撞判定
9. 带有background选项且ID较小的动画中，较上层的碰撞判定
10. 带有background选项且ID较小的动画中，较下层的碰撞判定

（这里的动画也包括dressup。）
