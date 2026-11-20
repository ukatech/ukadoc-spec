# owner draw 選單的設定

本頁說明如何設定 owner draw 選單（右鍵選單）的顯示方式。

也請一併參考檔案結構中的「[owner draw 選單](../manual/owner-draw-menu.md)」。

設定可記載於 shell 的 `descript.txt`，或作為取得資源時發出的數個 SHIORI Event 的回應來設定。

## 目次

1. [在 shell 的 descript.txt 中設定](ownerdraw.md#シェルのdescripttxtで設定する)
2. [透過 SHIORI Event 設定](ownerdraw.md#shiori-eventで設定する)

## 在 shell 的 descript.txt 中設定

shell 的 `descript.txt` 可以設定用作一般狀態背景、選取狀態背景及側邊欄的３張圖片，以及文字顏色。

僅 SSP 也可以指定文字大小及字型。

此外，dressup 選單的項目配置等也在 shell 的 `descript.txt` 中設定，相關內容請參閱「[dressup 的設定](bind.md)」頁面。

請注意，如果同一項目也透過 SHIORI Event 設定，則以 SHIORI Event 的設定為優先。

在 SSP 中，ghost 的 `descript.txt`（`ghost/master/descript.txt`）也可以記載相同項目。如果 shell 的 `descript.txt` 也有相同項目，則以 shell 的設定為優先。

以下是以 `descript.txt` 設定的範例。

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
menu.disable.font.color.r,120
menu.disable.font.color.g,120
menu.disable.font.color.b,120
```

各行的詳細說明請參閱「[Shell 設定](../descript/shell/descript-txt/menu.font.name.md)」，以下僅概略說明。

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png
```

以上三行分別設定 owner draw 選單使用的3種圖片。

background 是一般狀態下的選單背景。

foreground 是選取項目的背景圖片。這可能有些難以理解：只有 owner draw 選單中游標目前所在的部分，會將 background 圖片替換為 foreground 圖片對應位置的部分。

sidebar 是附在 owner draw 選單左側的圖片。

[![owner draw 選單使用的三張圖片](../assets/image/ownerdraw_materials.png)](../assets/image/ownerdraw_materials.png)

[![owner draw 選單的顯示](../assets/image/ownerdraw_view.png)](../assets/image/ownerdraw_view.png)

*上方是使用的3張圖片，下方是實際顯示效果（例:Emily/Phase4.5）*

```
menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom
```

以上三行分別設定3種圖片的配置方式。

在上述範例中，background、foreground 圖片以左上角為起點配置。如果因選單的文字數量或項目數量而使選單大於背景圖片，超出區域的右側及下側會分別延伸圖片右端及左端的顏色來顯示。

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
menu.disable.font.color.r,120
menu.disable.font.color.g,120
menu.disable.font.color.b,120
```

以上是文字顏色的設定。

background 是一般狀態下的選單文字顏色，foreground 是游標位於項目上時的文字顏色，separator 是選單分隔字元的顏色，disable 是非作用中項目的文字顏色，例如沒有 dressup 的 shell 中的 dressup 選單，或不支援 network update 的 ghost 中的 network update 項目。

RGB 色彩的各個色彩分量以 0～255 的數值指定。rgb 全部為255時是白色，全部為0時是黑色。

## 透過 SHIORI Event 設定

除了與 shell 端 `descript.txt` 相同的設定之外，也可以設定選單各項目的顯示名稱，以及我的最愛與入口網站連結集的內容。

即使同一項目在 shell 端 `descript.txt` 中已有設定，仍以 SHIORI Event 的設定為優先。

如何針對取得選單相關資源的 SHIORI Event 設定及回傳值，必須參閱各 SHIORI 的說明。

例如使用 Satori 時，可以參考以下頁面。

[Satori wiki - 右鍵選單](http://soliton.sub.jp/satori/index.php?%B1%A6%A5%AF%A5%EA%A5%C3%A5%AF%A5%E1%A5%CB%A5%E5%A1%BC)

其他 SHIORI Event 請參閱「[SHIORI Resource](../list/shiori-resource/ownerdraw-image/menu.sidebar.bitmap.filename.md)」頁面。
