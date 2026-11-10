# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数))]`

**カテゴリ:** 事件命令

將指定的圖示檔套用為通知區域（工作列通知區）的圖示。<br />
檔名可使用相對於\[執行中的ghost資料夾\]或\[執行中的ghost資料夾\]/ghost/master的路徑。<br />
文字會在滑鼠游標移到圖示上時顯示，可省略。預設為「SSP/Emily/Phase4.5」等，也就是SSP/\[啟動中的ghost名稱\]。<br />
指定--duration=等待時間(ms)後，即可讓圖示動畫播放。此時若指定檔名.ico，會依照檔名00.ico、檔名01.ico……等尾端數字的順序讀取多個圖示，並每隔指定的等待時間（毫秒）播放動畫。 \[SSP 2.5.58～\]<br />
另外指定--runcount後，即可設定動畫的重複次數。未指定時會無限重複。 \[SSP 2.5.59～\]

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```
