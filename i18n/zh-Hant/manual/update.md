# 網路更新

網路更新相關的設定等，請參閱「[支援網路更新](../dev/update.md)」頁面。

網路更新相關檔案的配置如下。

- **ghost 的情況**:

  ```filetree
  +-(myghost)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt (SSPのみ)
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(僅限 SSP) 讓追加 shell 支援網路更新的情況**:

  ```filetree
  +-(myshell)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(僅限 SSP) 讓 balloon 支援網路更新的情況**:

  ```filetree
  +-(myballoon)
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-descript.txt
  　　+-balloons*s.txt
  　　+-balloonk*s.txt
  　　+-readme.txt
  　　+-balloons*.png
  　　+-balloonk*.png
  　　:
  　　:
  ```

  plugin、headline sensor 等也相同，放在各自的資料夾內即可。

- **updates2.dau**: 列出更新目標檔案的 MD5 雜湊值等資訊的檔案。

  用於網路更新時，檢查伺服器上的檔案與實際下載的檔案之間，是否有檔案損毀或遭到竄改。

  通常使用 baseware 的功能等方式建立，無須由人工編輯。

  建立步驟等請參閱「[支援網路更新](../dev/update.md)」頁面

- **updates.txt**: 功能幾乎與 updates2.dau 相同。有其中一個即可（兩者都有也沒問題）。

  除了格式略有不同，也能避開因副檔名限制而無法上傳 dau 等問題。

- **[delete.txt](../descript/install/delete.txt/index.md)**: 檔案刪除設定檔。

  放置在伺服器上與 updates2.dau 相同的位置。

  用於避免不再需要的檔案持續累積、增加檔案體積等。

  格式等詳細資訊請參閱[連結頁面](../descript/install/delete.txt/index.md)。

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: 僅限 SSP。

  放置在要建立 updates2.dau 的位置（最上層目錄）。

  在 SSP 建立 updates2.dau（updates.txt）時，用來指定不納入目標的檔案等。

  不需要上傳到伺服器（例如指定排除自身即可），但即使保留也沒有影響；可自行決定，並考量使用者可能會再次重新封裝成 nar 等情況。

  格式等詳細資訊請參閱[連結頁面](../descript/install/developer_options.txt/index.md)。
