# ghost

master ghost 資料夾中的檔案如下。

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-(saori).dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau （旧仕様）
　　　　　　+-updates.txt （旧仕様）
　　　　　　+-*.ico
　　　　　　+-*.cur
　　　　　　+-thumbnail.png
　　　　　　+-ai0.png
　　　　　　+-ai0_dark.png
```

- **[descript.txt](../descript/ghost/index.md)**: 用於識別 ghost 的檔案。

  缺少此檔案時，主程式無法識別 ghost。

  關於檔案內記載內容等詳細資訊，請參閱[連結目標](../descript/ghost/index.md)。

- **[updates2.dau](update.md)**

- **[updates.txt](update.md)**: 記載更新資訊的檔案。

  此處的檔案位置屬於舊規格，基本上只需放在根目錄（(myghost) 直下）。

  詳細資訊請參閱[連結目標](update.md)

- **shiori.dll**: ghost 的核心。幾乎是必備檔案。

  有許多通用 SHIORI 可供使用，通常會使用其中一種。

  接收由 baseware（例如 SSP）傳送的 [SHIORI Event](../list/shiori-event/index.md)（[補充說明](../memo/shiori-event.md)），建立作為 ghost 動作指示的 [Sakura Script](../list/sakura-script/index.md)，再傳回 baseware。

  實際對話的寫法等 ghost 核心部分的製作方式，會因 SHIORI 而大不相同，請參閱各 SHIORI 的文件。

- **(saori).dll**: SHIORI 的功能擴充模組。

  基本上會放在與 shiori.dll 相同的目錄層級。

  但也可以在從 SHIORI 呼叫時指定相對路徑。

  使用步驟取決於 SHIORI，請參閱 SHIORI 的文件。

  此檔案可以省略。

- **[makoto.dll](translator.md)**: 用於轉換的 DLL。

  詳細資訊請參閱[連結目標](translator.md)。也可以放在[shell 端](shell.md)。

  此檔案可以省略。

- **\*.ico**: 圖示檔案。

  可以使用 32×32 與 16×16 的圖示。

  在圖示化時或 ghost explorer 等處顯示。

  此檔案可以省略。省略時會使用預設圖示。

- **\*.cur**: 游標檔案。

  游標移到 ghost 上時，會變成指定的游標。

  此檔案可以省略。省略時會維持一般游標。

- **thumbnail.png**: 在選單樹狀清單中選擇 ghost 時顯示的縮圖。

  可使用的圖片格式為 PNG 或 JPG。

  將 PNG 重新命名為 PNR 後，圖片左上角的 1 個像素（座標 0,0）會以同色透明處理。

  此檔案可以省略。

- **ai0.png / ai0_dark.png**: 請參閱 [AI 圖表說明](../descript/ghost/descript-txt/shiori.logo.file.md)。

  此檔案可以省略。

除此之外，SHIORI（等）通常也會在 DLL 外部備有數個檔案，例如稱為「字典」的字串資源檔（ghost 製作者也常以這些檔案為主要編輯對象）。<br />
關於這些檔案的詳細資訊，請參閱所使用的各 SHIORI 文件。
