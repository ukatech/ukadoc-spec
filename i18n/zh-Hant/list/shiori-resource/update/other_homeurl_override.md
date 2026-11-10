# other_homeurl_override

**カテゴリ:** 更新資訊

在 `\![updateother]` 或 shell、balloon 同時更新功能中，強制替換更新目標的更新 URL（homeurl）。<br />
若不需要替換，請回傳 204 或空字串。

- **Reference0**: 更新目標的類型（shell、balloon、headline、plugin、language 等）
- **Reference1**: 更新目標的名稱（descript.txt 的 name）
- **Reference2**: 更新目標的作者名稱（descript.txt 的 craftmanname）
- **Reference3**: 更新目標的資料夾名稱。
- **Reference4**: 原本應用於更新的 homeurl。

**対応:** SSP 2.5.33
