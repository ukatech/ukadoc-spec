# OnURLDropping

**カテゴリ:** URL 拖放事件

URL 被拖放後，開始下載時發生。<br />
此事件會在下載處理之前發生。其他情況（例如homeurl安裝或feed（RSS）安裝）不會觸發。

- **Reference0**: 拖放的 URL。
- **Reference1**: 被拖放的角色的 scope 編號。本體側為0，搭檔側為1，第三位及之後的角色為2以上。

**対応:** Materia / SSP 的Ref1支援於2.6.36起 / CROW
