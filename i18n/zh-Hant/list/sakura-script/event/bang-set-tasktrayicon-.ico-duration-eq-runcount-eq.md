# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数)(,--interval=再生間隔))]`

**カテゴリ:** 事件指令

將指定的圖示檔案套用至通知區域（系統匣）的圖示。<br />
檔案名稱可使用相對於\[執行該指令的 ghost 資料夾\]或\[執行該指令的 ghost 資料夾\]/ghost/master 的路徑。<br />
文字是在滑鼠移至圖示上時顯示的內容，可省略。預設為「SSP/Emily/Phase4.5」等 SSP/\[執行中的 ghost 名稱\]。<br />
指定 --duration=等待時間(ms) 後，即可讓圖示播放動畫。此時若指定ファイル名.ico，會依末尾數字的順序讀取ファイル名00.ico、ファイル名01.ico…等多個檔案，並依指定的等待時間（毫秒）間隔顯示動畫。 \[SSP 2.5.58～\]<br />
進一步指定 --runcount 可設定動畫的重複次數。未指定時會無限重複。 \[SSP 2.5.59～\]

## 指定動畫圖片

除了 .ico，檔案名稱也可指定動畫圖片（ANI、GIF、APNG、WebP）或靜態圖片（PNG 等）。不必準備連號的 .ico，單一圖片檔案即可播放動畫。 \[SSP 2.9.40～\]

- 動畫圖片會依檔案中各影格的等待時間和迴圈次數播放，不需要 --duration。
- 指定 --duration=等待時間(ms) 後，會以該值覆寫所有影格的等待時間（下限為 50 毫秒）。
- 影格圖片會縮小至通知區域的圖示大小使用（顯示縮放比例為 100% 時為 16px 見方、150% 時為 24px 見方、200% 時為 32px 見方。顯示縮放比例變更時，會以新尺寸重新產生）。非正方形圖片會保持比例置中顯示。
- .ico（包含連號檔案）與以往相同，只有指定 --duration 時才會播放動畫。
- 此設定僅適用於 SSP，其他 baseware 只能讀取 .ico。

## 播放方式

可透過 --interval=播放間隔 指定動畫的播放時機（僅限 SSP）。使用的詞彙與 surfaces.txt 的[動畫間隔](../../../descript/shell-surfaces/surface-brace/h-animationinterval/introduction_animationinterval.md)相同。 \[SSP 2.9.40～\]

| 播放間隔 | 動作 |
| --- | --- |
| always | 不停止地無限重複，忽略檔案內的迴圈次數。 |
| runonce | 播放一次後停止。 |
| runcount,N | 播放 N 次後停止，與 --runcount=N 相同。 |
| never | 不播放，停在第一個影格。 |
| rarely | 每秒有四分之一的機率播放一次。 |
| sometimes | 每秒有二分之一的機率播放一次。 |
| random,N | 每秒有 N 分之一的機率播放一次。省略 N 時為 2。 |
| periodic,N | 播放結束後，每隔 N 秒播放一次。省略 N 時為 1。 |

- 所有模式在播放結束後都會停在最後一個影格（與 surfaces.txt 的動畫相同）。random、periodic、rarely、sometimes 一開始停在第一個影格，每次播放都從第一個影格開始。若要在播放後回到第一張圖片，請將最後一個影格設為與第一個影格相同的圖片。
- 未指定 --interval 時，若有 --runcount 則依其設定，否則依檔案內的迴圈次數播放（ANI 為無限；GIF 若沒有 NETSCAPE 擴充則播放一次後停止）。連號的 .ico 為無限。
- 同時指定 --interval 和 --runcount 時，以 --interval 為優先。但 random、periodic、rarely、sometimes 會使用 --runcount 作為每次播放的重複次數（未指定時為 1 次）。
- 可使用逗號分隔，例如 `--interval=random,5`（也可寫成 `--interval=random:5`）。
- 指定的 --duration、--runcount、--interval 在 ghost 最小化及還原後仍會保留。要將圖示還原為預設值時，請將檔案名稱留空並執行 `\![set,tasktrayicon,]`（文字不會還原）。若要連文字一併還原，請使用下方的 `--reset`。

## 取消所有設定（--reset）

如 `\![set,tasktrayicon,--reset]` 所示，以 --reset 取代檔案名稱，即可取消此標籤指定的所有設定，還原為 descript.txt 的設定。 \[SSP 2.9.40～\]

- 檔案名稱、文字、--duration、--runcount、--interval 都會取消。
- 圖示會還原為 descript.txt 的 [icon](../../../descript/ghost/descript-txt/icon.md)（最小化時為 [icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md)），文字則還原為預設的「SSP/\[執行中的 ghost 名稱\]」（最小化時為「SSP\[Minimize\]/\[執行中的 ghost 名稱\]」）。
- --reset 之後的引數會被忽略。
- 將檔案名稱留空的 `\![set,tasktrayicon,]` 只會還原圖示，此標籤指定的文字會維持不變。

descript.txt 的 [icon](../../../descript/ghost/descript-txt/icon.md)、[icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md) 指定的圖示也能以相同方式播放動畫（播放方式由 [icon.interval](../../../descript/ghost/descript-txt/icon.interval.md)、[icon.minimize.interval](../../../descript/ghost/descript-txt/icon.minimize.interval.md) 指定）。

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
