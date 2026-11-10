# surfaces.txt

## 概要

用于定义 shell 各项内容的文件。原则上所有项目都可以省略，只需编写必要的内容。<br />
例如，各个 surface（表情、部件、帧、dressup 部件）的动画、碰撞判定、图像合成等设置都在此处进行。<br />
此外，也可以在此处为 surface ID 设置别名。<br />
在 SSP 中，还可以设置光标持续悬停在碰撞判定区域时显示的工具提示，以及更改光标显示等内容。

另一方面，shell 名称、shell 作者名等 shell 基本信息的设置，以及 dressup 的 owner draw 菜单（右键菜单）显示设置等，不是在此处，而是在 [descript.txt](../shell/index.md) 中进行，请注意。

## 基本格式

原则上，大多数设置都*可以省略*，根据需要进行设置即可。

设置内容应分别写在由「\{」和「\}」括起来的各个块中；但 [charset](file/charset.md) 必须写在第一行（如需设置）。（各个块请参阅本页中的相应项目。）

「\{」和「\}」必须各自单独占一行，例如不能像「surface1 \{」这样接在块名后面书写。

```
ブレス名
{
// 設定内容
}
```

无法识别为块名、\{\} 或设置内容的行，都会被视为注释行。通常以「//」作为行首。

各行可以缩进。

仅 SSP 会读取所有名为「surfaces\*\*\*.txt（\*\*\*为任意字符串）」的文本文件，并将其与 surfaces.txt 同等处理。如果有多个待读取文件，则按文件名顺序读取。

另外，如果准备了多个 surfaces\*\*\*.txt，则每个文件都需要设置 [descript 块](descript-brace/introduction_descriptbrace.md)（以及 [charset](file/charset.md)）（也就是说，各个文件可以使用不同的设置）。

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
