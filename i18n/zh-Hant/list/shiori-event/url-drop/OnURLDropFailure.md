# OnURLDropFailure

**カテゴリ:** URL 拖放事件

接收拖放的 URL 失敗或遭取消時發生。<br />
嘗試安裝NAR但失敗時會觸發此事件。其他情況（例如homeurl安裝或feed（RSS）安裝）不會觸發。

- **Reference0**: 已完成下載的檔案本機路徑。
- **Reference1**: [※失敗原因](../network-update/caption_updateresultfailure.md)
- **Reference2**: 拖放的 URL。
- **Reference3**: 被拖放的角色的 scope 編號。本體側為0，搭檔側為1，第三位及之後的角色為2以上。

**対応:** Materia / SSP 的Ref2、3支援於2.6.36起 / CROW
