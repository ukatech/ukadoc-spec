# 绘制方法

## 概述

[animation模式定义](../animation-star-.pattern-star.md)以及[element定义](../element-star.md)中，各帧（部件）的合成・绘制方法。

除了图像合成以外，还存在各种用途的方法，例如替换[基础surface](../caption_basesurface.md)（base）、移动基础surface（move），以及插入、执行其他动画（insert、start、stop、alternativestart、alternativestop）。

## dressup中的绘制方法处理

在dressup定义中，非图像合成的方法（move、insert、start、stop、alternativestart、alternativestop）无效（按overlay处理）。但base只有在用于第一个pattern时才有效，因此可以实现仅在该dressup开启时替换基础surface的机制。

作为dressup用方法实现的add和bind，在实现上与overlay同义。在dressup中，这三种方法无论指定哪一种，效果都相同。

## element定义中的绘制方法处理

在element定义中，非图像合成的方法（base、move、insert、start、stop、alternativestart、alternativestop）无效（按overlay处理）。

其他dressup用方法add、bind也无效（但在SSP的当前实现中，无效的指定会被解释为overlay，因此最终会按指定进行绘制）。

不言而喻，第一个element（element0；若不存在surface\*.png，则后续element也可能是第一个）中指定的绘制方法，大多数都与base同义。但asis方法会让透明色照常显示，这一点仍然有效。

此外，element合成的surface用作动画部件时，element合成的结果会被视为一张图像。但请注意，此实现始于SSP2.3.53，在此之前的行为未定义。

## 合成类方法在element、动画、dressup中的异同

合成类方法的含义会因其用于element、动画还是dressup而有所不同。

element定义的目的是获得一张作为基础surface的静态图像。在element定义中，会基于截至上一刻的合成结果继续进行下一次合成并不断重复，最终得到一张静态图像。

dressup定义与element定义一样，也是用于获得静态图像的机制，因此绘制方法的处理流程与element定义十分相似。在dressup的pattern定义中，第一个pattern会与基础surface合成，之后基于截至上一刻的合成结果继续进行下一次合成并不断重复，最终获得一张静态图像。因此，dressup会表现得像是与基础surface融为一体。

与此相对，非dressup的普通动画属于视频式表现，其处理流程与前两者大不相同。动画的每个pattern定义只是构成动画的各个帧的定义，彼此独立。每个pattern定义都会将基础surface与一张新图像合成，生成新的帧，因此前一个pattern定义（前一帧）的合成结果不会影响下一帧。如此不断绘制新帧，即可实现视频式表现。

然而，在所有情况下，合成类方法的共同点都是承担合成「原始图像」和「新图像」这两张图像的功能。因此，ukadoc为方便起见，在说明绘制方法时，将*「原始图像」*称为*基础图层*，将后者*「新图像」*称为*新图层*。

换言之，动画的每个pattern定义都是将基础surface作为基础图层，与新图层合成以生成帧。与此相对，dressup和element合成则是将截至上一刻的合成结果作为基础图层，与新图层反复合成，最终得到一张静态图像。

## 绘制方法与透明色

图像左上角1像素的颜色会被视为透明色，实际显示时相同颜色的部分会变为透明；这同样适用于pattern定义中使用的surface以及element定义中使用的图像。

此时，参与合成的各图像的透明色RGB值不必完全一致。

各绘制方法对透明色的处理各有特点，请参阅相应条目。

## 基础图层与新图层的偏移和重叠

将新图层合成到基础图层外部区域时（由图像尺寸或位置关系造成）的行为取决于baseware的实现。

在MATERIA中，超出基础图层的部分不会显示。

在CROW中，若进行超出基础图层的合成，图像将无法正确绘制。

在SSP中，允许将新图层合成到基础图层之外，并会以*在基础图层中补充全透明区域，直至新图层不再超出范围*的方式处理。

反过来，新图层外部的区域是*不同于全透明区域的空区域*；合成时*不会发生任何变化，基础图层的内容会原样保留*。理解会影响合成结果的新图层全透明区域的replace方法和reduce方法时，尤其要注意这一前提。
