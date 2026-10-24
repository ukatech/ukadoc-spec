# OnInstallCompleteAll

**カテゴリ:** インストールイベント

複数のnarをD&Dした時などに、インストールが**すべて**正常終了した際に、OnInstallComplete/同Exの後に、最後に発生。<br />
SSPでは2.9.00より前のバージョンに実装漏れがあり、実際には発生しない。

- **Reference0**: インストールした物の[※識別子](caption_install-identifier.md)。複数の場合はバイト値1区切り。
- **Reference1**: インストールした物の名前。複数の場合はバイト値1区切り。
- **Reference2**: インストールした場所。複数の場合はバイト値1区切り。

**対応:** SSP 2.9.00 / Ninix
