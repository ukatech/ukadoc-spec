# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数)(,--interval=再生間隔))]`

**カテゴリ:** Event command

Applies the specified icon file to the notification area (task tray) icon.<br />
The filename can be a path relative to \[the executing ghost's folder\] or \[the executing ghost's folder\]/ghost/master.<br />
The text is displayed when the mouse hovers over the icon and may be omitted. By default, it is SSP/\[running ghost name\], such as "SSP/Emily/Phase4.5".<br />
Specifying --duration=wait time (ms) allows the icon to be animated. When filename.ico is specified, multiple files are loaded in numerical order, such as filename00.ico, filename01.ico, and so on, and displayed as an animation at the specified wait time (milliseconds). \[SSP 2.5.58 onward\]<br />
Additionally, --runcount can be specified to set the number of animation repetitions. If omitted, the animation repeats indefinitely. \[SSP 2.5.59 onward\]

## Specifying animated images

In addition to .ico, the filename can specify an animated image (ANI, GIF, APNG, or WebP) or a static image (such as PNG). A single image file can provide animation without preparing numbered .ico files. \[SSP 2.9.40 onward\]

- Animated images play according to the frame delays and loop count stored in the file. --duration is not required.
- Specifying --duration=wait time (ms) overrides the delay of every frame with that value (minimum 50 milliseconds).
- Frames are scaled down to the notification area icon size (16px square at 100% display scaling, 24px square at 150%, and 32px square at 200%; they are recreated at the new size when display scaling changes). Non-square images are centered while preserving their aspect ratio.
- As before, .ico files (including numbered sequences) animate only when --duration is specified.
- This option is available only in SSP. Other baseware can only read .ico files.

## Playback

--interval=playback interval specifies when the animation plays (SSP only). The values are the same as the [animation intervals](../../../descript/shell-surfaces/surface-brace/h-animationinterval/introduction_animationinterval.md) in surfaces.txt. \[SSP 2.9.40 onward\]

| Playback interval | Behavior |
| --- | --- |
| always | Repeats indefinitely without stopping. Ignores the loop count stored in the file. |
| runonce | Plays once and stops. |
| runcount,N | Plays N times and stops. Equivalent to --runcount=N. |
| never | Does not play. Remains on the first frame. |
| rarely | Plays once with a 1 in 4 chance each second. |
| sometimes | Plays once with a 1 in 2 chance each second. |
| random,N | Plays once with a 1 in N chance each second. N defaults to 2. |
| periodic,N | Plays once every N seconds after playback ends. N defaults to 1. |

- All modes stop on the last frame when playback ends (as with animations in surfaces.txt). random, periodic, rarely, and sometimes initially remain on the first frame and start from the first frame each time they play. To return to the initial image after playback, make the last frame identical to the first.
- If --interval is not specified, --runcount is used if present; otherwise, the loop count stored in the file is used (ANI loops indefinitely; GIF stops after one play if it has no NETSCAPE extension). Numbered .ico files loop indefinitely.
- If both --interval and --runcount are specified, --interval takes precedence. However, with random, periodic, rarely, and sometimes, --runcount specifies the number of repetitions per playback (defaulting to 1).
- Values can be separated by a comma, as in `--interval=random,5` (or written as `--interval=random:5`).
- The specified --duration, --runcount, and --interval are retained after the ghost is minimized and restored. To restore the default icon, leave the filename empty and execute `\![set,tasktrayicon,]` (the text is not restored). To restore the text as well, use `--reset` below.

## Canceling all settings (--reset)

Writing --reset in place of the filename, as in `\![set,tasktrayicon,--reset]`, cancels all settings specified by this tag and restores the settings in descript.txt. \[SSP 2.9.40 onward\]

- The filename, text, --duration, --runcount, and --interval settings are canceled.
- The icon reverts to [icon](../../../descript/ghost/descript-txt/icon.md) in descript.txt ([icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md) while minimized), and the text reverts to the default "SSP/\[running ghost name\]" ("SSP\[Minimize\]/\[running ghost name\]" while minimized).
- Arguments written after --reset are ignored.
- `\![set,tasktrayicon,]` with an empty filename restores only the icon; the text specified by this tag remains unchanged.

Icons specified by [icon](../../../descript/ghost/descript-txt/icon.md) and [icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md) in descript.txt can also be animated in the same way (playback is specified by [icon.interval](../../../descript/ghost/descript-txt/icon.interval.md) and [icon.minimize.interval](../../../descript/ghost/descript-txt/icon.minimize.interval.md)).

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```

```sakurascript
\![set,tasktrayicon,alert.gif,通知あり,--interval=periodic,10]アイコンを alert.gif のアニメーションにし、再生が終わるたびに10秒待ってからもう一度再生する。
```

```sakurascript
\![set,tasktrayicon,--reset]このタグで指定したアイコンとテキストをすべて取り消して、descript.txtの指定に戻す。
```
