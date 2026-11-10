# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数))]`

**カテゴリ:** Event command

Apply the specified icon file to the notification area (task tray) icon.<br />
A relative path can be used from \[the folder of the running ghost\] or from \[the folder of the running ghost\]/ghost/master.<br />
The text, which is optional, is displayed when the mouse is placed over the icon. By default, it is something like "SSP/Emily/Phase4.5" or SSP/\[the name of the running ghost\].<br />
Specifying --duration=wait time (ms) allows the icon to be animated. In this case, specifying filename.ico loads multiple files in numerical order, such as filename00.ico, filename01.ico, and so on, and displays them as an animation at the specified interval (in milliseconds). \[SSP 2.5.58～\]<br />
Additionally, specifying --runcount sets the number of times the animation repeats. If unspecified, it repeats indefinitely. \[SSP 2.5.59～\]

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```
