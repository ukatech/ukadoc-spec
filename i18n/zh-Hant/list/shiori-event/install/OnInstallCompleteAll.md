# OnInstallCompleteAll

**カテゴリ:** 安裝事件

例如拖放多個 nar 時，安裝**全部**正常完成後，會在 OnInstallComplete/同 Ex 之後最後發生。<br />
SSP 在 2.9.00 之前的版本有實作遺漏，因此實際上不會發生。

- **Reference0**: 已安裝項目的[※識別碼](caption_install-identifier.md)。有多個項目時，以位元組值 1 分隔。
- **Reference1**: 已安裝項目的名稱。有多個項目時，以位元組值 1 分隔。
- **Reference2**: 安裝位置。有多個項目時，以位元組值 1 分隔。

**対応:** SSP 2.9.00 / Ninix
