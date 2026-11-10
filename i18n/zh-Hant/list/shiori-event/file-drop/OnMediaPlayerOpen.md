# OnMediaPlayerOpen

**カテゴリ:** 檔案拖放事件

檔案以 DnD 拖放，ghost 未對 OnFileDrop2 回應（或執行 [`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md) \[2.9.10\]），且開啟媒體播放器時觸發。Reference 與 OnFileDrop2 相同。

- **Reference0**: 拖放的檔案路徑。若有多個檔案／目錄，則以 byte 值 1 分隔。
- **Reference1**: 拖放目標角色的 scope 編號。主體一側為 0，搭檔為 1，第三名角色起為 2 以上。
- **Reference2**: 拖放檔案的 MIME 類型。若有多個檔案／目錄，則以 byte 值 1 分隔。

**対応:** SSP 2.8.51
