# OnMinuteChange

**カテゴリ:** 時間事件

每分鐘發生一次。

無法播放談話時，Reference3 會設為 0，並以 NOTIFY 通知事件。**傳回的腳本會被忽略。**

- **Reference0**: OS 連續運作時間（小時）
- **Reference1**: 被切出視窗時為 1，其他情況為 0。
- **Reference2**: 重疊時為 1，其他情況為 0。
- **Reference3**: 可以播放談話時為 1，其他情況為 0。
- **Reference4**: ※僅 SSP　（OS 層級）未操作而閒置的時間，單位為秒。

**対応:** Materia / SSP / CROW / Ninix
