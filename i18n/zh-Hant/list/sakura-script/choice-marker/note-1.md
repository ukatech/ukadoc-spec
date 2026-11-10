# 補充

## 形状指定の方法

- **square**: 顯示矩形。
- **underline**: 顯示底線。
- **square+underline**: 顯示矩形和底線。
- **none**: 不顯示。
- **default**: 恢復為 balloon 設定的預設值。

## 文字色指定の方法

基本上與 HTML、CSS 的色彩表示法相似。<br />
\[2.8.93\] 不符合以下任何一種格式的值（例如 R、G、B 不是數值，或色碼包含非十六進位字元）會被忽略。過去有時會將其視為黑色。

- **R,G,B**: 以 0～255 的十進位數值分別表示紅、綠、藍三原色的亮度，並以逗號分隔。<br />
  0,0,0 為黑色，255,255,255 為白色。
- **R%,G%,B%**: 以 0～100% 的百分比值分別表示紅、綠、藍三原色的亮度，並以逗號分隔。<br />
  0%,0%,0% 為黑色，100%,100%,100% 為白色。
- **十六進位色碼**: 如 #07f，將紅、綠、藍三原色的亮度接在「#」後，以*十六進位*表示。<br />
  可用紅、綠、藍各 2 位共 6 位，或各 1 位共 3 位表示。<br />
  十六進位字母可使用大寫或小寫。<br />
  #000000 或 #000 為黑色，#ffffff 或 #fff 為白色。
- **預先定義的關鍵字**: 可使用表示色名的關鍵字（全小寫）指定，例如 red、white、black。<br />
  對於 X11 color 與 W3C color 定義不同的顏色（例如 green、gray），採用 W3C color 的定義。<br />
  色彩範例：[CSS Color Module Level 3 Extended color keywords](http://www.w3.org/TR/css3-color/#svg-color)（外部連結）
- **default**: 在顏色指定部分填入 default，會將指定文字還原為該文字的預設顏色。<br />
  預設顏色包括 balloon 的 descript.txt 中定義的顏色（未定義時為黑色）。
- **disable**: 在顏色指定部分填入 disable，可將顏色設為停用狀態的顯示色。
- **default.anchor**: 在顏色指定部分指定 default.anchor，會將指定文字的顏色改為選取時錨點的預設文字顏色。<br />
  \[2.5.76 - 可用於一般字串\]
- **default.anchornotselect**: 在顏色指定部分指定 default.anchornotselect，會將指定文字的顏色改為未選取時錨點的預設文字顏色。<br />
  \[2.5.76 - 可用於一般字串\]
- **default.anchorvisited**: 在顏色指定部分指定 default.anchorvisited，會將指定文字的顏色改為已造訪錨點的預設文字顏色。<br />
  \[2.5.76 - 可用於一般字串\]
- **default.cursor**: *※僅可指定選項或錨點的文字顏色*。<br />
  在顏色指定部分指定 default.cursor，會將指定文字的顏色改為選取時選項的預設文字顏色。
- **default.cursornotselect**: *※僅可指定選項或錨點的文字顏色*。<br />
  在顏色指定部分指定 default.anchor，會將指定文字的顏色改為未選取時選項的預設文字顏色。
- **default.plain**: *※僅可指定選項或錨點的文字顏色*。<br />
  在顏色指定部分指定 default.plain，會將指定文字的顏色改為一般文字的預設文字顏色。
