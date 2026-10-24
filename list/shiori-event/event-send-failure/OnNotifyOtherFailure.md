# OnNotifyOtherFailure

**カテゴリ:** イベント送信失敗イベント

`\![notifyother]`が失敗した際に発生。

- **Reference0**: 見つからなかった場合、notfound。<br />
  `\t`中だった場合、timecritical。<br />
  パッシブモードだった場合、passivemode。<br />
  インダクションモードだった場合、inductionmode。<br />
  最小化中だった場合、minimized。<br />
  他、204など実行結果。<br />
  \_\_SYSTEM_ALL_GHOST\_\_などの場合バイト値1区切りのリスト。
- **Reference1**: ゴースト名または`\0`名。<br />
  \_\_SYSTEM_ALL_GHOST\_\_などの場合バイト値1区切りのリスト。
- **Reference2**: 実行しようとしたイベントID。
- **Reference3～**: 実行しようとしたイベントのReference。

**対応:** SSP
