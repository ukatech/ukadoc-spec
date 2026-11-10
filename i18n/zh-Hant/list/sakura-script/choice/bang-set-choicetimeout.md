# `\![set,choicetimeout,時間]`

**カテゴリ:** 選択肢コマンド

Specifies the timeout duration for choices. The unit is milliseconds.<br />
The countdown starts after all the talk has finished displaying.<br />
This setting is effective only for the current script. It is effective even if written after the choices.<br />
If a choice times out, the [OnChoiceTimeout](../../shiori-event/choice/OnChoiceTimeout.md) event occurs.

Omitting the duration resets it to the default value.<br />
A duration of 0 or -1 disables the timeout.

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[早押し,FastPush]\![set,choicetimeout,500]
```
