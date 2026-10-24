# OnExecuteFileWatchFailure

**カテゴリ:** その他通信イベント

[`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md)が失敗した際や、監視を続けられなくなった際に発生。この場合、その監視は解除される。

--asyncでOnから始まるIDを指定した場合は、そのIDの後ろにFailureをつけたイベント名になる。

- **Reference0**: --asyncで指定した文字列そのもの（無ければ空）
- **Reference1**: 指定したパスの文字列そのもの
- **Reference2**: 失敗の理由<br />
  notauthorized : SSTPなど外部から送られたスクリプトで監視しようとした<br />
  invalid : パスが指定されていない<br />
  notfound : 監視先のディレクトリ（ファイルの場合はそのファイルを置くディレクトリ）が無い、監視を始められない、または監視中に無くなった<br />
  limit : SSP全体で監視しているディレクトリの種類が上限（63）を超える

**対応:** SSP 2.8.91
