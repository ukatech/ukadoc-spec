# Dressup settings

## Dressup

Ukagaka shells can have *dressup* features (for an explanation of dressup itself, see “[Dressup (MAYUNA)](../descript/shell-surfaces/surface-brace/introduction_mayuna.md)” in “Shell settings - surfaces.txt”).

Dressup lets users switch parts of a character’s appearance on or off within a single shell when selected from the owner draw menu.

In SSP, dressup can also be switched using [Sakura Script commands](../list/sakura-script/surface/bang-bind.md).

Dressup is supported only by MATERIA and SSP; in CROW, only the initial dressup layout is displayed.

However, due to a bug in MATERIA, the dressup menu is displayed only for the `\0` side.

Therefore, in practice, only SSP has a complete implementation, including `\1` and later.

This page assumes some familiarity with animation settings.

For information on animation settings, see the “[Writing surfaces.txt - Animation](shell.md#surfacestxtを書く---アニメーション編)” section of “Creating a shell.”

## 目次

1. [Settings in surfaces.txt](bind.md#surfacestxtでの設定)
2. [Settings in descript.txt](bind.md#descripttxtでの設定)

1. (In preparation) Various settings for SSP's dressup menu
2. (In preparation) Dressup with movement
3. (In preparation) A three-dimensional structure where one dressup overlaps another dressup in front or behind

## Settings in surfaces.txt

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

As shown above, an animation with bind specified for interval becomes a dressup.

Drawing methods such as add and reduce are described later.

The wait value is set to 0, but when configuring an animation whose interval is bind (that is, a dressup), any wait value specified is ignored.

The X and Y coordinate offsets can be specified in the same way as for ordinary animation patterns.

Also, the number “0” in animation0 is the animation ID, but this ID is particularly important for dressup.

### About dressup drawing methods

In the original Ukagaka, dressup was generally handled using four methods: bind, add, reduce, and insert.

In SSP, methods such as base, overlay, overlayfast, replace, interpolate, and asis can also be used, as with regular animations.

However, methods that do not simply composite images, such as start, stop, and move, cannot be used.

## Settings in descript.txt

In short, the settings in descript.txt prepare dressup items to appear in the dressup menu of the owner-draw menu.

Write it as follows.

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

With the settings above, “Apron Dress,” “Black Clothes,” “White Ribbon,” and “Black Ribbon” will appear in the main character's dressup menu,

and “Necktie,” “Armband,” and “Arm” will appear in the partner's menu, allowing you to freely put them on and take them off.

Write ?.bindgroup\* as a comma-separated list of the category name, part name, and thumbnail filename, in that order.

The number in the \* of “bindgroup\*” corresponds to the dressup animation ID set in surfaces.txt.

Note that the same animation ID must be assigned to the same outfit (dressup) across all surfaces.

?.bindgroup\*.default sets the dressup with animation ID “\*” as the initial dressup setting for that shell.

With the settings in the example above, the default will be Apron Dress and White Ribbon, and Necktie and Black Armband.

Specifying 0 or omitting it turns dressup OFF.

?.menuitem\*,\* represents the structure of menu items.

Assign numbers in menu display order, then specify the number corresponding to the \* in bindgroup\*, separated by commas (note that this is not an animation ID).

Writing “-” instead of a bindgroupID displays a separator (a dividing line) at that position in the menu.

In the example above, the shell dressup menu displays, from top to bottom: black clothes, black ribbon, (separator), apron dress, and white ribbon.

Thumbnails are displayed as a guide when selecting a menu item.

You can omit them if they are not needed, but they are useful when there are many dressups or when it is difficult to infer what a dressup looks like from its name.

## SSP dressup menu settings

In preparation

## Animated dressups

In preparation

## When the three-dimensional structure of one dressup spans before and after another dressup

In preparation
