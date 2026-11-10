# OnSecondChange

**カテゴリ:** 时间事件

每秒触发一次。

无法播放对话时，会将Reference3设为0，并通过NOTIFY通知事件。**返回的脚本会被忽略。**

- **Reference0**: OS连续运行时间（hour）
- **Reference1**: 被遮挡时为1，否则为0。
- **Reference2**: 重叠时为1，否则为0。
- **Reference3**: 可以播放对话时为1，否则为0。
- **Reference4**: ※仅限SSP　（OS级别）无操作闲置时间，单位为秒。

**対応:** Materia / SSP / CROW / Ninix
