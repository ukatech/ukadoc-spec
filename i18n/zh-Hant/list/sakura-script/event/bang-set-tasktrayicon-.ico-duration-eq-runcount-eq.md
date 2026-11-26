# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数)(,--interval=再生間隔))]`

**カテゴリ:** 事件指令

將指定的圖示檔案套用為通知區域（系統匣）的圖示。<br />
檔案名稱可使用相對於\[執行此指令的 ghost 資料夾\]或\[執行此指令的 ghost 資料夾\]/ghost/master 的路徑。<br />
文字會在滑鼠移至圖示上時顯示，可省略。預設為「SSP/Emily/Phase4.5」等，即 SSP/\[執行中的 ghost 名稱\]。<br />
指定 --duration=等待時間(ms) 可使圖示播放動畫。此時，若指定檔案名稱.ico，會依照檔案名稱00.ico・檔案名稱01.ico…等結尾的數字順序讀取多個檔案，並以指定的等待時間（毫秒）間隔播放動畫。 \[SSP 2.5.58～\]<br />
再指定 --runcount 可設定動畫的重複次數。未指定時會無限重複。 \[SSP 2.5.59～\]

## 指定動畫圖片

檔案名稱除了 .ico，還可指定動畫圖片（ANI・GIF・APNG・WebP）或靜態圖片（如 PNG）。不需準備連號的 .ico，僅用一個圖片檔案即可播放動畫。 \[SSP 2.9.40～\]

- 動畫圖片依照檔案中各影格的等待時間和循環次數播放。不需要 --duration。
- 指定 --duration=等待時間(ms) 時，會以該值覆寫所有影格的等待時間（下限為50毫秒）。
- 影格圖片會縮小至通知區域圖示的大小（16px 正方形）後使用。非正方形的圖片會保持比例置中。
- .ico（包含連號檔案）與以往相同，僅在指定 --duration 時播放動畫。
- 此功能僅適用於 SSP。其他 baseware 只能讀取 .ico。

## 播放方式

可透過 --interval=播放間隔 指定動畫的播放時機（僅限 SSP）。可用的值與 surfaces.txt 的[動畫間隔](../../../descript/shell-surfaces/surface-brace/h-animationinterval/introduction_animationinterval.md)相同。 \[SSP 2.9.40～\]

| 播放間隔 | 動作 |
| --- | --- |
| always | 不停止，無限重複。忽略檔案所含的循環次數。 |
| runonce | 播放1次後停止。 |
| runcount,N | 播放 N 次後停止。與 --runcount=N 相同。 |
| never | 不播放。停在第1格。 |
| rarely | 每秒以四分之一的機率播放1次。 |
| sometimes | 每秒以二分之一的機率播放1次。 |
| random,N | 每秒以 N 分之一的機率播放1次。省略 N 時為2。 |
| periodic,N | 播放結束後，每隔 N 秒播放1次。省略 N 時為1。 |

- 所有模式播放結束後都會停在最後一格（與 surfaces.txt 的動畫相同）。random・periodic・rarely・sometimes 一開始停在第1格，每次播放都從第1格開始。若要在播放後回到開頭的圖片，請將最後一格設為與開頭相同的圖片。
- 未指定 --interval 時，若有指定 --runcount，則遵循該值；否則遵循檔案所含的循環次數（ANI 為無限次；GIF 若沒有 NETSCAPE 擴充，則播放1次後停止）。連號的 .ico 為無限次。
- 同時指定 --interval 和 --runcount 時，以 --interval 為優先。不過在 random・periodic・rarely・sometimes 中，--runcount 會作為每次播放的重複次數（未指定時為1次）。
- 可用逗號分隔，例如 `--interval=random,5`（也可寫成 `--interval=random:5`）。
- 指定的 --duration・--runcount・--interval 在 ghost 最小化及還原後仍會保留。若要將圖示還原為預設值，請將檔案名稱留空並執行 `\![set,tasktrayicon,]`。

descript.txt 的[icon](../../../descript/ghost/descript-txt/icon.md)・[icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md)指定的圖示也可同樣播放動畫（播放方式由[icon.interval](../../../descript/ghost/descript-txt/icon.interval.md)・[icon.minimize.interval](../../../descript/ghost/descript-txt/icon.minimize.interval.md)指定）。

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```

```sakurascript
\![set,tasktrayicon,alert.gif,通知あり,--interval=periodic,10]アイコンを alert.gif のアニメーションにし、再生が終わるたびに10秒待ってからもう一度再生する。
```
