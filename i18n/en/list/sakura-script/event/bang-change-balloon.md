# `\![change,balloon,バルーン名]`

**カテゴリ:** Event commands

Switches to the specified balloon.<br />
If the balloon does not exist, the command is ignored.<br />
After the change, the SHIORI event [OnBalloonChange](../../shiori-event/boot-close-change/OnBalloonChange.md) is notified.

Set the balloon name to lastinstalled to switch to the last installed balloon. This is invalid if SSP has been shut down since installation.<br />
Set the balloon name to random to switch to a random balloon.

\[SSP 2.9.35\] The balloon's [UUID](../../propertysystem/property-system/general-property/uuid.md) can also be specified instead of its name.

**対応:** SSP / Ninix

## 記述例

```sakurascript
SSPデフォルト+にバルーン変更。\![change,balloon,SSPデフォルト+]
```
