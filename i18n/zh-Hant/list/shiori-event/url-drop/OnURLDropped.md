# OnURLDropped

**カテゴリ:** URL 拖放事件

接收完拖放的 URL 時發生。<br />
此事件會在安裝NAR之前、下載處理完成後立即發生。其他情況（例如homeurl安裝或feed（RSS）安裝）不會觸發。

- **Reference0**: 已完成下載的檔案本機路徑。
- **Reference1**: 拖放的 URL。
- **Reference2**: 被拖放的角色的 scope 編號。本體側為0，搭檔側為1，第三位及之後的角色為2以上。

**対応:** Materia / SSP 的Ref1、2支援於2.6.36起 / CROW
