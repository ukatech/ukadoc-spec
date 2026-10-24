# OnExecuteScheduleFailure

**カテゴリ:** その他通信イベント

`\![execute,schedule-add/schedule-delete]`が失敗した際に発生。

--eventでOnから始まるIDを指定した場合は、そのIDの後ろにFailureをつけたイベント名になる。

- **Reference0**: 操作の種類。add または delete
- **Reference1**: 失敗の理由<br />
  notauthorized : SSTPなど外部から送られたスクリプトで登録・削除しようとした<br />
  invalid : --summary・--startが無い、日時の書式が正しくない、UIDに使えない文字が含まれている、schedule-deleteでUIDが無い<br />
  notfound : schedule-deleteで指定したUIDの予定が無い<br />
  save : ファイルへの保存に失敗した（登録・削除自体は反映されている）
- **Reference2**: 指定されたUID（無ければ空）

**対応:** SSP 2.8.91
