# 创建 shell

这里介绍创建基本 shell 的步骤。

不过，内容主要围绕配置文件的编写，几乎没有涉及绘图和图像处理等方面，请知悉。

另请参阅文件结构中的[shell](../manual/shell.md)。

## 目次

1. [准备立绘图像](shell.md#立ち絵となる画像を用意する)

2. [编写 descript.txt](shell.md#descripttxtを書く)

3. [编写 surfaces.txt](shell.md#surfacestxtを書く)

   1. [编写 surfaces.txt - 碰撞判定](shell.md#surfacestxtを書く---当たり判定編)
   2. [编写 surfaces.txt - 动画](shell.md#surfacestxtを書く---アニメーション編)
   3. [编写 surfaces.txt - element 合成](shell.md#surfacestxtを書く---element合成編)

4. [编写 readme.txt](shell.md#readmetxtを書く)

1. [关于半透明 surface](shell.md#半透明のサーフェスについて)
2. [关于追加 shell 的网络更新](shell.md#追加シェルのネットワーク更新について)
3. [关于 dressup](shell.md#着せ替えについて)
4. [汇总多个 surface 的共同设置](shell.md#複数のサーフェスで共通の設定をまとめる)
5. [设置 owner draw 菜单](shell.md#オーナードローメニューを設定する)
6. [设置缩略图](shell.md#サムネイル画像を設定する)

## 准备立绘图像

首先准备好立绘图像。

可以自行绘制，也可以使用称为 free shell 的已发布成品 shell。

!!! tip "提示"

    可以从以下网站寻找 free shell。

    [freeshell wiki](http://wikiwiki.jp/feeshell/)

ghost 使用的基本图像格式是 png。

jpg、bmp 等格式无法使用（SSP 中可以）。

使用 png 时，尺寸和颜色数没有限制，但透明度基本无效（仅 SSP 可根据设置启用。请参阅后文[关于半透明 surface](shell.md#半透明のサーフェスについて)）。

如果想减小文件大小，请使用工具进行减色处理。

构成 shell 的每一张立绘，以及后文所述动画中的每一帧，都以称为 *surface* 的单位进行管理。

准备 surface 的方法有两种：准备名为「surface○○.png」（○○部分填入0以上的数字）的图像，或者通过[后文所述的 surfaces.txt](shell.md#surfacestxtを書く)合成多张图像。

`surface0.png`和`surface10.png`这两张图像基本上是必需的。

`surface0.png`是主侧的基本 surface，`surface10.png`是搭档侧的基本 surface。

即使 ghost 中只有一个角色、不需要搭档，也请准备一张纯色填充图像（＝全部透明显示。后文介绍）作为`surface10.png`。

即使将 surface 写作`surface0000.png`、`surface0010.png`等，也会与`surface0.png`、`surface10.png`一样被识别。

在 surface 图像中，左上角的一个像素会作为「透明色」，在 ghost 显示时被设为透明。

如果角色内部也有与透明色相同的颜色，那部分也会变透明，因此请使用角色没有用到的色系作为透明色。

自行准备作为 surface 使用的图像时，需要注意的特点之一是轮廓的处理。

| ![](../assets/image/surface0_alias1.gif) | → | ![](../assets/image/surface0_alias2.gif) |
| --- | --- | --- |

角色轮廓会因为半透明而与背景混合，最终就会像右图那样显示。

| ![](../assets/image/surface0_alias3.gif) | → | ![](../assets/image/surface0_alias4.gif) |
| --- | --- | --- |

像这样避免轮廓与背景混合，就能干净地抠出颜色。

!!! tip "提示"

    如果使用 Photoshop 制作，[ClearBrain Systems](http://homepage3.nifty.com/khsoft/cbs/)（[存档](https://web.archive.org/web/20100714191818/http://homepage3.nifty.com/khsoft/cbs/)）的[シェル＆縮小サーフェス制作補助プラグインセット for Photoshop](http://homepage3.nifty.com/khsoft/cbs/software/)（[存档](https://web.archive.org/web/20070103182224/http://homepage3.nifty.com/khsoft/cbs/software/)）可以帮助提高工作效率。

    此外，还有一款名为「[ふちどり](http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82)（[存档](https://web.archive.org/web/20251119211223/http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82)）」的工具已经发布，可用于识别轮廓并添加「边缘」。

## 编写 descript.txt

`descript.txt`是用于设置 shell 基本信息的文件。

如果没有正确准备`descript.txt`，ghost 就无法识别该 shell。

首先，将以下内容复制到文本文件中，并将文件命名为`descript.txt`，然后根据自己的 shell 修改为适当的内容。

```
charset,Shift_JIS
type,shell
name,このシェルの名前

craftman,制作者名(英数のみで書いてください)
craftmanw,制作者名(日本語表記でも可能)
craftmanurl,制作者のURL(配布サイトurlなど)
```

charset 基本上请设置为 Shift_JIS。

还可以设置许多其他项目，但最低限度需要设置的项目大致如上（严格来说，只有 name 和 type 是必需的）。

有关此处未介绍的设置以及各项设置的详细说明，请参阅「[Shell 设置](../descript/shell/index.md)」页面。

举一个例子，要更改整个 shell 的基本 balloon 位置，可以添加如下项目：

```
sakura.balloon.offsetx,0
sakura.balloon.offsety,0
kero.balloon.offsetx,0
kero.balloon.offsety,0
```

就需要添加这类项目。

sakura.balloon.offset 用于更改主侧的 balloon 位置，kero.balloon.offset 用于更改搭档侧的 balloon 位置。

数值增大时，x 坐标会朝角色方向移动，y 坐标会向下移动。

添加负号后，显示位置会朝相反方向移动，x 坐标会远离角色，y 坐标则会向上移动。

如果要在菜单中显示 dressup，也需要在`descript.txt`中进行设置。有关这部分的说明，请参阅[dressup 设置](bind.md)页面。

## 编写surfaces.txt

首先创建一个名为`surfaces.txt`的文本文件。

这是用于设置动画、图像合成，以及使用鼠标光标操作角色时的碰撞判定等内容的文件。

请同时参阅「[Shell设置 - surfaces.txt](../descript/shell-surfaces/index.md)」页面。

创建`surfaces.txt`后，首先将以下内容复制到文件开头。

```
charset,Shift_JIS

descript
{
version,1
}
```

第一行是与`descript.txt`相同的字符编码指定。没有特别理由时，使用Shift_JIS即可。

下面的内容用于设置动画的定义格式。

如果没有这段内容，动画相关定义就必须使用旧格式（SERIKO/1.x）。

请注意，本页以下出现的示例使用的是新格式（SERIKO/2.0）。

!!! tip "提示"

    已使用旧格式编写的surfaces.txt，可以使用以下工具从旧格式转换为新格式。

    - [Sakura Editor宏「SERIKO1to2.js」](http://gallnuts.webcrow.jp/etc/etc.shtml)（[存档](https://web.archive.org/web/20160621201301/http://gallnuts.webcrow.jp/etc/etc.shtml)）

      使用方法：安装[Sakura Editor](http://sakura-editor.sourceforge.net/)后，将其用作宏。详细信息请参阅附带的readme.txt。

    - [将surfaces.txt从旧格式转换为新格式的工具](http://typehoon.kusakage.com/zip/SurfacesTxtConverter.zip)

      使用方法：在surfaces.txt所在的文件夹中运行解压出的.exe。

### 编写surfaces.txt - 碰撞判定篇

首先尝试为surface定义碰撞判定。

请先将以下内容追加到`surfaces.txt`中。

```
surface0
{
}
```

这表示在这个大括号（\{\}）内设置surface0的相关内容。

不仅是碰撞判定，后面将介绍的动画和element设置也都写在这里。

像下面这样编写，就可以定义碰撞判定。

```
surface0
{
collision0,117,71,185,130,Face
collision1,115,174,174,217,Bust
}
```

如上所示，每处碰撞判定依次写为collision0、collision1、collision2。

请确保编号在同一个surface内不重复。

每个surface最多可以有256个collision。

后面的四个数字用于指定坐标。

以surface图像本身的左上角为0,0，依次指定矩形左上角的x、y坐标和右下角的x、y坐标。

最后的字符串是ghost一侧使用的碰撞判定名称。

另外，多个碰撞判定可以使用同一个名称（上例中的Face、Bust）。例如，要将手的碰撞判定命名为Hand时，通常左右手的区域会分开，因此指定Hand的行也会分成两行。

!!! tip "提示"

    使用[Coordin](http://ukgk.s34.xrea.com/poskoma/#content_1_11)工具可以方便地获取碰撞判定的坐标。

    将图像拖放到Coordin中，再通过拖动创建矩形碰撞判定区域。

    坐标会自动复制到剪贴板，请将其粘贴到碰撞判定的数字中。

!!! tip "提示"

    在MATERIA中，如果在设置中勾选开发接口，就可以通过owner draw菜单查看碰撞判定区域。

    在SSP中，前往设置→本体设置的「一般」，启用开发者功能，然后打开功能→开发用调色板，通过显示碰撞判定进行确认。

### 编写surfaces.txt - 动画篇

伺か（Ukagaka）中的动画称为SERIKO，它通过连续绘制静止图像来呈现。

这里将简要介绍动画的执行时机，以及各张静止图像的叠放方式等设置方法。

下面以让surface0眨眼为例说明动画。

```
surface0
{
animation0.interval,sometimes
animation0.pattern0,overlayfast,100,50,0,0
animation0.pattern1,overlayfast,101,50,0,0
animation0.pattern2,overlayfast,100,50,0,0
animation0.pattern3,overlay,-1,100,0,0

collision0,117,71,185,130,Face
collision1,115,174,174,217,Bust
}
```

要让surface0.png播放动画，需要像这样写上surface0，并在其下方的大括号（\{\}）内定义动画内容。

```
animation0.interval,sometimes
```

animation\*,interval这一行用于定义对应编号的动画何时执行。

「animation」后面的数字是动画定义的ID。一个动画定义由时机设置interval和后续的「帧」设置pattern等组成。

动画ID可以任意指定，不必连续编号，但预期*具有相同含义的动画会使用相同的ID*。[※](shell.md#surfacestxtを書く---アニメーション編)

animation0.interval,后面的「sometimes」是间隔定义的内容。

如示例所示指定sometimes时，该动画会偶尔自动执行（每秒的执行概率为二分之一）。

也就是说，这里指定的是「ID为0的动画会偶尔自动播放」。

关于其他可用的时机指定，请参阅「Shell设置 - surfaces.txt」中的[动画间隔相关章节](../descript/shell-surfaces/surface-brace/h-animationinterval/sometimes.md)。

接下来，逐张定义组成动画的静止图像（帧）。

依次写为pattern0、pattern1、pattern2。模式编号不能缺失或重复。

请记得在开头加入同一动画组的ID（animation\*）。

另外，请将interval定义行和一系列pattern定义行连续编写，不要分开写在不同位置。

```
animation0.pattern0,overlay,100,50,0,0
```

overlay部分指定绘制方法。

overlay是一种将图像叠加显示在原始图像上的绘制方法。

除此之外还有多种绘制方法。

详细信息请参阅「Shell设置 - surfaces.txt」中的[surface绘制方法相关章节](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md)。

```
animation0.pattern0,overlayfast,100,50,0,0
```

100部分表示该帧要绘制surface100。

通常可以将其理解为`surface100.png`。

指定101时，会使用`surface101.png`图像。

指定-1时，会停止该动画的绘制，并重置为显示基础图像（上例中为surface0）。

```
animation0.pattern0,overlayfast,100,50,0,0
```

50部分是显示时间（单位：毫秒）。

请指定*切换到该帧之前的时间*。

请注意，这不是该帧自身的显示时间。

```
animation0.pattern0,overlayfast,100,50,0,0
```

最后的0,0部分是帧的显示位置（x坐标、y坐标）。

指定相对于原始图像的偏移量。

x方向向右为正，y方向向下为正。

!!! note "注"

    #### [※1](shell.md#surfacestxtを書く---アニメーション編)

    例如，假设角色有正面姿势的surface0和侧面姿势的surface5，并且希望两者都能播放「眨眼」动画。

    此时，除了像上例那样在surface0中定义眨眼动画外，还需要在surface5中进行类似的定义；但由于侧面和正面姿势不同，用作帧的surface（图像）应该也不同。

    不过，两者都是以相同方式处理的「眨眼」，因此最好使用相同的动画ID（例如0）。

    这条规则尤其是在另一节介绍的「[dressup](bind.md)」中是必需的。

### 编写 surfaces.txt - element 合成篇

element是一种将多个部件图像合成为一张图像，并作为一个 surface 使用的机制。

例如，如果所有 surface 都必须准备成 surface0.png 这样的图像，那么要增加角色的表情时，即使只是嘴型略有不同，也需要准备与表情数量相同的全身立绘。

但是，如果可以将身体部件和表情部件分开并进行合成，那么增加表情时，只需准备表情差分图像即可，因此 shell 的整体容量会大幅减少。

此外，如果再将眼部和嘴部部件分开，那么只需组合眼睛和嘴巴就能表现出各种表情，甚至无需实际绘制那些表情，也能制作出一定数量的表情。

以下是 element 定义的写法示例。

```
surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face1.png,0,0
}
```

这样，「body0.png」上叠加「face1.png」后，就会被定义为 surface1。

可以根据要叠加的部件数量，任意添加多行。

另外，这种情况下不需要 surface1.png。

```
element0,overlay,body0.png,0,0
```

紧接在「element」后面的数字，是该 surface 中 element 的 ID（序号）。

ID 从 0 开始连续编号。数字越小，合成的部件越靠下（越靠近画面深处）。

请注意，名为 surface\*.png 的 png 图像会被视为位于 element0 下方的部件。

```
element0,overlay,body0.png,0,0
```

接下来的关键字是绘制方法。

基本上[与动画中的相同](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md)，但 start、move 等并非单纯合成图像的部分方法无法使用。

```
element0,overlay,body0.png,0,0
```

接着指定要合成的文件名。

可以指定任意名称的 png 文件。

```
element0,overlay,body0.png,0,0
```

最后两个数字用于指定合成位置（x 坐标、y 坐标）。

指定相对于基础图像的偏移量。

x 方向向右为正，y 方向向下为正。

顺便一提，与之前[命中判定](shell.md#surfacestxtを書く---当たり判定編)和[动画](shell.md#surfacestxtを書く---アニメーション編)的示例不同，这次是在 surface1 而不是 surface0 中定义 element。

这虽然只是示例，但这么做还是有一定理由的[※](shell.md#surfacestxtを書く---element合成編)。

如果只考虑 shell（ghost）自身的运行，在 surface0 或 surface10 中使用 element 完全没有问题。

!!! note "注"

    #### [※2](shell.md#surfacestxtを書く---element合成編)

    例如，可以设想某种 Web 服务（如 ghost 数据库）需要显示 ghost 预览。

    [如前所述](shell.md#立ち絵となる画像を用意する)，surface0 和 surface10 被视为基本 surface，通常不能省略。

    也就是说，surface0 和 surface10 一定存在，因此很适合用于预览。

    但是，如果 surface0 或 surface10 是通过 element 合成构成的，预览显示方就需要读取 element 定义，并按预期进行合成。

    这不仅会给人工操作带来障碍，也会给通过程序自动化的系统带来一些障碍。

    因此，如果考虑使用这类服务，最好将 surface0 和 surface10 准备为实际的 png 图像。

    另外，提供这类预览显示的服务包括更新 feed「[SiReFaSo](https://sirefaso.appspot.com/)（[存档](https://web.archive.org/web/20170423052451/https://sirefaso.appspot.com/)）」。

## 编写 readme.txt

如果存在名为 `readme.txt` 的文件，就可以在 owner draw 菜单或安装时等场景中显示其内容。

虽然可以省略，但如果 ghost 作者和 shell 作者不同，最好写明联系方式。

请填写 shell 说明、联系事项等必要内容。

与其他文件一样，readme 也可以在第一行写上 charset,UTF-8 等内容，或包含 BOM，以使用 Shift JIS 以外的字符编码。

## 关于半透明的 surface

要实现半透明，需要为要设置半透明的图像创建一个同名的「pna」文件。

例如，为 `surface0.png` 创建 `surface0.pna`。

在 SSP 中，也可以为[element 合成](shell.md#surfacestxtを書く---element合成編)的部件准备 pna。例如，为 `face1.png` 创建 `face1.pna`。

pna 是将用灰度表示透明度的 png 图像直接重命名后的文件。

pna 中完全白色的部分是不透明的，完全黑色的部分是透明的，中间色则为半透明。

| ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
| --- | --- | --- | --- | --- |
| surface0.png |  | surface0.pna |  | 桌面上的显示 |

半透明部分可以作为角色点击。

因此，透明部分请使用纯黑色（RGB 为 0,0,0）。

此外，在 SSP 中，也可以不使用 pna，而将 `surface*.png` 图像制作为带有 alpha 通道的 PNG，并将其 alpha 通道用作透明度。

这种情况下，需要在 `descript.txt` 中添加以下内容。

```
seriko.use_self_alpha,1
```

关于如何创建带有 alpha 通道的 PNG，请参阅各种绘图软件的说明（有些软件可能无法处理这类图像。也可以尝试搜索「带透明度的 PNG」「32bitPNG」「αPNG」等关键词）。

## 关于追加 shell 的网络更新

在 SSP 中，可以为 shell 本身添加网络更新功能。

详情请阅读“[支持网络更新](update.md)”页面。

## 关于 dressup

在伺か (Ukagaka) 中，dressup 是作为动画的一种进行设置的。

详情请阅读“[dressup 设置](bind.md)”页面。

## 汇总多个 surface 的通用设置

例如，可能存在多个角色姿势相同的 surface，它们的碰撞判定、动画指定等也完全相同。

遇到这种情况，除了在各个 surface 的大括号中反复复制粘贴相同的设置外，还有几种方便的写法。

不过，其中大多数方法仅限于 *SSP*。

详情请参阅“Shell 设置 - surfaces.txt”页面中的“[可在 surface\*大括号中指定的 ID](../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md)”。

## 设置 owner draw 菜单

shell 也可以设置 owner draw 菜单（右键菜单）的背景图像和文字颜色等。

详情请参阅“[owner draw 菜单设置](ownerdraw.md)”。

## 设置缩略图

在 owner draw 菜单的 shell 选择项中，可以在光标悬停在 shell 上时显示缩略图。

如果有多个 shell，或者希望一眼就能分辨它们，准备缩略图会比较方便。

如果同一文件夹中有名为 `thumbnail.png` 的图像，就会自动使用。
