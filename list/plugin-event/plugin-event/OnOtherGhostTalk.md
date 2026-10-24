# OnOtherGhostTalk

**カテゴリ:** PLUGIN Event

ゴーストが話した際に発生。<br />
descript.txtの[otherghosttalkで設定可能。](../../../descript/plugin/descript-txt/otherghosttalk.md)

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
- **Reference3**: ゴーストの話したイベントID。
- **Reference4**: ゴーストの話した内容のスクリプト。
- **Reference5**: バイト値1区切りのゴーストに渡されたReference。

**対応:** SSP
