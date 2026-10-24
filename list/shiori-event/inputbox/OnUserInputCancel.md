# OnUserInputCancel

**カテゴリ:** 入力ボックスイベント

InputBoxが閉じられた際に発生。<br />
タイムアウトした場合、かつこのイベントに反応がない場合は、互換性確保のため、OnUserInput Reference1=timeout が送られる。

- **Reference0**: 入力のイベントID。
- **Reference1**: タイムアウトした場合、timeout。閉じられた場合、close。
- **Reference2**: 入力内容補足(sliderinputのみ、最小,最大。ほかは空欄)
- **Reference3～**: --reference=で指定した追加情報

**対応:** SSP / Ninix
