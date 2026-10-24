# OnURLDropFailure

**カテゴリ:** URLドロップイベント

ドロップされたURLの受領に失敗したかキャンセルされた際に発生。<br />
このイベントはNARインストールを試行しようとして失敗した際に発生する。他(homeurlインストールやfeed(RSS)インストール)では発生しない。

- **Reference0**: ダウンロードし終わった分のファイルのローカルパス。
- **Reference1**: [※失敗理由](../network-update/caption_updateresultfailure.md)
- **Reference2**: ドロップされたURL。
- **Reference3**: ドロップされたキャラクターのスコープ番号。本体側0、相方1、3人目以降は2以降。

**対応:** Materia / SSP Ref2,3は2.6.36 / CROW
