# OnOtherGhostTalk

**カテゴリ:** その他イベント

他のゴーストが話した際に発生。`\![set,otherghosttalk,true]`で有効に。

- **Reference0**: ゴースト名。
- **Reference1**: ゴーストの本体側名。
- **Reference2**: トークを中断した場合、break。<br />
  コミュニケートの場合、communicate。<br />
  SSTP SENDの場合、sstp-send。<br />
  Owned SSTPの場合、owned。<br />
  非ローカルSSTPの場合、remote。<br />
  トランスレートしない指定の場合、notranslate<br />
  プラグインからのスクリプトの場合、plugin-script<br />
  プラグインからのイベント反応の場合、plugin-event<br />
  該当するものがカンマ区切りで返る。
- **Reference3**: 他ゴーストの話したイベントID。
- **Reference4**: 他ゴーストの話した内容のスクリプト。
- **Reference5**: バイト値1区切りの他ゴーストに渡されたReference。

**対応:** SSP / Ninix
