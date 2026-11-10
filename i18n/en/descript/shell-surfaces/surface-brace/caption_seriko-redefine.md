# SERIKO: Old and New Definitions

## What Are the New and Old SERIKO Definitions?

In a late version of the original Ukagaka (MATERIA), the format for SERIKO (animation) settings in surfaces.txt was changed.<br />
The conventional SERIKO/1.x format described in the [original specification](http://usada.sakura.vg/contents/seriko.html) is sometimes called the old definition, and the new format that was never officially documented (SERIKO/2.0) is sometimes called the new definition.

Separately from this, *entirely unrelated to this*, SSP and others added their own notations for the sufraces.txt format after MATERIA development ended (for example, surface.append and range specifications such as surface1-9).<br />
Some people or documents may include these in what they call the new definition, but note that at least in UKADOC, the terms new and old definition refer specifically to SERIKO formats, not to such usages.

## Differences Between the New and Old Definitions

The new definition has the following four format changes:

1. All [SERIKO-related definition lines](animation-star-.interval.md) now begin with the word "animation".
2. The parameter order in [pattern definition lines](animation-star-.pattern-star.md) has changed (the drawing method is now first).
3. The unit of the weight parameter in pattern definitions has changed from 10 milliseconds to 1 millisecond.
4. In the drawing method [alternativestart](h-drowmethod/alternativestart.md), the brackets for specifying IDs have changed from \[\] to ().

In addition, you must add a descript brace and define "[version,1](../descript-brace/version.md)".

The following examples show the old and new definitions for the *same definition*.

```
// 旧定義
surface1
{
0interval,rarely
0pattern0,0,0,alternativestart,[1,2]

1interval,never
1pattern0,101,70,overlay,200,100
1pattern1,102,70,overlay,200,100
1pattern2,101,70,overlay,200,100
1pattern3,-1,70,overlay,0,0

2interval,never
2pattern0,101,70,overlay,200,100
2pattern1,102,70,overlay,200,100
2pattern2,101,70,overlay,200,100
2pattern3,-1,70,overlay,0,0
2pattern4,101,70,overlay,200,100
2pattern5,102,70,overlay,200,100
2pattern6,101,70,overlay,0,0
2pattern7,-1,70,overlay,0,0
}
```

```
// 新定義
surface1
{
animation0.interval,rarely
animation0.pattern0,alternativestart,(1,2)

animation1.interval,never
animation1.pattern0,overlay,101,700,200,100
animation1.pattern1,overlay,102,700,200,100
animation1.pattern2,overlay,101,700,200,100
animation1.pattern3,overlay,-1,700,0,0

animation2.interval,never
animation2.pattern0,overlay,101,700,200,100
animation2.pattern1,overlay,102,700,200,100
animation2.pattern2,overlay,101,700,200,100
animation2.pattern3,overlay,-1,700,0,0
animation2.pattern4,overlay,101,700,200,100
animation2.pattern5,overlay,102,700,200,100
animation2.pattern6,overlay,101,700,200,100
animation2.pattern7,overlay,-1,700,0,0
}
```

- Animation ID
- Pattern ID
- Surface ID
- Drawing method
- Weight
- x coordinate
- y coordinate

Note that the lines now begin with "animation", the weight values are multiplied by 10, and the drawing method has moved to the beginning of the parameters.<br />
Also, for alternativestart, the brackets have changed from \[\] to (), and the parameters ignored in the case of alternativestart ("Surface ID" and "weight") can now be omitted entirely, including the "compositing position x,y", because the drawing method has moved to the beginning. In the old definition, dummy values of 0 were written for these parameters.

## Advantages of Using the New Definition

- Settings added independently by SSP (items on this page that show ![Materia](../../../assets/image/icon_m.png) without ![SSP](../../../assets/image/icon_s.png)) may not be expected to be written using the old definition.<br />
  The same may apply to any settings added in the future.<br />
  When using such settings, it is preferable to write them using the new definition (they may not work correctly with the old definition).<br />
  In this case, mixing the old and new definitions causes an error, so you must use the new definition consistently.
- The weight unit changes from 10 ms to 1 ms, allowing finer adjustments.
- Also, as seen in the example above, moving the drawing method to the beginning of the parameters may be an advantage because parameters ignored by special drawing methods such as start and alternativestart can be neatly omitted.
- Another possible advantage is that explicitly using the word "animation" emphasizes that the definition relates to SERIKO and makes the meaning of the line easier to understand. However, readability largely depends on familiarity and personal preference, and it is perfectly natural to find the old definition more familiar and easier to read.

If you do not consider the points above to be advantages, there may be no particular reason to migrate if you only intend to support SSP.

Note that UKADOC generally uses the new definition when describing SERIKO, so if you want to write definitions in the old format, refer to the above and convert them as appropriate.
