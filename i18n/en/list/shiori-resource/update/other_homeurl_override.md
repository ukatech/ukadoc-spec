# other_homeurl_override

**カテゴリ:** Update Information

In `\![updateother]` and the simultaneous shell/balloon update function, forcibly replace the update destination URL (homeurl) for the item being updated.<br />
If no replacement is needed, return 204 or an empty string.

- **Reference0**: Type of item being updated (shell,balloon,headline,plugin,language, etc.)
- **Reference1**: Name of the item being updated (name in descript.txt)
- **Reference2**: Author of the item being updated (craftmanname in descript.txt)
- **Reference3**: Folder name of the item being updated.
- **Reference4**: The homeurl that should originally have been used for the update.

**対応:** SSP 2.5.33
