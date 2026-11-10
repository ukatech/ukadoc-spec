# other_homeurl_override

**カテゴリ:** 更新信息

在 `\![updateother]` 或 shell/balloon 同时更新功能中，强制替换更新目标的更新 URL（homeurl）。<br />
如果不需要替换，请返回 204 或空字符串。

- **Reference0**: 更新目标的类型（shell、balloon、headline、plugin、language 等）
- **Reference1**: 更新目标的名称（descript.txt 中的 name）
- **Reference2**: 更新目标的作者名（descript.txt 中的 craftmanname）
- **Reference3**: 更新目标的文件夹名称。
- **Reference4**: 原本应当用于更新的 homeurl。

**対応:** SSP 2.5.33
