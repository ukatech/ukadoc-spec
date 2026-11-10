# delete.txt

## 概要

也請參閱[檔案結構「network update」](../../../manual/update.md)頁面。

更新時，客戶端（使用者）的檔案只會由伺服器（作者）的檔案覆寫，並不會進行同步。<br />
也就是說，已下載或建立在客戶端的檔案，即使從伺服器刪除，也無法移除。<br />
因此，發佈後若需要刪除已發佈的檔案，必須在 delete.txt 中列出該檔案。<br />
另外，delete.txt 執行刪除後不會自動刪除；只要不修改，已列出的內容就會永久持續排除。

以下是僅適用於 SSP 的規格。

- **charset,(字元編碼)**: 指定檔案的字元編碼

## 記述例

```
ghost\master\ai.dtx
ghost\master\testdict\
shell\master\surface110.png
```
