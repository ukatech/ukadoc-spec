# `\![set,choicetimeout,時間]`

**カテゴリ:** Choice command

Specifies the choice timeout duration. The unit is milliseconds.<br />
The timer starts after all the talk has finished displaying.<br />
This applies only within the current script. It also applies if written after the choice.<br />
If the choice times out, the [OnChoiceTimeout](../../shiori-event/choice/OnChoiceTimeout.md) event occurs.

Omit the duration: returns to the default value<br />
Duration is 0 or -1: no timeout

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[早押し,FastPush]\![set,choicetimeout,500]
```
