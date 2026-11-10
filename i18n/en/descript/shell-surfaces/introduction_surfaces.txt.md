# surfaces.txt

## Overview

A file for defining various aspects of a shell. In general, all settings are optional; specify only what you need.<br />
For example, this is where you configure animations for each surface (expressions, parts, cels, dressup parts), hit regions, and image compositing.<br />
You can also use this file to assign aliases to surface IDs.<br />
In SSP, you can additionally configure tooltips displayed when the cursor remains over a hit region, as well as cursor changes.

Note that settings for basic shell information, such as the shell name and shell author's name, and settings for displaying the dressup owner draw menu (right-click menu) are configured in [descript.txt](../shell/index.md), not here.

## Basic format

Nearly all settings are *optional*; configure them as needed.

Settings are written inside braces, each enclosed by "\{" and "\}", except for [charset](file/charset.md), which must be written on the first line if used (see the respective sections on this page for details about each brace).

"\{" and "\}" must each appear alone on a line; for example, you cannot place them after a brace name as in "surface1 \{".

```
ブレス名
{
// 設定内容
}
```

Lines that are not recognized as a brace name, \{\}, or a setting are treated as comments. By convention, comment lines begin with "//".

Indentation is allowed on each line.

In SSP only, all text files named "surfaces\*\*\*.txt" (where \*\*\* is any string) are loaded and treated the same as surfaces.txt. If multiple files are to be loaded, they are loaded in filename order.

When providing multiple surfaces\*\*\*.txt files, the settings in the [descript brace](descript-brace/introduction_descriptbrace.md) (and [charset](file/charset.md)) must be specified in each file (in other words, you can use different settings in each file).

## 記述例

```
charset,Shift_JIS

descript
{
version,1
}

surface0
{
animation0.interval,sometimes
animation0.pattern0,overlay,101,100,168,67
animation0.pattern1,overlay,100,100,168,67
animation0.pattern2,overlay,101,100,168,67
animation0.pattern3,overlay,-1,100,168,67
}

surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face1.png,0,0
}

surface10
{
collision0,40,56,95,90,Head

sakura.balloon.offsetx,80
sakura.balloon.offsety,-100
kero.balloon.offsetx,-30
kero.balloon.offsety,20
}

// SSPのみで有効な記法 ←このようにコメント行は//から始める
surface.append0-9
{
collision0,188,25,252,63,Head
collision1,190,92,236,118,Face
collision2,180,191,220,222,Bust
collision3,154,311,248,362,Skirt
}
```
