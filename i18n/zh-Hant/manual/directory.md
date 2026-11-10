# 整體結構

## ghost 與 shell

ghost 的組成檔案會放置在 baseware（SSP、materia 等）的 ghost 儲存資料夾中。

所有 ghost 都必須有一個 master ghost 和 master shell。

從 shell 的角度來看，所有 shell 都必定隸屬於某一個 ghost。

因此，兩者的檔案結構如下，shell 包含在 ghost 之中。

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau
　　　　　　+-*.ico
　　　　　　+-*.cur
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-makoto.dll (必要な時のみ)
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
　　　　　　+-readme.txt (必要な時のみ)
　　　　　　+-thumbnail.png
　　　　　　+-surfaces**.txt (SSPのみ）
　　　　　　+-surfacetable.txt (必要な時のみ)(SSPのみ)
　　　　　　+-alias.txt (必要な時のみ)(旧仕様）
　　　　+-(additional_shell)
　　+-delete.txt (必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
　　+-developer_options.txt (必要な時のみ)(SSPのみ)
　　+-.narignore (必要な時のみ)(SSPのみ)
　　+-.updateignore (必要な時のみ)(SSPのみ)
　　+-.narinclude (必要な時のみ)(SSPのみ)
　　+-.updateinclude (必要な時のみ)(SSPのみ)
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-thumbnail.png
```

## balloon

balloon 不是由各個 ghost 分別管理，而是由 baseware 統一管理，並由所有 ghost 共用。

各個 balloon 的組成檔案會放置在 baseware 的 balloon 儲存資料夾下，結構如下。

```filetree
+-(myballoon)
　　+-descript.txt
　　+-balloons*s.txt
　　+-balloonk*s.txt
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-balloons*.png
　　+-balloonk*.png
　　+-balloons*.pna （MATERIA不可）
　　+-balloonk*.pna （MATERIA不可）
　　+-balloonc*.png
　　+-online*.png
　　+-sstp.png
　　+-arrow*.png
　　+-thumbnail.png
　　+-ok_down.png/ok_up.png （SSPのみ）
　　+-cancel_down.png/cancel_up.png （SSPのみ）
　　+-mode_down.png/mode_up.png （SSPのみ）
　　+-sstp_new.png （SSPのみ）
　　+-marker.png （SSPのみ）
　　+-delete.txt (SSPのみ・必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
```

- **(myghost)\\**: 各 ghost 的 home 目錄（根資料夾）。

  資料夾名稱建議使用英數字。

- **(myghost)\\ghost\\**: ghost 內部動作檔案的資料夾。

- **(myghost)\\ghost\\master\\**: ghost 預設使用的資料夾。

  目前只會使用 master（沿用過去設計的遺留規格）。

ghost 資料夾內檔案結構的詳細資訊，請參閱「[ghost](ghost.md)」頁面。

關於 makoto.dll，請參閱「[轉換器](translator.md)」頁面。

- **(myghost)\\shell\\**: 存放 ghost 的 shell（用於顯示圖像的檔案群）的資料夾。

- **(myghost)\\shell\\master\\**: 預設 shell 的資料夾。必須存在。

- **(myghost)\\shell\\(additional_shell)\\**: 追加 shell 的資料夾。名稱不限（建議使用英數字）。檔案結構與 master 相同。

  可以有任意數量。存在時，可從 owner draw 選單等處選擇切換。

shell 資料夾內檔案結構的詳細資訊，請參閱「[shell](shell.md)」頁面。

關於 menu_background.png、menu_foreground.png、menu_sidebar.png，請參閱「[owner draw 選單](owner-draw-menu.md)」頁面。

關於 makoto.dll，請參閱「[轉換器](translator.md)」頁面。

- **(myghost)\\[delete.txt](../descript/install/delete.txt/index.md)**: 檔案刪除設定檔。

  詳細資訊請參閱[連結目標](../descript/install/delete.txt/index.md)。

  可以省略。

- **(myghost)\\[developer_options.txt](../descript/install/developer_options.txt/index.md)**: 僅適用於 SSP。nar 與更新檔案建立功能的設定檔。

  詳細資訊請參閱[連結目標](../descript/install/developer_options.txt/index.md)。

  可以省略。

- **(myghost)\\readme.txt 或 readme.md**: 整個 ghost 的 readme。

  通常會明確記載發行者、發行來源等資訊。

  在第一行寫上 charset,UTF-8，或是加入 BOM，即可使用 Shift JIS 以外的編碼。

  除了安裝時會開啟之外，也可以從 owner draw 選單等處開啟。

  可以省略，但建議提供。

  可以使用 readme.md 取代 readme.txt；此時會以 Markdown 格式解析，並以附有字體大小、表格等裝飾的方式顯示。<br />
  也可以解析圖片嵌入 `\![圖片說明]`(圖片路徑)，但只有在圖片路徑為相對路徑、檔案實際存在於 ghost 中，且格式為 PNG 或 JPEG 時才能使用。

- **(myghost)\\terms.txt 或 terms.md**: 顯示使用條款。在安裝 NAR/ZIP 檔案前，會顯示對話方塊呈現此檔案的內容。

  由於會顯示對話方塊並中斷安裝，因此只在確實需要時才加入。

  與 readme 相同，在第一行寫上 charset,UTF-8，或是加入 BOM，即可使用 Shift JIS 以外的編碼。

  可以省略，而且*若不需要，建議省略*。

  terms.md 也可以在與 readme.md 相同的條件下使用。

- **(myghost)\\thumbnail.png**: 在選單樹狀清單中選擇 ghost 時顯示的縮圖。

  可使用的圖片格式為 PNG 或 JPG。

  將 PNG 重新命名為 PNR 後，圖片左上角的 1 個像素（座標 0,0）會以同色透明處理。

  可以省略。

- **(myballoon)\\**: 各 balloon 的 home 目錄（根資料夾）。

  資料夾名稱建議使用英數字。

balloon 資料夾內檔案結構的詳細資訊，請參閱「[balloon](balloon.md)」頁面。
