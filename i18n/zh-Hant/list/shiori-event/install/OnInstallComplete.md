# OnInstallComplete

**カテゴリ:** 安裝事件

安裝成功完成時觸發。<br />
此事件屬於舊規格，因此單次安裝中同時安裝的項目只會通知*最前面的 2 件*。<br />
若透過同梱可能同時安裝 3 件以上，請使用 [OnInstallCompleteEx](OnInstallCompleteEx.md)。

- **Reference0**: 已安裝項目的[※識別碼](caption_install-identifier.md)。
- **Reference1**: 已安裝項目的名稱（install.txt 中指定的 name）。
- **Reference2**: 已安裝項目的名稱 2（例如將 balloon 同梱於 ghost 時，為 balloon 端的名稱）。

**対応:** Materia / SSP / CROW / Ninix
