# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数))]`

**カテゴリ:** Event command

Applies the specified icon file as the notification area (taskbar tray) icon.<br />
The file name can be a relative path from \[the running ghost's folder\] or from \[the running ghost's folder\]/ghost/master.<br />
The text is displayed when the mouse is over the icon; this is optional. By default, it is something like "SSP/Emily/Phase4.5" or SSP/\[the name of the running ghost\].<br />
Specifying --duration=wait time(ms) animates the icon. In this case, specifying filename.ico loads multiple files in order of the numbers at the end, such as filename00.ico, filename01.ico…, and displays them as an animation at the specified interval (in milliseconds). \[SSP 2.5.58～\]<br />
Additionally, specifying --runcount sets the number of times the animation repeats. If not specified, it repeats indefinitely. \[SSP 2.5.59～\]

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```
