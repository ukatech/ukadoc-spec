# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数)(,--interval=再生間隔))]`

**カテゴリ:** Event command

Applies the specified icon file to the notification area (task tray) icon.<br />
The file name can be a path relative to \[the executing ghost's folder\] or \[the executing ghost's folder\]/ghost/master.<br />
The optional text is displayed when the mouse hovers over the icon. The default is SSP/\[running ghost name\], such as "SSP/Emily/Phase4.5".<br />
Specifying --duration=delay (ms) animates the icon. When file name.ico is specified, multiple files are loaded in numeric order, such as file name00.ico, file name01.ico, and so on, and displayed in sequence at the specified delay in milliseconds. \[SSP 2.5.58 and later\]<br />
Specifying --runcount also sets the number of times the animation repeats. If unspecified, it repeats indefinitely. \[SSP 2.5.59 and later\]

## Specifying an animated image

In addition to .ico, the file name can specify an animated image (ANI, GIF, APNG, or WebP) or a still image (such as PNG). A single image file can animate the icon without a numbered sequence of .ico files. \[SSP 2.9.40 and later\]

- Animated images play according to the frame delays and loop count in the file. --duration is not required.
- Specifying --duration=delay (ms) overrides the delay for all frames with that value (minimum 50 milliseconds).
- Frame images are scaled down to the notification area icon size (16px square). Non-square images are centered while preserving their aspect ratio.
- As before, .ico files (including numbered sequences) animate only when --duration is specified.
- This feature is available only in SSP. Other baseware can only read .ico files.

## Playback

--interval=playback interval specifies when the animation plays (SSP only). The values are the same as the [animation intervals](../../../descript/shell-surfaces/surface-brace/h-animationinterval/introduction_animationinterval.md) in surfaces.txt. \[SSP 2.9.40 and later\]

| Playback interval | Behavior |
| --- | --- |
| always | Repeats indefinitely without stopping. Ignores the loop count in the file. |
| runonce | Plays once and stops. |
| runcount,N | Plays N times and stops. Equivalent to --runcount=N. |
| never | Does not play. Remains on the first frame. |
| rarely | Plays once with a 1 in 4 chance each second. |
| sometimes | Plays once with a 1 in 2 chance each second. |
| random,N | Plays once with a 1 in N chance each second. N defaults to 2. |
| periodic,N | Plays once every N seconds after playback ends. N defaults to 1. |

- In all cases, the animation stops on the last frame when playback ends, as with animations in surfaces.txt. random, periodic, rarely, and sometimes initially remain on the first frame and start from it each time they play. To return to the first image after playback, make the last frame identical to the first.
- If --interval is unspecified, --runcount is used if present; otherwise, the loop count in the file is used (ANI loops indefinitely; GIF stops after one play if it has no NETSCAPE extension). Numbered .ico sequences loop indefinitely.
- If both --interval and --runcount are specified, --interval takes precedence. However, with random, periodic, rarely, and sometimes, --runcount specifies the number of repetitions per playback (one if unspecified).
- Values can be separated by a comma, as in `--interval=random,5` (or written as `--interval=random:5`).
- The specified --duration, --runcount, and --interval are retained after the ghost is minimized and restored. To restore the default icon, leave the file name empty and execute `\![set,tasktrayicon,]`.

Icons specified by [icon](../../../descript/ghost/descript-txt/icon.md) and [icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md) in descript.txt can also be animated in the same way (playback is specified by [icon.interval](../../../descript/ghost/descript-txt/icon.interval.md) and [icon.minimize.interval](../../../descript/ghost/descript-txt/icon.minimize.interval.md)).

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```

```sakurascript
\![set,tasktrayicon,alert.gif,通知あり,--interval=periodic,10]アイコンを alert.gif のアニメーションにし、再生が終わるたびに10秒待ってからもう一度再生する。
```
