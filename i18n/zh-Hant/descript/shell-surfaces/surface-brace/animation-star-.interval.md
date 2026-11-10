# animation\*.interval, interval

**カテゴリ:** surface brace

Defines the timing (cycle) at which an animation starts.<br />
For intervals, see [Animation intervals](h-animationinterval/index.md) below. SSP alone allows multiple intervals to be combined by listing them separated by +.<br />
The \* (animationID) can be any number. Across all surfaces within the scope (`\0`, `\1`, ...), animations with the same ID should have the same meaning (for example, “blinking,” “lip-sync,” or “changing into the same outfit”).<br />
The interval definition indicates the start of the entire animation definition for that ID and must always be written first in the series of animation definitions.<br />
For the relationship between animation overlap and ID order, see [animation-sort](../descript-brace/animation-sort.md).<br />
[Legacy definition](caption_seriko-redefine.md): \*interval, interval

**既定値:** No behavior

**対応:** Materia / SSP / CROW
