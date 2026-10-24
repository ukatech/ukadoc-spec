# OnExecuteHTTPComplete

**カテゴリ:** その他通信イベント

execute-httpで正常に取得完了した際に発生。

- **Reference0**: post/get/head/put/delete のいずれか
- **Reference1**: --sync・--asyncオプションで指定した文字列。
- **Reference2**: 対象のURL。
- **Reference3**: --nofileオプションがある場合、取得したデータの中身。ただし改行コードはバイト値1に置き換えられている。<br />
  そうでない場合は取得したファイルのフルパス。
- **Reference4**: 取得結果コード。(timeout|fileio|200|204|403|404)等。[\[失敗理由\]](../network-update/caption_updateresultfailure.md)も参照。
- **Reference5**: Cookieの文字列。
- **Reference6**: 受け取ったすべてのレスポンスヘッダ。改行の代わりにバイト値1で区切られている。 \[2.6.40\]

**対応:** SSP / Ninix
