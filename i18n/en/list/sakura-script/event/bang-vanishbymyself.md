# `\![vanishbymyself]`

**カテゴリ:** Event command

Uninstalls the current ghost without a request for permission to disappear.<br />
Note that this runs immediately without showing a confirmation dialog.<br />
Whether deletion occurs depends on the user's SSP settings.

The following options can be specified in SSP<br />
`\![vanishbymyself,ゴースト名]` Specifies which ghost to switch to after deletion (if it cannot be found, SSP selects one automatically as appropriate)<br />
`\![vanishbymyself,--option=query]` 2.5.82 : Displays a deletion confirmation dialog. This is the same as when run from the menu.

**対応:** Materia / SSP / Ninix

## 記述例

```
自分自身を削除。Send Boxからのサンプル入力での実行時は要注意。\![vanishbymyself]
```
