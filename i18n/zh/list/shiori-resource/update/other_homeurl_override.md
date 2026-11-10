# other_homeurl_override

**カテゴリ:** Update information

In `\![updateother]` and the simultaneous shell/balloon update feature, forcibly replace the update destination URL (homeurl) for the update target.<br />
If no replacement is needed, return 204 or an empty string.

- **Reference0**: Type of update target (shell, balloon, headline, plugin, language, etc.)
- **Reference1**: Name of update target (name in descript.txt)
- **Reference2**: Author name of update target (craftmanname in descript.txt)
- **Reference3**: Folder name.
- **Reference4**: The homeurl that should originally have been used for the update.

**対応:** SSP 2.5.33
