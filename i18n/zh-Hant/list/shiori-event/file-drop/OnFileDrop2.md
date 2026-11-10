# OnFileDrop2

**カテゴリ:** 檔案拖放事件

檔案以 DnD 拖放時觸發。此事件是目前最新的規格。<br />
若回應此事件，便不會執行本體的預設處理（以影像檢視器、媒體播放器或封存檢視器開啟）。若要在回應事件的同時也執行預設處理，請使用 [`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)。\[2.9.10\]

- **Reference0**: 拖放的檔案路徑。若有多個檔案／目錄，則以 byte 值 1 分隔。
- **Reference1**: 拖放目標角色的 scope 編號。主體一側為 0，搭檔為 1，第三名角色起為 2 以上。
- **Reference2**: 拖放檔案的 MIME 類型（SSP 2.7.98 以後）。若有多個檔案／目錄，則以 byte 值 1 分隔。

**対応:** Materia / SSP / CROW / Ninix
