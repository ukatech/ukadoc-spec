# animation\*.interval, interval

**カテゴリ:** surface brace

Defines when an animation starts (its interval).<br />
For intervals, see [Animation Intervals](h-animationinterval/index.md) below. SSP-only: multiple intervals can be combined by listing them separated by +.<br />
The \* (animationID) can be any number. For all surfaces within that scope (`\0`, `\1`, ...), animations with the same ID should have the same meaning (for example, “blinking,” “lip-sync,” or “changing into the same outfit”).<br />
The interval definition marks the beginning of the entire animation definition for that ID, and must always be written first in the series of animation definitions.<br />
For the relationship between animation overlap and ID order, see [animation-sort](../descript-brace/animation-sort.md).<br />
[Old definition](caption_seriko-redefine.md): \*interval, interval

**既定値:** No behavior

**対応:** Materia / SSP / CROW
