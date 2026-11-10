# descript.txt（Shell）

## 概要

Shell 的基本設定檔。<br />
除了 Shell 名稱和作者資訊，也可在此設定 balloon 的顯示位置、owner draw 選單（右鍵選單）的圖片，以及 dressup 在 owner draw 選單中的顯示方式。

## 記述例 與基本寫法

```
charset,Shift_JIS
type,shell
name,master

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

menu.background.bitmap.filename,menu_background.png
menu.foreground.bitmap.filename,menu_foreground.png
menu.sidebar.bitmap.filename,menu_sidebar.png

sakura.balloon.offsetx,0
sakura.balloon.offsety,80
kero.balloon.offsetx,-20
kero.balloon.offsety,10
sakura.balloon.alignment,none
kero.balloon.alignment,none

sakura.bindgroup0.name,服,エプロンドレス,apron
sakura.bindgroup1.name,リボン,白リボン,ribbonwhite
sakura.bindgroup2.name,服,黒服,black
sakura.bindgroup3.name,リボン,黒リボン,ribbonblack
sakura.bindgroup0.default,1
sakura.bindgroup1.default,1

kero.bindgroup0.name,ネクタイ,ネクタイ
kero.bindgroup1.name,腕章,黒腕章
kero.bindgroup2.name,腕,ドリル
kero.bindgroup0.default,1
kero.bindgroup1.default,1

sakura.menuitem0,2
sakura.menuitem1,3
sakura.menuitem2,-
sakura.menuitem3,0
sakura.menuitem4,1

kero.menuitem0,0
kero.menuitem1,1
kero.menuitem2,-
kero.menuitem3,2
```

type、name為必填項目。

在 SSP 中，只要也為 shell 設定 homeurl，就能從檔案總管等位置執行 network update。

各項 dressup 設定請參閱後續的各節。<br />
基本機制是，針對在[surfaces.txt](../../shell-surfaces/index.md)中定義的 timing bind animationID，設定 dressup 名稱和 dressup 類別名稱（sakura(kero).bindgroup\*.name,～），並指定其在 owner draw 選單中的位置（sakura(kero).menuitem\*,～）。

另外，以 \\ 或 % 開頭的字串會被視為 Sakura Script 或環境變數的標籤，基於安全性風險會被捨棄。若要將這些字元當作一般文字使用，必須以 \\\\ 或 \\% 等方式逸出。
