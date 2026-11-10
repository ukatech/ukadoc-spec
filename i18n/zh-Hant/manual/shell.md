# shell

shell 資料夾中的檔案如下。

```filetree
+-(myghost)
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-readme.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-surfaces**.txt （SSPのみ）
　　　　　　+-alias.txt（旧仕様）
　　　　　　+-thumbnail.png
　　　　　　+-makoto.dll
　　　　　　+-surfacetable.txt (SSPのみ)
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
```

※關於 menu_background.png、menu_foreground.png、menu_sidebar.png，請參閱「[owner draw 選單](owner-draw-menu.md)」頁面。

- **[descript.txt](../descript/shell/index.md)**: 用來識別 shell 並進行基本設定的檔案。

  文字檔中的記載事項請參閱[連結頁面](../descript/shell/index.md)。

- **readme.txt**: shell 製作者用來記載發佈來源等資訊的檔案。

  可以省略，但若有準備，安裝時或透過 baseware 選單等方式便能參閱。

  尤其是 ghost 作者與 shell 作者不同時，建議盡可能準備此檔案。

- **surface\*.png**: surface 檔案。

  顯示在桌面上的圖像。

  圖像尺寸與色數皆無限制。

  檔案格式為 PNG[※](shell.md#シェル)。

  與圖像左上角的 1 個像素（座標 0,0）同色的區域會被視為透明色（去背色），顯示時將會透明。

  surface 編號[有一定程度的標準分配方式](../descript/shell-surfaces/surface-brace/caption_standarddef.md)，但基本上可自由設定。

  不過，surface0 和 surface10 為必須項目（SSP 中建議使用，但不是必須）。

  因此，即使是只有一個角色的 ghost，也需要準備 surface10.png，例如放置一張以單色填滿的圖像。

  如果 baseware 是 MATERIA（embryo、本家的 伺か (Ukagaka)），surface 編號範圍為 0～8192。

  其他 baseware 則沒有此限制。

  SSP 2.7.38 之後，若將動畫 GIF/APNG/WebP 動畫指定為 surface\*.png，即使不撰寫 SERIKO 定義也會播放動畫。

- **surface\*.pna**: surface 的 alpha 通道定義檔。

  將灰階 PNG 圖像（黑：透明 ←→ 不透明：白）的副檔名改為 pna。

  放置與 surface 編號相同的 pna 檔案，即可讓 surface 半透明。

  | ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
  | --- | --- | --- | --- | --- |
  | surface0.png |  | surface0.pna |  | 桌面顯示 |

  未完全透明的區域會產生命中判定。

  此外，在 Windows9x 或非常老舊的顯示卡等不支援的環境中，pna 會被忽略。

  另外，在 SSP 中也可以透過[設定](../descript/shell/descript-txt/seriko.use_self_alpha.md)使用 PNG 本身的 alpha 通道（透明度資訊）。

- **(element).png**: 依照 [element](../descript/shell-surfaces/surface-brace/element-star.md) 規格，可將任意名稱的 PNG 圖像[※](shell.md#シェル)作為零件合成，並視為一個 surface。這是用於此目的的零件圖像。

  ※可將 (element) 部分替換為任意名稱。可使用任意數量的圖像，也可以完全不使用。

  SSP 2.7.38 之後，若在 surfaces.txt 的 element 定義中指定動畫 GIF/APNG/WebP 動畫，即使不撰寫 SERIKO 定義也會播放動畫。

  詳情也請參閱後述的「surfaces.txt」。

- **(element).pna**: 各 element 合成用零件圖像的 pna。

- **[surfaces.txt](../descript/shell-surfaces/index.md)**: 定義 surface ID 分配、圖層合成、動畫、命中判定等的檔案。

  定義內容請參閱 [surfaces.txt](../descript/shell/index.md)。

  動畫與 dressup 請參閱動畫。

- **[surfaces\*\*.txt](../descript/shell-surfaces/index.md)**: SSP 專用。

  \*\*可使用任意字串。

  2.01 系列之後開始支援 surfaces2.txt 這類名稱，而可加上任意字串則是從 2.2.57 之後開始。

  功能與 `surfaces.txt` 相同。

  此檔案可在維持相容性的同時使用 SSP 專用功能。

  此檔案可以省略。只追加需要的部分也沒有問題。

- **[alias.txt](../descript/shell-surfaces/surface-alias-brace/caption_aliastxt.md)**: 舊規格。用來記述 sakura(kero).alias 括號的文字檔。

  目前此功能已整合至 surfaces.txt。

- **thumbnail.png**: 在選單樹中選取 shell 時顯示的縮圖。

  可使用的圖像格式為 png 或 jpg。

  將 png 改名為 pnr 後，圖像左上角的 1 個像素（座標 0,0）同色部分會變透明。

  此檔案可以省略。

- **[makoto.dll](translator.md)**: 用來使用轉譯功能。

  與可準備在 [ghost 端](ghost.md)的檔案相同。詳情請參閱[連結頁面](translator.md)。

  此檔案可以省略。

- **[surfacetable.txt](../descript/shell-surfacetable/index.md)**: SSP 專用。

  定義 surface 內容的檔案，供 SSP 開發用面板的「surface 測試」功能及其他 shell 製作支援工具使用。

  詳情請參閱[連結頁面](../descript/shell-surfacetable/index.md)。

  此檔案可以省略。

!!! tip "提示"

    - **[※1](shell.md#シェル),[※2](shell.md#シェル)**: SSP 也可以使用加密 PNG（DAP/DDP/DFP/DGP）、GIF（非動畫）、JPEG、BMP，但*不建議使用*。

      為了向前相容而仍可載入，但不保證日後新增的功能或規格會支援 PNG 以外的格式。

      此外，目前 PNG 以外的所有格式都無法使用透明度規格（pna 及 [seriko.use_self_alpha](../descript/shell/descript-txt/seriko.use_self_alpha.md)）；而 JPEG 也容易因壓縮造成色彩偏移，因此不適合搭配透明色使用。
