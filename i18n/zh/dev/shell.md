# 创建 shell

本文介绍创建基本 shell 的步骤。

不过，内容主要围绕配置文件的编写，几乎不会涉及绘图或图像处理等内容，请注意。

另请参阅文件结构中的[shell](../manual/shell.md)。

## 目次

1. [准备立绘图像](shell.md#立ち絵となる画像を用意する)

2. [编写 descript.txt](shell.md#descripttxtを書く)

3. [编写 surfaces.txt](shell.md#surfacestxtを書く)

   1. [编写 surfaces.txt - 碰撞判定篇](shell.md#surfacestxtを書く---当たり判定編)
   2. [编写 surfaces.txt - 动画篇](shell.md#surfacestxtを書く---アニメーション編)
   3. [编写 surfaces.txt - element 合成篇](shell.md#surfacestxtを書く---element合成編)

4. [编写 readme.txt](shell.md#readmetxtを書く)

1. [关于半透明 surface](shell.md#半透明のサーフェスについて)
2. [关于追加 shell 的网络更新](shell.md#追加シェルのネットワーク更新について)
3. [关于 dressup](shell.md#着せ替えについて)
4. [汇总多个 surface 的共用设置](shell.md#複数のサーフェスで共通の設定をまとめる)
5. [设置 owner draw 菜单](shell.md#オーナードローメニューを設定する)
6. [设置缩略图像](shell.md#サムネイル画像を設定する)

## 准备立绘图像

首先准备作为立绘的图像。

可以自己绘图，也可以使用名为 free shell 的现成 shell，例如从网上获取的作品。

!!! tip "提示"

    可以通过以下网站寻找 free shell。

    [freeshell wiki](http://wikiwiki.jp/feeshell/)

ghost 图像的基本格式是 png。

不能使用 jpg、bmp 等格式（SSP 中可以）。

使用 png 时，图像尺寸和色数没有限制，但透明度通常无效（仅 SSP 可根据设置启用。请参阅下文[关于半透明 surface](shell.md#半透明のサーフェスについて)）。

如果想缩小文件大小，请使用某种工具减少色数。

构成 shell 的每张立绘，以及下文所述动画的每一帧，都以称为 *surface* 的单位进行管理。

准备名为「surface○○.png」（○○处填入0以上的数字）的图像，或者通过[下文所述的surfaces.txt](shell.md#surfacestxtを書く)合成多张图像，即可准备 surface。

`surface0.png`和`surface10.png`这两张图像通常是必需的。

`surface0.png`是主角色的基本 surface，`surface10.png`是搭档的基本 surface。

即使 ghost 只有一个角色、不需要搭档，也请准备一张纯色填充的图像（即全部显示为透明。见下文）作为`surface10.png`。

surface 也可以写作`surface0000.png`、`surface0010.png`等形式，识别结果与`surface0.png`、`surface10.png`相同。

在 surface 图像中，左上角的一个像素会作为“透明色”，在 ghost 显示时被设为透明。

如果角色上也有与透明色相同的颜色，那部分也会变成透明，因此请将角色没有使用的色系用作透明色。

自己准备作为 surface 使用的图像时，需要注意轮廓的处理。

| ![](../assets/image/surface0_alias1.gif) | → | ![](../assets/image/surface0_alias2.gif) |
| --- | --- | --- |

角色轮廓变成半透明并与背景混合后，就会像右图那样显示。

| ![](../assets/image/surface0_alias3.gif) | → | ![](../assets/image/surface0_alias4.gif) |
| --- | --- | --- |

像这样避免轮廓与背景混合，就能干净地去除背景色。

!!! tip "提示"

    使用 Photoshop 制作时，可以使用[ClearBrain Systems](http://homepage3.nifty.com/khsoft/cbs/)（[存档](https://web.archive.org/web/20100714191818/http://homepage3.nifty.com/khsoft/cbs/)）的[シェル＆縮小サーフェス制作補助プラグインセット for Photoshop](http://homepage3.nifty.com/khsoft/cbs/software/)（[存档](https://web.archive.org/web/20070103182224/http://homepage3.nifty.com/khsoft/cbs/software/)），应该能提高工作效率。

    此外，还有一款名为「[ふちどり](http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82)（[存档](https://web.archive.org/web/20251119211223/http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82)）」的工具，可以识别轮廓并为其添加“边缘线”。

## 编写 descript.txt

`descript.txt`是用于设置 shell 基本信息的文件。

如果没有正确准备`descript.txt`，即使 ghost 识别到 shell，也无法将其识别为 shell。

首先，将以下内容复制并粘贴到名为`descript.txt`的文本文件中，然后改写成适合自己 shell 的内容。

```
charset,Shift_JIS
type,shell
name,このシェルの名前

craftman,制作者名(英数のみで書いてください)
craftmanw,制作者名(日本語表記でも可能)
craftmanurl,制作者のURL(配布サイトurlなど)
```

charset 基本上请设置为 Shift_JIS。

此外还可以设置很多其他项目，但最低限度只需要上述这些（严格来说，只有 name 和 type 是必需的）。

关于本文未介绍的设置，以及各项设置的详细说明，请参阅「[Shell 设置](../descript/shell/index.md)」页面。

举一个例子，要更改整个 shell 的基本 balloon 位置，可以添加

```
sakura.balloon.offsetx,0
sakura.balloon.offsety,0
kero.balloon.offsetx,0
kero.balloon.offsety,0
```

这样的项目。

sakura.balloon.offset用于更改主角色一侧的 balloon 位置，kero.balloon.offset用于更改搭档一侧的 balloon 位置。

增大数字时，x 坐标会移向角色，y 坐标会向下显示。

加上负号后，显示位置会朝相反方向移动，x 坐标会远离角色，y 坐标会向上显示。

要在菜单中显示 dressup，也需要在`descript.txt`中添加相应的内容。相关说明请参阅[dressup 设置](bind.md)页面。

## Writing surfaces.txt

First, create a text file named `surfaces.txt`.

This file is used to configure animations, image compositing, and hit detection for operating characters with the mouse cursor.

Also refer to the page「[Shell settings - surfaces.txt](../descript/shell-surfaces/index.md)」.

After creating `surfaces.txt`, first copy the following to the beginning of the file.

```
charset,Shift_JIS

descript
{
version,1
}
```

The first line specifies the character encoding, just like in `descript.txt`. Unless there is a particular reason to use something else, Shift_JIS is fine.

The lines below it configure the format used to define animations.

If this definition is missing, you must write animation-related definitions using the legacy format (SERIKO/1.x).

Note that the examples that follow on this page use the new format (SERIKO/2.0).

!!! tip "Tip"

    If your surfaces.txt is already written using the legacy format, you can convert it to the new format using the following tools.

    - [The "SERIKO1to2.js" macro for Sakura Editor](http://gallnuts.webcrow.jp/etc/etc.shtml)（[archive](https://web.archive.org/web/20160621201301/http://gallnuts.webcrow.jp/etc/etc.shtml)）

      Usage: Install [Sakura Editor](http://sakura-editor.sourceforge.net/) and use the macro. See the included readme.txt for details.

    - [A tool to convert surfaces.txt from the legacy format to the new format](http://typehoon.kusakage.com/zip/SurfacesTxtConverter.zip)

      Usage: Run the extracted .exe in the same folder as surfaces.txt.

### Writing surfaces.txt - Hit detection

Start by defining hit detection areas for a surface.

First, append the following to `surfaces.txt`.

```
surface0
{
}
```

This means that settings for surface0 are defined inside these braces (\{\}).

In addition to hit detection, settings for animations and elements, which are covered later, are also written here.

Writing the following here defines hit detection areas.

```
surface0
{
collision0,117,71,185,130,Face
collision1,115,174,174,217,Bust
}
```

As shown above, write each hit detection area in sequence as collision0, collision1, collision2, and so on.

Do not reuse numbers within a single surface.

The maximum number of collisions per surface is 256.

The next four numbers specify coordinates.

The top-left corner of the surface image is 0,0; the coordinates are listed as the rectangle's upper-left x,y coordinates, followed by its lower-right x,y coordinates.

The final string is the name of the hit detection area used by the ghost.

You may define multiple hit detection areas with the same name (such as Face or Bust in the example above). For example, if you want the hands to use a hit detection area named Hand, the right and left hands will usually occupy separate regions, so you would specify Hand on two separate lines.

!!! tip "Tip"

    The [Coordin](http://ukgk.s34.xrea.com/poskoma/#content_1_11) tool is useful for getting the coordinates of hit detection areas.

    Drop an image into Coordin and drag to create a rectangular hit detection area.

    The coordinates are automatically copied to the clipboard, so paste them into the numbers for the hit detection area.

!!! tip "Tip"

    In MATERIA, enable the development interface in the settings to view hit detection areas from the owner draw menu.

    In SSP, enable developer features under Settings → Baseware settings → General, open Features → Developer palette, then select Show hit detection areas.

### Writing surfaces.txt - Animations

Animations in 伺か (Ukagaka), called SERIKO, are represented by drawing a sequence of still images.

This section briefly introduces how to configure when animations run and how each still image is layered.

The following example shows an animation of surface0 blinking.

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

To animate surface0.png, write surface0 as shown here, then define the animation inside the braces (\{\}) below it.

```
animation0.interval,sometimes
```

A line in the form animation\*,interval defines when the animation with that number runs.

The number after "animation" is the ID of that animation definition (a set consisting of the interval setting and the subsequent pattern settings for each "frame").

The animation ID can be any number and does not have to be sequential, but *animations with the same meaning are expected to have the same ID*[※](shell.md#surfacestxtを書く---アニメーション編).

The "sometimes" following animation0.interval, specifies the interval.

As in the example, specifying sometimes means that the animation runs automatically from time to time (with a probability of one-half per second).

In other words, this specifies that "the animation with ID 0 runs automatically from time to time."

For other available interval settings, see the [section on animation intervals](../descript/shell-surfaces/surface-brace/h-animationinterval/sometimes.md) in "Shell settings - surfaces.txt".

Next, define each still image (frame) that makes up the animation.

Write them in sequence as pattern0, pattern1, pattern2, and so on. Pattern numbers cannot be skipped or duplicated.

Remember to include the ID of the animation group (animation\*) at the beginning.

Also, write the interval definition and the sequence of pattern definitions together, without separating them into different locations.

```
animation0.pattern0,overlay,100,50,0,0
```

The overlay part specifies the drawing method.

Overlay is a drawing method that displays an image over the original image.

Various other drawing methods are also available.

For details, see the [section on surface drawing methods](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md) in "Shell settings - surfaces.txt".

```
animation0.pattern0,overlayfast,100,50,0,0
```

The 100 part means that this frame draws surface100.

In general, you can think of this as `surface100.png`.

If you specify 101, the image in `surface101.png` is used.

If you specify -1, drawing of the animation stops and the display resets to the base image (surface0 in the example above).

```
animation0.pattern0,overlayfast,100,50,0,0
```

The 50 part is the display duration (in milliseconds).

Specify the *time until switching* to that frame.

Note that this is not the display duration of the frame itself.

```
animation0.pattern0,overlayfast,100,50,0,0
```

The final 0,0 part specifies the frame's display position (x-coordinate,y-coordinate).

Specify how far to offset it from the original image.

The positive x direction is right, and the positive y direction is down.

!!! note "Note"

    #### [※1](shell.md#surfacestxtを書く---アニメーション編)

    For example, suppose a character has a front-facing pose on surface0 and a side-facing pose on surface5, and you want both to have a "blinking" animation.

    In this case, you would define blinking on surface0 as in the example above, and make a similar definition on surface5. However, because the poses are different, the surfaces (images) used as frames should also be different.

    Since both are treated as the same "blinking" animation, however, it is preferable to use the same animation ID (for example, 0).

    This rule is especially important when using "[dressup](bind.md)", which is described in another section.

### Writing surfaces.txt - element compositing

element is a mechanism for combining multiple part images and treating them as a single surface.

For example, if every surface had to be prepared as an image such as surface0.png, then adding expressions to a character would require preparing a full-body standing image for every expression, even if only the shape of the mouth changed slightly.

However, if body parts and expression parts can be separated and composited, then adding expressions would only require preparing the expression variations as images, greatly reducing the overall size of the shell.

Furthermore, if the eye and mouth parts are separated, their combinations can create various expressions, allowing you to produce a range of expressions without actually drawing each one.

Here is an example of an element definition.

```
surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face1.png,0,0
}
```

This defines the result of compositing "face1.png" over "body0.png" as surface1.

You can add as many parts as you want to composite.

In this case, surface1.png is not needed.

```
element0,overlay,body0.png,0,0
```

The number immediately following "element" is the element ID (sequence number) on that surface.

IDs are consecutive numbers starting from 0. The smaller the number, the further down (toward the back of the screen) the part is composited.

Note that png images with names like surface\*.png are treated as parts below element0.

```
element0,overlay,body0.png,0,0
```

The next keyword is the drawing method.

Basically, it is [the same as for animations](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md), but some methods that do not simply composite images, such as start and move, cannot be used.

```
element0,overlay,body0.png,0,0
```

Next, specify the name of the file to composite.

You can specify a png file with any name.

```
element0,overlay,body0.png,0,0
```

The last two numbers specify the compositing position (x-coordinate, y-coordinate).

They specify how far to offset the image when compositing it over the base image.

The positive direction on the x-axis is right, and the positive direction on the y-axis is down.

In this example, unlike the examples for [hit detection](shell.md#surfacestxtを書く---当たり判定編) and [animation](shell.md#surfacestxtを書く---アニメーション編) mentioned earlier, the element definition is on surface1 rather than surface0.

This is only an example, but there is a reason for this[※](shell.md#surfacestxtを書く---element合成編).

When considering only the behavior of the shell (ghost) itself, there is no problem at all with using element on surface0 or 10.

!!! note "Note"

    #### [※2](shell.md#surfacestxtを書く---element合成編)

    Consider a web service, such as a ghost database, that wants to display ghost previews.

    [As mentioned earlier](shell.md#立ち絵となる画像を用意する), surface0 and surface10 are considered basic surfaces and generally cannot be omitted.

    In other words, surface0 and 10 are assumed to always exist, so they are convenient to use for previews.

    However, if surface0 or 10 is constructed through element compositing, the person displaying the preview will need to read the element definition and composite the parts as intended.

    This presents some obstacles, both for manual work and for systems that automate the process with programs.

    Therefore, if you plan to use such services, it may be better to prepare surface0 and 10 as actual png files.

    One service that displays such previews is the update feed "[SiReFaSo](https://sirefaso.appspot.com/) ([archive](https://web.archive.org/web/20170423052451/https://sirefaso.appspot.com/))".

## Writing readme.txt

If a file named `readme.txt` exists, it can be displayed in the owner draw menu and during installation.

It can be omitted, but if the ghost author and shell author are different, it may be a good idea to specify contact information.

Enter any necessary information, such as a description of the shell or notices.

Like other files, readme can use encodings other than Shift JIS by specifying charset,UTF-8 on the first line or including a BOM.

## About semi-transparent surfaces

To make an image semi-transparent, create a "pna" file with the same name as the image you want to make semi-transparent.

For example, `surface0.png` would have a corresponding file named `surface0.pna`.

With SSP, you can also prepare these for parts used in [element compositing](shell.md#surfacestxtを書く---element合成編). For example, `face1.png` would have a corresponding `face1.pna`.

A pna is simply a grayscale png representing opacity, renamed with the pna extension.

Areas made completely white in a pna are opaque, areas made completely black are transparent, and the shades in between are semi-transparent.

| ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
| --- | --- | --- | --- | --- |
| surface0.png |  | surface0.pna |  | Desktop display |

Semi-transparent areas can be clicked as part of the character.

Therefore, make transparent areas completely black (RGB is 0,0,0).

Also, with SSP, instead of using pna, you can create `surface*.png` images as PNGs with an alpha channel and use that alpha channel for transparency.

In that case, you need to add the following entry to `descript.txt`.

```
seriko.use_self_alpha,1
```

For instructions on how to create PNGs with an alpha channel, refer to the documentation for your paint software (some software may not support them. You can also search for terms such as PNG with transparency, 32-bit PNG, and αPNG).

## About Network Updates for Additional Shells

SSP allows network update functionality to be added to the shell itself.

For details, read the page “[Support for Network Updates](update.md)”.

## About Dressup

In 伺か (Ukagaka), dressup is configured as a type of animation.

For details, read the page “[Configuring Dressup](bind.md)”.

## Grouping Shared Settings Across Multiple Surfaces

For example, if there are several surfaces with the same character pose, some of them may have exactly the same hit detection areas and animation settings.

In such cases, there are several convenient ways to specify settings, besides repeatedly copying and pasting the same settings into the braces of each surface.

However, most of these methods are *SSP-only*.

For details, see “[ID specifications available in surface\* braces](../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md)” on the “Shell settings - surfaces.txt” page.

## Configuring the Owner Draw Menu

You can also configure the background image, text color, and other settings for the owner draw menu (right-click menu) in the shell.

For details, see “[Configuring the Owner Draw Menu](ownerdraw.md)”.

## Setting a Thumbnail Image

You can display a thumbnail image when the cursor is over a shell in the shell selection menu of the owner draw menu.

This is useful when, for example, there are multiple shells and you want to make them easier to distinguish at a glance.

If an image named `thumbnail.png` is in the same folder, it will be used automatically.
