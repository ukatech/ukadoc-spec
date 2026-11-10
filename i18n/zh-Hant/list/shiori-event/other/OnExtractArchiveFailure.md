# OnExtractArchiveFailure

**カテゴリ:** 其他事件

封存檔解壓縮失敗時會發生。

如果在 [`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md) 中，透過 --event 選項指定的識別碼以 On 開頭，便會發生名稱附加「Failure」的事件。否則便會發生本事件。

- **Reference0**: 透過 Sakura Script 的 --event 選項指定的事件識別碼。
- **Reference1**: 錯誤內容。請參閱[※錯誤代碼一覽](caption_archive_error_codes.md)。

**対応:** SSP 2.7.23
