# 概要

這是 ghost 更新系統（network update）所使用的更新定義檔規格。<br />
更新定義檔記錄了構成 ghost 的檔案清單及其雜湊值；baseware 會從伺服器取得此檔案，並與本機檔案比較以進行差異更新。

目前有效的格式有以下 2 種。舊格式 updates.dau (Version 1) 已廢止，因此不予說明。

- **updates2.dau (Version 2)**：以位元組值 1 分隔、較偏向二進位的格式。
- **updates.txt (Version 3)**：以位元組值 1 分隔，並具有行前綴的文字格式。
