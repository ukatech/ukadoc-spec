# icon.interval,Playback interval

**カテゴリ:** descript.txt

The timing of the animation in the animated image (ANI, GIF, APNG, or WebP) specified by [icon](icon.md).
The allowed values are the same as for --interval in [\![set,tasktrayicon]](../../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md) (always, runonce, runcount,N, never, rarely, sometimes, random,N, or periodic,N). In descript.txt, write them directly, as in `icon.interval,random,5`.

If unspecified, the loop count in the file is used. When playback ends, the animation stops on the last frame.
This does not apply to icons specified by the tag (`\![set,tasktrayicon]`); only the tag's --interval is used.

**既定値:** No value (uses the loop count in the file)

**対応:** SSP 2.9.40
