# `\f[name,フォント名]`

**カテゴリ:** Text change command

Changes the text font to the specified font name.<br />
If default is specified, or none of the specified font candidates are available, the font reverts to the balloon's standard font (or the balloon font override in SSP settings, if enabled).<br />
If disable is specified, the font is set to the same font used for disabled display.<br />
Font files placed under \[the folder of the ghost that ran\]/ghost/master or in the current balloon's folder can also be specified as font names.<br />
Multiple font names can be specified, separated by commas. They are selected from among the fonts installed automatically in the order listed (highest priority first) (SSP only).<br />

**対応:** SSP

## 記述例

```sakurascript
\f[name,メイリオ,meiryo.ttf]メイリオがインストール済みならメイリオ、そうでなければmeiryo.ttf、それもなければデフォルトフォントで表示される。
```
