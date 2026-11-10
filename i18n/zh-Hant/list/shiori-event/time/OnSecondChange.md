# OnSecondChange

**カテゴリ:** 時間事件

每秒發生一次。

無法播放對話時，Reference3會設為0，並以NOTIFY通知事件。**回傳的腳本會被忽略。**

- **Reference0**: OS連續運作時間（小時）
- **Reference1**: 部分隱藏時為1，其他情況為0。
- **Reference2**: 重疊時為1，其他情況為0。
- **Reference3**: 可播放對話時為1，其他情況為0。
- **Reference4**: ※僅限SSP　（在OS層級）未進行任何操作的閒置時間，單位為秒。

**対応:** Materia / SSP / CROW / Ninix
