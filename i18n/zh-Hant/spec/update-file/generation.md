# 產生處理

透過SSP的「建立更新檔案」功能等，可從ghost的檔案清單產生updates2.dau / updates.txt。

- **檔案掃描**: 遞迴掃描目錄。以下檔案會排除。

  - 隱藏檔案 (`FILE_ATTRIBUTE_HIDDEN`)
  - [developer_options.txt](../../descript/install/developer_options.txt/index.md) 中以 `noupdate` 指定的檔案
  - 由.gitignore格式的篩選檔排除的檔案

- **複製至ghost\\master**: 若目錄下存在 `ghost\master` 資料夾，也會將產生的更新檔案複製到該處。
