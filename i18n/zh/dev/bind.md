# Dressup settings

## Dressup

A shell for 伺か (Ukagaka) can have *dressups* (for an explanation of dressups themselves, see “[Dressup (MAYUNA)](../descript/shell-surfaces/surface-brace/introduction_mayuna.md)” in “Shell settings - surfaces.txt”).

Dressups allow you to switch parts of a character’s appearance on or off within a single shell when selected from the owner draw menu.

With SSP, you can also switch dressups using [Sakura Script commands](../list/sakura-script/surface/bang-bind.md).

Dressups are supported only by MATERIA and SSP; in CROW, only the initial dressup configuration is displayed.

However, due to a bug in MATERIA, the dressup menu is displayed only on the `\0` side.

Therefore, in practice, only SSP fully implements dressups, including for `\1` and subsequent sides.

The explanations on this page assume some familiarity with animation configuration.

For information on animation settings, see the “[Writing surfaces.txt - Animations](shell.md#surfacestxtを書く---アニメーション編)” section of the “Creating a shell” page.

## 目次

1. [surfaces.txt 中的设置](bind.md#surfacestxtでの設定)
2. [descript.txt 中的设置](bind.md#descripttxtでの設定)

1. （准备中）SSP 的 dressup 菜单设置等
2. （准备中）具有动态效果的 dressup
3. （准备中）某个 dressup 跨越其他 dressup 前后的三维结构情况

## surfaces.txt 中的设置

```
surface0
{
animation0.interval,bind
animation0.pattern0,add,100,0,0,0
animation0.pattern1,add,101,0,20,35
animation0.pattern2,reduce,102,0,0,0
animation0.pattern3,add,103,0,0,0
}
```

如上所示，将 interval 指定为 bind 的动画会成为 dressup。

关于 add、reduce 等绘制方法，将在后文说明。

等待时间指定为 0，但在 interval 为 bind 的动画（也就是 dressup）设置中，无论指定什么等待时间都会被忽略。

X 坐标和 Y 坐标的偏移位置可以像普通动画模式一样指定。

另外，animation0 中的数字「0」是动画 ID；在 dressup 的情况下，这个 ID 尤其重要。

### 关于 dressup 的绘制方法

在原版伺か中，dressup 基本上使用 bind、add、reduce、insert 这4种方法。

在 SSP 中，除此之外，还可以使用 base、overlay、overlayfast、replace、interpolate、asis 等方法，这些方法也可用于普通动画。

但是，start、stop、move 等不用于合成图像的简单方法无法使用。

## 在 descript.txt 中的设置

简单来说，在 descript.txt 中进行的设置是为将 dressup 显示在 owner draw 菜单的 dressup 菜单中做准备。

按如下方式编写。

```
sakura.bindgroup0.name,服,エプロンドレス,apron.png
sakura.bindgroup1.name,リボン,白リボン,ribbonwhite.png
sakura.bindgroup2.name,服,黒服,black.png
sakura.bindgroup3.name,リボン,黒リボン,ribbonblack.png

sakura.bindgroup0.default,1
sakura.bindgroup1.default,1

kero.bindgroup0.name,ネクタイ,ネクタイ
kero.bindgroup1.name,腕章,黒腕章
kero.bindgroup2.name,腕,ドリル

kero.bindgroup0.default,1
kero.bindgroup1.default,1

sakura.menuitem0,2
sakura.menuitem1,3
sakura.menuitem2,-
sakura.menuitem3,0
sakura.menuitem4,1

kero.menuitem0,0
kero.menuitem1,1
kero.menuitem2,-
kero.menuitem3,2
```

如上所述进行设置后，主角色的 dressup 菜单中会出现「围裙连衣裙」「黑色衣服」「白色缎带」「黑色缎带」

搭档角色的菜单中会出现「领带」「臂章」「手臂」，并且可以自由穿脱这些部件。

?.bindgroup\* 从左到右依次用逗号分隔填写类别名称、部件名称和缩略图文件名。

此时，「bindgroup\*」中 \* 的数字对应于 surfaces.txt 中设置的 dressup 动画 ID。

因此，请注意，所有 surface 中同一件衣服（dressup）都必须使用相同的动画 ID。

?.bindgroup\*.default 用于将动画 ID 为「\*」的 dressup 设置为该 shell 的 dressup 初始值。

按照上例设置后，默认状态为围裙连衣裙和白色缎带、领带和黑色臂章。

Specifying 0 or omitting it turns dressup off.

?.menuitem\*,\* represents the structure of menu items.

Assign numbers in the order they appear in the menu, and specify the corresponding number for bindgroup\*'s \*, separated by commas (note that this is not an animation ID).

Writing “-” instead of a bindgroupID displays a separator (divider line) at that position in the menu.

In the example above, the dressup menu on the main body appears in this order from top to bottom: black clothes, black ribbon, (separator), apron dress, white ribbon.

Thumbnails are displayed as a guide when selecting a menu item.

They can be omitted if unnecessary, but specifying them is useful when there are many dressups or when it is difficult to infer the dressup from its name.

## SSP dressup menu settings and other details

In preparation

## Animated dressup

In preparation

## When a dressup has a three-dimensional structure that spans before and after another dressup

In preparation
