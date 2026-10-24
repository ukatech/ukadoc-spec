# OnInstallReroute

**カテゴリ:** インストールイベント

インストールするファイルが他のゴーストを指名していた際、かつ、指名対象ゴーストが一緒に起動していた時に発生。以降のインストールイベントは指名対象ゴースト側に発生する。

- **Reference0**: 指定されたゴーストの本体側名（install.txtの[accept](../../../descript/install/install-txt/accept.md)指定、つまり本来渡すべき相手）。
- **Reference1**: インストールした物の[※識別子](caption_install-identifier.md)。
- **Reference2**: インストールした物の名前。

**対応:** SSP 2.4 / Ref1以降は2.4.85
