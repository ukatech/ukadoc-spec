# animation\*.interval, interval

**カテゴリ:** surface brace

Defines when an animation starts (its cycle).<br />
See [animation intervals](h-animationinterval/index.md) below for intervals. SSP alone allows combinations to be specified by listing them separated by +.<br />
The \* (animationID) can be any number. Across all surfaces in that scope (`\0`, `\1`, ...), animations with the same ID should have the same meaning (for example, “blinking,” “lip-sync,” or “changing into the same outfit”).<br />
The interval definition indicates the starting point of all animation definitions for that ID, and must always be written first in the sequence of animation definitions.<br />
See [animation-sort](../descript-brace/animation-sort.md) for the relationship between animation overlap and ID order.<br />
[Legacy definition](caption_seriko-redefine.md): \*interval, interval

**既定値:** No effect

**対応:** Materia / SSP / CROW
