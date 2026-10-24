# OnSecondChange

**カテゴリ:** 時間イベント

1秒ごとに発生。

トーク再生不能な時は、Reference3が0になった上でNOTIFYでイベント通知される。**返されたスクリプトは無視される。**

- **Reference0**: OSの連続起動時間（hour）
- **Reference1**: 見切れ時に1、それ以外は0。
- **Reference2**: 重なり時に1、それ以外は0。
- **Reference3**: トーク再生可能なときに1、それ以外は0。
- **Reference4**: ※SSPのみ　(OSレベルで)何も操作せず放置されている時間。秒単位。

**対応:** Materia / SSP / CROW / Ninix
