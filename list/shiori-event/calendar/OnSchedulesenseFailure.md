# OnSchedulesenseFailure

**カテゴリ:** カレンダーイベント

スケジュールセンサの処理に失敗した場合に発生。<br />
特定のゴーストではなく起動中の全ゴーストに通知される。

Begin/Completeと違い、[定期チェックでも発生する](caption_schedulesensetiming.md)。

- **Reference0**: [失敗した理由](../headline-rss/caption_headlinesenseresult.md)（ヘッドラインセンサのものと共通）。取得できなかった場合can't download、取得はできたがiCalとして解析できなかった場合can't analyze。
- **Reference1**: スケジュールセンサの名前。定期チェックではBeginが無いため、これが無いとどのセンサが失敗したのか分からない

**対応:** SSP
