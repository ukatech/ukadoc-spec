# descript.txt（Balloon 的）

## 概要

氣球的基本設定檔。<br />
除了氣球名稱和作者資訊，也可設定零件的顯示位置及文字顯示相關項目。

descript.txt是氣球整體的標準設定，並以此設定為基礎，再透過各氣球表面的個別設定檔[balloon(s/k)\*s.txt](../balloonsoption/index.md)進行調整。

## 記述例與基本寫法

```
charset,Shift_JIS
type,balloon
name,凡例さんの吹き出し
homeurl,http://ssp.shillest.net/ukadoc/manual/hogehoge/example/

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

origin.x,14
origin.y,14

validrect.left,0
validrect.top,0
validrect.right,0
validrect.bottom,-12

wordwrappoint.x,-20

font.color.r,0
font.color.g,0
font.color.b,0

cursor.blendmethod,mergepennot
cursor.style,square
cursor.brush.color.r,0
cursor.brush.color.g,127
cursor.brush.color.b,127
cursor.pen.color.r,0
cursor.pen.color.g,0
cursor.pen.color.b,0
cursor.font.color.r,0
cursor.font.color.g,0
cursor.font.color.b,0

arrow0.x,296
arrow0.y,8
arrow1.x,296
arrow1.y,-18

onlinemarker.x,16
onlinemarker.y,-27

sstpmarker.x,16
sstpmarker.y,-20
sstpmessage.x,28
sstpmessage.y,-21
sstpmessage.font.name,ＭＳ ゴシック
sstpmessage.font.height,7
number.font.name,Arial
number.font.height,10
number.font.color.r,0
number.font.color.g,0
number.font.color.b,0
number.xr,-28
number.y,-24

communicatebox.x,8
communicatebox.y,21
communicatebox.width,385
communicatebox.height,20
```

即使與 ghost 或 shell 的 descript.txt 相比，這個檔案也有許多項目在規格上或實際使用上都必須設定。

在 SSP 中，只要也為氣球設定 homeurl，就能從檔案總管等位置執行網路更新。

另外，以 \\ 或 % 開頭的字串會被視為 Sakura Script 或環境變數標籤，並基於安全風險而遭到丟棄。若要將這些字元作為一般文字使用，必須以 \\\\ 或 \\% 等方式逸出。
