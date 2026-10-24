# other_homeurl_override

**カテゴリ:** 更新情報

`\![updateother]`やシェル・バルーン同時更新機能において、更新対象の更新先URL(homeurl)を強制的に置き換える。<br />
置き換える必要がない場合は、204を返すか空文字列とすること。

- **Reference0**: 更新対象の種類(shell,balloon,headline,plugin,languageなど)
- **Reference1**: 更新対象の名前(descript.txtのname)
- **Reference2**: 更新対象の作者名(descript.txtのcraftmanname)
- **Reference3**: 更新対象のフォルダ名。
- **Reference4**: 本来更新に使用すべきだったhomeurl。

**対応:** SSP 2.5.33
