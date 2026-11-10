# OnExtractArchiveComplete

**カテゴリ:** 其他事件

封存檔解壓縮成功完成時會發生。

如果在 [`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md) 中，透過 --event 選項指定的識別碼以 On 開頭，便會發生該識別碼的事件。否則便會發生本事件。

- **Reference0**: 透過 Sakura Script 的 --event 選項指定的事件識別碼。
- **Reference1**: 解壓縮的檔案數。
- **Reference2**: 壓縮後大小（位元組）。
- **Reference3**: 解壓縮後大小（位元組）。

**対応:** SSP 2.7.23
