# descript.txt（shell 的）

## 概要

shell 的基本設定檔。<br />
除了 shell 名稱和作者資訊，也在此設定 balloon 的顯示位置、owner draw 選單（右鍵選單）的圖片，以及 dressup 在 owner draw 選單中的顯示方式等。

!!! note "也可寫在 ghost 的 descript.txt 中的項目"
    本頁標示為「也可寫在 ghost 的 descript.txt 中」的項目，也能以相同格式寫在 [ghost 的 `descript.txt`](../../ghost/descript-txt/index.md) 中。寫在 ghost 端的項目會成為所有 shell 共用的預設值；若 shell 的 `descript.txt` 中有相同項目，則優先使用 shell 端的設定（覆寫 ghost 端的設定）。

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

type、name 為必填項目。

在 SSP 中，也可為 shell 設定 homeurl，以便從檔案總管等工具進行 network update。

dressup 設定的各個項目請參閱後續各節。<br />
基本機制是為 [surfaces.txt](../../shell-surfaces/index.md) 中定義的 timing 為 bind 的 animationID 指定 dressup 名稱與 dressup 類別名稱（sakura(kero).bindgroup\*.name,～），並指定其在 owner draw 選單中的排列位置（sakura(kero).menuitem\*,～）。

此外，以 \\ 或 % 開頭的字串會被視為 Sakura Script 或環境變數的標籤，並因安全風險而遭到捨棄。若要將它們作為一般字元使用，必須以 \\\\ 或 \\% 等方式跳脫。
