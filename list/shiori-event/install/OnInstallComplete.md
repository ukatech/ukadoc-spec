# OnInstallComplete

**カテゴリ:** インストールイベント

インストールが正常終了した際に発生。<br />
このイベントは旧仕様のため、1回のインストールで同時に入った物のうち*先頭の2件*しか通知されない。<br />
同梱によって3件以上が同時にインストールされうる場合は、[OnInstallCompleteEx](OnInstallCompleteEx.md)を使う事。

- **Reference0**: インストールした物の[※識別子](caption_install-identifier.md)。
- **Reference1**: インストールした物の名前（install.txtのname指定）。
- **Reference2**: インストールした物の名前2（ゴーストにバルーンを同梱した場合などのballoon側の名前）。

**対応:** Materia / SSP / CROW / Ninix
