# OnTextAreaInputCancel

**カテゴリ:** 入力ボックスイベント

複数行入力ボックス(textareabox)が閉じられた際に発生。<br />
IDにかかわらずこのイベントが発生する。OnUserInputCancelと違い、タイムアウト時に入力決定のイベントへ投げ直すことはない。

- **Reference0**: textareaboxのID。
- **Reference1**: タイムアウトした場合、timeout。閉じられた場合、close。
- **Reference2**: 閉じるまでに入力されていた内容。改行はバイト値1の文字(`\1`)で区切られる。
- **Reference3～**: --reference=で指定した追加情報

**対応:** SSP 2.9.10
