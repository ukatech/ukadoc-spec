# OnTextAreaInput

**カテゴリ:** 入力ボックスイベント

[複数行入力ボックス(textareabox)](../../sakura-script/open/bang-open-textareabox-ID.md)に入力され決定された際に発生。<br />
IDが「On」で始まる場合はこのイベントの代わりにID名のイベントが発生し、Reference0に入力内容が入る(以降は1つずつ前へずれる)。[InputBoxのID](../../sakura-script/open/notes_inputbox-id.md)と同じ規則。

- **Reference0**: textareaboxのID。
- **Reference1**: 入力された内容。改行はバイト値1の文字(`\1`)で区切られる。
- **Reference2**: 空欄(OnUserInputとReferenceの位置を揃えるため)
- **Reference3～**: --reference=で指定した追加情報

**対応:** SSP 2.9.10
