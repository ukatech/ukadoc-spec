# dressup（MAYUNA）

## 概述

伺か（Ukagaka）的shell具有一种称为dressup的机制，可在单个shell中显示或隐藏多个服装等部件，或切换其种类。

伺か（Ukagaka）的shell将dressup归类为一种动画。<br />
但与其他动画不同，它不会逐帧播放，而是在动画开始时立即合成所有帧（pattern）和基础表面，此后作为静止图像处理（因此pattern定义中的等待时间参数会被忽略）。<br />
这种“绘制表现得仿佛与基础表面融为一体”的特性，非常适合用于表示衣物之类的内容。

dressup动画的开始和结束，主要通过切换所有者绘制菜单中的dressup菜单来控制。在SSP中，还可以通过Sakura Script的[`\![bind]`](../../../list/sakura-script/surface/bang-bind.md)标签从ghost一侧进行控制。<br />
所有者绘制菜单一侧的设置不在surfaces.txt中，而是在[descript.txt](../../shell/index.md)中进行，请参阅该页面。

此外，surfaces.txt中与动画相关的一系列规范称为MAYUNA。

## 基本格式与示例

```
surface0
{
// 服1の定義　アニメーションIDは0
animation0.interval,bind
animation0.pattern0,add,500,0,50,100

// 服2の定義　アニメーションIDは1
animation1.interval,bind
animation1.pattern0,add,501,0,50,100
}

//--- 以下着せ替えパーツ定義 ---
// 服1
surface500
{
element0,overlay,dress1.png,0,0
}

// 服2
surface501
{
element0,overlay,dress2.png,0,0
}
```

surfaces.txt中的dressup定义例如上面所示。

上例中，为surface0定义了“服1”和“服2”两种dressup。

与常规动画定义一样，需要interval定义和pattern定义。在interval定义中指定bind，表示该动画定义为dressup。

动画的pattern定义会按照帧数逐个编写；而dressup使用静止图像，因此需要合成的与其说是帧，不如说是所需数量的部件。如果构成dressup的部件只有一个，如示例所示，则只需一行pattern行。此外，dressup的各个部件会立即合成，因此会忽略等待时间参数。

pattern定义中的绘制方法将在后文说明。

## 可用的绘制方法

在MATERIA（本家伺か）中，可使用为dressup准备的4种方法，即“bind”“add”“reduce”“insert”。其中bind是旧规范，add与其向后兼容。

在SSP中，一部分为普通动画准备的绘制方法也可用于dressup。

有关dressup可用的绘制方法等详细信息，请参阅[绘制方法](h-drowmethod/introduction_drawmethod.md)一节。

## 间隔的组合指定中的bind

在SSP中，如[动画间隔一节](h-animationinterval/introduction_animationinterval.md)所述，可以组合指定间隔。

在组合指定中包含bind时，动画会失去bind单独使用时原有的静止图像特性（pattern定义中的等待时间参数不再被忽略）。但动画的生命周期不会改变，因此例如使用bind+runonce这样的组合指定时，所有pattern绘制完成时的显示内容会持续保留，直到基础表面发生变化或dressup状态发生变化。

因此，在包含bind的间隔组合指定中，应该在pattern定义的最后一行合成要作为静止图像保留的绘制内容，而不结束动画。

## 多重dressup定义（仅SSP）

如果动画帧所引用的目标表面定义了该表面的动画，通常会忽略这些动画。

但在SSP中，仅当interval为bind的动画（即dressup）不会被忽略，而是会生效。

这样一来，对于会受dressup影响的动画结构，就可以在动画帧一侧定义与dressup相对应的内容。

此外，也可以将多重dressup嵌套，但循环引用会被忽略。
