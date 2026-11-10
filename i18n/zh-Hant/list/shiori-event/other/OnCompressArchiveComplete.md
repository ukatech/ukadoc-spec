# OnCompressArchiveComplete

**カテゴリ:** 其他事件

封存檔壓縮順利完成時觸發。

透過 [`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md) 的 --event 選項指定的識別碼若以 On 開頭，便會觸發該識別碼所代表的事件。否則會觸發本事件。

- **Reference0**: Sakura Script 的 --event 選項所指定的事件識別碼。
- **Reference1**: 壓縮的檔案數。
- **Reference2**: 壓縮後的大小（位元組）。
- **Reference3**: 未壓縮的大小（位元組）。

**対応:** SSP 2.7.23
