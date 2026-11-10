# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数))]`

**カテゴリ:** 事件命令

将指定的图标文件应用为通知区域（系统托盘）图标。<br />
文件名可使用相对于\[运行中的 ghost 文件夹\]或\[运行中的 ghost 文件夹\]/ghost/master的路径。<br />
文本是鼠标悬停在图标上时显示的内容，可省略。默认值为「SSP/Emily/Phase4.5」等形式的 SSP/\[运行中的 ghost 名称\]。<br />
指定 --duration=等待时间(ms) 后，可使图标动画显示。此时指定文件名.ico，会按末尾数字的顺序加载多个文件，如文件名00.ico、文件名01.ico……，并按指定的等待时间（毫秒）间隔显示动画。\[SSP 2.5.58～\]<br />
此外，指定 --runcount 可设置动画的重复次数。未指定时将无限重复。\[SSP 2.5.59～\]

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```
