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

  沒有此檔案，baseware 便無法辨識。

  文字內容等詳細資訊請參閱[連結頁面](../descript/ghost/index.md)。

- **[updates2.dau](update.md)**

- **[updates.txt](update.md)**: 記載更新資訊的檔案。

  放在此位置是舊規格，基本上只需放在根目錄（(myghost) 正下方）。

  詳情請參閱[連結頁面](update.md)。

- **shiori.dll**: ghost 的核心。幾乎是必需的。

  由於已有許多通用 SHIORI，通常會使用這些現成的 SHIORI。

  其作用是接收 baseware（如 SSP）傳送的 [SHIORI Event](../list/shiori-event/index.md)（[補充說明](../memo/shiori-event.md)），建立作為 ghost 動作指示的 [Sakura Script](../list/sakura-script/index.md)，並回傳給 baseware。

  實際編寫對話等 ghost 核心部分的方式因 SHIORI 而完全不同，請參閱各 SHIORI 的文件。

- **(saori).dll**: SHIORI 的功能擴充模組。

  基本上放在與 shiori.dll 相同的層級。

  但從 SHIORI 呼叫時也可以指定相對路徑。

  使用步驟依 SHIORI 而異，請參閱 SHIORI 的文件。

  此檔案可省略。

- **[makoto.dll](translator.md)**: 用於轉譯的 DLL。

  詳情請參閱[連結頁面](translator.md)。也可放在 [shell 側](shell.md)。

  此檔案可省略。

- **\*.ico**: 圖示檔案。

  可以使用 32×32 和 16×16 的圖示。

  最小化為圖示時或在 ghost 瀏覽器等處顯示。

  此檔案可省略。省略時使用預設圖示。

- **\*.cur**: 游標檔案。

  游標移到 ghost 上時會變成指定的游標。

  此檔案可省略。省略時維持一般游標。

- **thumbnail.png**: 在選單樹中選擇 ghost 時顯示的縮圖。

  可使用的圖片格式為 png 或 jpg。

  將 png 重新命名為 pnr 後，與圖片左上角 1 個像素（座標 0,0）相同的顏色會變成透明。

  此檔案可省略。

- **ai0.png / ai0_dark.png**: 請參閱 [AI 圖表說明](../descript/shell/descript-txt/shiori.logo.file.md)。

  此檔案可省略。

除此之外，SHIORI（等）通常會在 dll 外部配置數個檔案，例如稱為「字典」的字串資源檔（ghost 製作者甚至往往以編輯這些檔案為主）。<br />
這些檔案的詳細資訊請參閱所使用的各 SHIORI 文件。
