# 設定オーナードローメニュー

本文說明如何設定オーナードローメニュー（右鍵選單）的顯示方式。

也請一併參考檔案結構中的「[オーナードローメニュー](../manual/owner-draw-menu.md)」。

設定可記載於 shell 的`descript.txt`，或設定為對數個用於取得資源的 SHIORI Event 所回覆的內容。

## 目次

1. [在 shell 的descript.txt中設定](ownerdraw.md#シェルのdescripttxtで設定する)
2. [透過SHIORI Event設定](ownerdraw.md#shiori-eventで設定する)

## 在 shell 的descript.txt中設定

可在 shell 的`descript.txt`中設定平時與選取時的背景、做為側邊欄使用的3張圖片，以及文字顏色。

只有 SSP 支援指定文字大小與字型。

此外，dressup 選單項目的配置等也可在 shell 的`descript.txt`中設定；相關內容請參閱「[dressup設定](bind.md)」頁面。

請注意，如果同一項目也透過 SHIORI Event 設定，會以 SHIORI Event 的設定為優先。

以下是使用`descript.txt`設定的範例。

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png

menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom

menu.background.font.color.r,0
menu.background.font.color.g,0
menu.background.font.color.b,0
menu.foreground.font.color.r,0
menu.foreground.font.color.g,0
menu.foreground.font.color.b,255
menu.separator.color.r,0
menu.separator.color.g,0
menu.separator.color.b,0
menu.disable.font.color.120
menu.disable.font.color.120
menu.disable.font.color.120
```

各行的詳細說明請參閱「[Shell設定](../descript/shell/descript-txt/menu.font.name.md)」，以下將簡單說明。

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png
```

以上三行分別設定オーナードローメニュー使用的3種圖片。

background 是平時的選單背景。

foreground 是目前選取項目的背景圖片。雖然不太容易理解，但オーナードローメニュー目前游標所在的部分，會以 foreground 圖片中相同位置的部分取代 background 圖片。

sidebar 是附加在オーナードローメニュー左側的圖片。

[![オーナードローメニュー使用的三張圖片](../assets/image/ownerdraw_materials.png)](../assets/image/ownerdraw_materials.png)

[![オーナードローメニュー的顯示畫面](../assets/image/ownerdraw_view.png)](../assets/image/ownerdraw_view.png)

*上方是使用的3張圖片，下方是實際顯示的畫面（範例：Emily/Phase4.5）*

```
menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom
```

以上三行分別設定3種圖片的配置方式。

在上面的範例中，background 與 foreground 圖片會以左上角為基準配置。若因選單文字或項目數量而使選單大於背景圖片，超出範圍的右側及下側會分別延伸圖片最右端與最左端的顏色來顯示。

```
menu.background.font.color.r,0
menu.background.font.color.g,0
menu.background.font.color.b,0
menu.foreground.font.color.r,0
menu.foreground.font.color.g,0
menu.foreground.font.color.b,255
menu.separator.color.r,0
menu.separator.color.g,0
menu.separator.color.b,0
menu.disable.font.color.120
menu.disable.font.color.120
menu.disable.font.color.120
```

以上是文字顏色的設定。

background 是平時的選單文字顏色，foreground 是游標位於項目上時的文字顏色，separator 是選單分隔線的顏色，disable 則是非作用中項目的文字顏色，例如沒有 dressup 的 shell 上的 dressup 選單，或不支援 network update 的 ghost 上的 network update 項目。

RGB 顏色的各個色彩分量以0～255的數值指定。RGB 全部為255時是白色，全部為0時是黑色。

## 透過SHIORI Event設定

除了與 shell 端`descript.txt`相同的設定外，也可以設定各選單項目的顯示名稱，以及我的最愛與入口網站連結清單的內容。

請注意，即使 shell 端的`descript.txt`已設定相同項目，也會以 SHIORI Event 的設定為優先。

關於如何對取得選單相關資源的 SHIORI Event 設定並回傳值，請參閱各 SHIORI 的說明。

例如，以下頁面可供參考，了解里々的情況。

[里々wiki - 右鍵選單](http://soliton.sub.jp/satori/index.php?%B1%A6%A5%AF%A5%EA%A5%C3%A5%AF%A5%E1%A5%CB%A5%E5%A1%BC)

關於其他 SHIORI Event，請參閱「[SHIORI Resource](../list/shiori-resource/ownerdraw-image/menu.sidebar.bitmap.filename.md)」頁面。
