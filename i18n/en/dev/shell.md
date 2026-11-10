# Creating a Shell

This section explains the basic steps for creating a shell.

Please note that it focuses on writing configuration files and barely covers drawing or image editing.

See also [Shell](../manual/shell.md) in the file structure documentation.

## 目次

1. [Prepare an image of the character sprite](shell.md#立ち絵となる画像を用意する)

2. [Write descript.txt](shell.md#descripttxtを書く)

3. [Write surfaces.txt](shell.md#surfacestxtを書く)

   1. [Write surfaces.txt - hit detection](shell.md#surfacestxtを書く---当たり判定編)
   2. [Write surfaces.txt - animation](shell.md#surfacestxtを書く---アニメーション編)
   3. [Write surfaces.txt - element compositing](shell.md#surfacestxtを書く---element合成編)

4. [Write readme.txt](shell.md#readmetxtを書く)

1. [About translucent surfaces](shell.md#半透明のサーフェスについて)
2. [Network updates for additional shells](shell.md#追加シェルのネットワーク更新について)
3. [About dress-up](shell.md#着せ替えについて)
4. [Consolidate settings shared by multiple surfaces](shell.md#複数のサーフェスで共通の設定をまとめる)
5. [Configure the owner-draw menu](shell.md#オーナードローメニューを設定する)
6. [Configure the thumbnail image](shell.md#サムネイル画像を設定する)

## Preparing Images for Standing Character Art

First, prepare the images to use as standing character art.

You can draw your own art or use a pre-made shell distributed as a free shell.

!!! tip "Tip"

    You can find free shells on sites such as the following.

    [freeshell wiki](http://wikiwiki.jp/feeshell/)

The standard image format for ghosts is png.

Formats such as jpg and bmp cannot be used (but are supported by SSP).

There are no restrictions on image size or color depth when using png, but transparency is generally disabled (it can be enabled in SSP depending on the settings. See [About Semi-Transparent Surfaces](shell.md#半透明のサーフェスについて) below).

To reduce file size, use a tool to reduce the color depth.

Each standing-character image that makes up a shell, and each frame of the animation described below, is managed as a unit called a *surface*.

You can prepare surfaces by creating images named “surface○○.png” (where ○○ is a number greater than or equal to 0), or by compositing multiple images in [surfaces.txt, described below](shell.md#surfacestxtを書く).

The two images `surface0.png` and `surface10.png` are generally required.

`surface0.png` is the main character's default surface, and `surface10.png` is the partner character's default surface.

Even if the ghost has only one character and does not need a partner, prepare `surface10.png` as an image filled with a single color (= displayed entirely transparent; described below), for example.

Surfaces named `surface0000.png`, `surface0010.png`, and so on are recognized in the same way as `surface0.png`, `surface10.png`, and so on.

In a surface image, the top-left pixel is used as the “transparent color” and is displayed as transparent in the ghost.

If the character contains pixels of the same color as the transparent color, those pixels will also become transparent, so use a color family that is not used in the character for the transparent color.

If you prepare your own images for use as surfaces, one feature to pay attention to is how the outlines are handled.

| ![](../assets/image/surface0_alias1.gif) | → | ![](../assets/image/surface0_alias2.gif) |
| --- | --- | --- |

The character's outline becomes semi-transparent and blends into the background, causing it to appear as shown on the right.

| ![](../assets/image/surface0_alias3.gif) | → | ![](../assets/image/surface0_alias4.gif) |
| --- | --- | --- |

If you prevent the outline from blending into the background like this, the colors are removed cleanly.

!!! tip "Tip"

    When creating a shell using Photoshop, you can work more efficiently with the [Shell & Reduced Surface Production Assistance Plugin Set for Photoshop](http://homepage3.nifty.com/khsoft/cbs/software/) ([archive](https://web.archive.org/web/20070103182224/http://homepage3.nifty.com/khsoft/cbs/software/)) from [ClearBrain Systems](http://homepage3.nifty.com/khsoft/cbs/) ([archive](https://web.archive.org/web/20100714191818/http://homepage3.nifty.com/khsoft/cbs/)).

    A tool called "[Fuchidori](http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82) ([archive](https://web.archive.org/web/20251119211223/http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82))" that detects outlines and adds a border is also available.

## Writing descript.txt

`descript.txt` is a file for configuring basic information about the shell.

If `descript.txt` is not prepared correctly, the ghost will not recognize the shell.

For now, copy the following content, paste it into a text file named `descript.txt`, and edit it to suit your shell.

```
charset,Shift_JIS
type,shell
name,このシェルの名前

craftman,制作者名(英数のみで書いてください)
craftmanw,制作者名(日本語表記でも可能)
craftmanurl,制作者のURL(配布サイトurlなど)
```

In general, set charset to Shift_JIS.

There are various other settings you can configure, but the above are the minimum required (strictly speaking, only name and type are required).

For settings not covered here, or more detailed explanations of each setting, see the [Shell settings](../descript/shell/index.md) page.

As just one example, to change the shell-wide default balloon position,

```
sakura.balloon.offsetx,0
sakura.balloon.offsety,0
kero.balloon.offsetx,0
kero.balloon.offsety,0
```

you would add entries like these.

sakura.balloon.offset changes the balloon position for the main character, while kero.balloon.offset changes it for the partner character.

Increasing the numbers moves the x-coordinate closer to the character and displays the y-coordinate lower.

Adding a minus sign moves the display position in the opposite direction: the x-coordinate moves away from the character, and the y-coordinate is displayed higher.

If you want to display dress-up options in the menu, you also need to add settings to `descript.txt`; for an explanation of this, see the [Dress-up settings](bind.md) page.

## Writing surfaces.txt

First, create a text file named `surfaces.txt`.

This file is used to configure animations, image compositing, and hit detection for controlling characters with the mouse cursor.

Also refer to the page “[Shell settings - surfaces.txt](../descript/shell-surfaces/index.md)”.

After creating `surfaces.txt`, first copy the following to the top of the file.

```
charset,Shift_JIS

descript
{
version,1
}
```

The first line specifies the character encoding, just like in `descript.txt`. Unless you have a particular reason otherwise, Shift_JIS is fine.

The entries below that configure the format for setting up animations.

If this entry is missing, you must write animation-related definitions using the legacy format (SERIKO/1.x).

Note that the examples on this page use the new format (SERIKO/2.0).

!!! tip "Tip"

    If your surfaces.txt already uses the legacy format, you can convert it to the new format using the following tools.

    - [“SERIKO1to2.js” macro for Sakura Editor](http://gallnuts.webcrow.jp/etc/etc.shtml) ([archive](https://web.archive.org/web/20160621201301/http://gallnuts.webcrow.jp/etc/etc.shtml))

      Usage: Install [Sakura Editor](http://sakura-editor.sourceforge.net/) and use the macro. See the included readme.txt for details.

    - [Tool to convert surfaces.txt from the legacy format to the new format](http://typehoon.kusakage.com/zip/SurfacesTxtConverter.zip)

      Usage: Run the extracted .exe in the same folder as surfaces.txt.

### Writing surfaces.txt - Hit detection

Let's start by defining hit regions on a surface.

First, add the following to `surfaces.txt`.

```
surface0
{
}
```

This means that settings for surface0 are defined within these braces (\{\}).

This is where you will also write the animation and element settings covered later, not just hit detection.

Writing the following here defines hit regions.

```
surface0
{
collision0,117,71,185,130,Face
collision1,115,174,174,217,Bust
}
```

As above, write each hit region in sequence as collision0, collision1, collision2, and so on.

Make sure the numbers are unique within a single surface.

The maximum number of collisions per surface is 256.

The next four numbers specify coordinates.

With the top-left corner of the surface image as 0,0, they specify the rectangle's top-left x,y coordinates followed by its bottom-right x,y coordinates.

The final string is the name of the hit region used by the ghost.

You can define multiple hit regions with the same name (Face and Bust in the example above). For example, if you want the hands to have a hit region named Hand, the right and left hands will usually be in separate areas, so there will likely be two lines specifying Hand.

!!! tip "Tip"

    [Coordin](http://ukgk.s34.xrea.com/poskoma/#content_1_11) is a useful tool for getting hit-region coordinates.

    Drop an image into Coordin and drag to create a rectangular hit region.

    The coordinates are automatically copied to the clipboard, so paste them into the hit-region numbers.

!!! tip "Tip"

    In MATERIA, enable the development interface in the settings to view hit regions from the owner-draw menu.

    In SSP, enable developer features under “General” in Settings → Baseware Settings, open Tools → Developer Palette, and select Show hit regions to view them.

### Writing surfaces.txt - Animation

Animations in Ukagaka (called SERIKO) are expressed by drawing still images in sequence.

This section briefly introduces how to configure when animations run and how each still image is layered.

The following example explains animation by making surface0 blink.

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

To animate surface0.png, write surface0 like this, then define the animation within the braces (\{\}) below it.

```
animation0.interval,sometimes
```

A line of the form animation\*,interval defines when the animation with that number runs.

The number following “animation” is the ID of the animation definition (a set consisting of the timing setting interval and the following frame settings, such as pattern).

The animation ID can be any number and does not have to be sequential, but *the same ID is expected to be used for animations with the same meaning*[※](shell.md#surfacestxtを書く---アニメーション編).

The “sometimes” following animation0.interval, specifies the interval definition.

As in the example, if you specify sometimes, the animation runs automatically from time to time (with a probability of one half per second).

In other words, this specifies that “the animation with ID 0 runs automatically from time to time.”

For other timing options, see the section on [animation intervals](../descript/shell-surfaces/surface-brace/h-animationinterval/sometimes.md) in “Shell settings - surfaces.txt”.

Next, define each still image (frame) that makes up the animation.

Write them in sequence as pattern0, pattern1, pattern2, and so on. Pattern numbers cannot be skipped or duplicated.

Remember to include the ID of the same animation group (animation\*) at the start.

Also, write the interval definition and the series of pattern definitions together, rather than in separate places.

```
animation0.pattern0,overlay,100,50,0,0
```

The overlay part specifies the drawing method.

Overlay is a drawing method that displays an image over the original image.

Various other drawing methods are also available.

For details, see the section on [surface drawing methods](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md) in “Shell settings - surfaces.txt”.

```
animation0.pattern0,overlayfast,100,50,0,0
```

The 100 part means that surface100 is drawn for this frame.

In general, you can think of this as `surface100.png`.

If you specify 101, the image in `surface101.png` is used.

If you specify -1, drawing the animation stops and the display resets to the base image (surface0 in the example above).

```
animation0.pattern0,overlayfast,100,50,0,0
```

The 50 part is the display time (in milliseconds).

Specify the *time until it switches* to that frame.

Note that this is not the display time of the frame itself.

```
animation0.pattern0,overlayfast,100,50,0,0
```

The final 0,0 part specifies the frame's display position (x-coordinate, y-coordinate).

Specify how far to offset it from the original image.

For the x direction, right is positive; for the y direction, down is positive.

!!! note "Note"

    #### [※1](shell.md#surfacestxtを書く---アニメーション編)

    For example, suppose a character has a forward-facing pose on surface0 and a side-facing pose on surface5, and you want both to have a “blink” animation.

    In this case, in addition to defining the blink on surface0 as in the example above, you will define it in a similar way on surface5. However, because the side-facing and forward-facing poses differ, the surfaces (images) used as frames will be different.

    Since both are handled as the same “blink” animation, it is preferable to give them the same animation ID (for example, 0).

    This rule is particularly important for “[dress-up](bind.md),” which is explained in another section.

### Writing surfaces.txt - element compositing

element is a mechanism for combining multiple part images and treating them as a single surface.

For example, if every surface had to be prepared as an image such as surface0.png, adding more character expressions would require preparing a full-body standing image for each expression, even if only the shape of the mouth were slightly different.

However, if body parts and expression parts can be separated and composited, adding more expressions would only require preparing the expression variations as images, greatly reducing the overall shell size.

Furthermore, if the eye and mouth parts are separated, combining different eyes and mouths produces various expressions, making it possible to create a range of expressions without actually drawing each one.

Here is an example of an element definition.

```
surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face1.png,0,0
}
```

This defines a composite of “face1.png” over “body0.png” as surface1.

You can add as many parts as you want to composite.

In this case, surface1.png is not needed.

```
element0,overlay,body0.png,0,0
```

The number immediately following “element” is the element ID (serial number) on that surface.

IDs are consecutive numbers starting at 0. The smaller the number, the farther back on the screen the part is composited.

Note that png images with names such as surface\*.png are treated as parts below element0.

```
element0,overlay,body0.png,0,0
```

The following keyword is the drawing method.

It is basically [the same as for animations](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md), but some methods that do not simply composite images, such as start and move, cannot be used.

```
element0,overlay,body0.png,0,0
```

Next, specify the filename to composite.

You can specify a png file with any name.

```
element0,overlay,body0.png,0,0
```

The last two numbers specify the compositing position (x-coordinate, y-coordinate).

They specify how far to offset the image when compositing it over the base image.

The positive direction of the x-axis is right, and the positive direction of the y-axis is down.

In this example, unlike the examples for [hit testing](shell.md#surfacestxtを書く---当たり判定編) and [animations](shell.md#surfacestxtを書く---アニメーション編) mentioned earlier, the element definition is on surface1 rather than surface0.

This is only an example, but there is a reason for this choice[※](shell.md#surfacestxtを書く---element合成編).

There is no problem at all with using elements on surface0 or 10 when considering only the behavior of the shell (ghost) itself.

!!! note "Note"

    #### [※2](shell.md#surfacestxtを書く---element合成編)

    Consider a web service, such as a ghost database, that displays previews of ghosts.

    [As mentioned earlier](shell.md#立ち絵となる画像を用意する), surface0 and surface10 are considered basic surfaces and generally cannot be omitted.

    In other words, surface0 and 10 are assumed to always exist, making them convenient for use in previews.

    However, if surface0 or 10 is composed using element compositing, anyone displaying the preview will need to read the element definition and composite the parts as intended.

    This presents some obstacles, both for people doing it manually and for systems that automate the process with programs.

    Therefore, if you intend to use such services, it may be better to prepare surface0 and 10 as actual png files.

    One service that provides this kind of preview is the update feed “[SiReFaSo](https://sirefaso.appspot.com/) ([archive](https://web.archive.org/web/20170423052451/https://sirefaso.appspot.com/)).”

## Writing readme.txt

If a file named `readme.txt` is present, it can be displayed in places such as the owner-draw menu and during installation.

It can be omitted, but if the ghost author and shell author are different, for example, it may be a good idea to specify contact information.

Include any necessary information, such as a description of the shell or other notices.

As with other files, readme can use encodings other than Shift JIS if you specify something like charset,UTF-8 on the first line or include a BOM.

## About translucent surfaces

To make an image translucent, create a “pna” file with the same filename as the image to be made translucent.

For example, `surface0.png` would have a corresponding `surface0.pna`.

With SSP, you can also create pna files for parts used in [element compositing](shell.md#surfacestxtを書く---element合成編). For example, `face1.png` would have a corresponding `face1.pna`.

A pna file is simply a grayscale png that represents transparency, renamed with the pna extension.

Areas made completely white in the pna are opaque, areas made completely black are transparent, and the areas in between are translucent.

| ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
| --- | --- | --- | --- | --- |
| surface0.png |  | surface0.pna |  | Desktop display |

Translucent areas can be clicked as part of the character.

Therefore, make transparent areas completely black (RGB 0,0,0).

Also, in SSP, instead of using pna files, you can create `surface*.png` images as PNGs with an alpha channel and use that alpha channel for transparency.

In that case, you need to add the following entry to `descript.txt`.

```
seriko.use_self_alpha,1
```

For instructions on creating PNGs with an alpha channel, refer to the documentation for your paint software (some software may not support them. You can also search for terms such as PNG with transparency, 32-bit PNG, and αPNG).

## Network Updates for Additional Shells

SSP allows network update functionality to be added to the shell itself.

For details, see the page "[Support for Network Updates](update.md)".

## About Dress-Up

In Ukagaka, dress-up is configured as a type of animation.

For details, see the page "[Configuring Dress-Up](bind.md)".

## Grouping Shared Settings Across Multiple Surfaces

For example, if there are several surfaces with the same character pose, some of them may have exactly the same hit detection areas and animation settings.

In such cases, there are several convenient ways to specify settings besides repeatedly copying and pasting the same settings into each surface brace.

However, most of these methods are *SSP-specific*.

For details, see "[IDs Available in surface\* Braces](../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md)" on the "Shell Settings - surfaces.txt" page.

## Configuring the Owner-Draw Menu

You can also configure the background image, text color, and other settings for the owner-draw menu (right-click menu) in a shell.

For details, see "[Configuring the Owner-Draw Menu](ownerdraw.md)".

## Setting a Thumbnail Image

You can display a thumbnail image when the cursor is over a shell in the shell selection menu of the owner-draw menu.

This is useful when you have multiple shells and want to make them easy to distinguish at a glance.

If an image named `thumbnail.png` is in the same folder, it will be used automatically.
