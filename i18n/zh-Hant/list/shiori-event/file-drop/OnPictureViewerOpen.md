# OnPictureViewerOpen

**カテゴリ:** 檔案拖放事件

檔案經由 DnD 拖放後，若 ghost 未回應 OnFileDrop2（或執行了[`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)［2.9.10］），且開啟了圖片檢視器，就會觸發此事件。Reference 與 OnFileDrop2 相同。

- **Reference0**: 被拖放檔案的路徑。若有多個檔案／目錄，以 byte 值 1 分隔。
- **Reference1**: 被拖放角色的 scope 編號。本體側為 0，搭檔為 1，第 3 人起為 2 以上。
- **Reference2**: 被拖放檔案的 MIME 類型。若有多個檔案／目錄，以 byte 值 1 分隔。

**対応:** SSP 2.8.51
