# OnExecuteRSSComplete

**カテゴリ:** その他通信イベント

`\![execute,rss-get/post]`で正常に取得完了した際に発生。

\[2.8.92\] どの項目がいくつ並ぶかは[RSS絞り込みオプション](../../sakura-script/misc/notes_executerss.md)で決まる。

- **Reference0～**: タイトル \[`\1`\] URL \[`\1`\] 更新日時（フォーマットはカンマ区切り：年,月,日,時,分,秒）\[`\1`\] 作者名 \[`\1`\] 内容または要約<br />
  更新がある時はRSSの要素数分Reference0,1,2～と続く<br />
  \[`\1`\]はバイト値1

**対応:** SSP 作者名・内容 2.4.10～
