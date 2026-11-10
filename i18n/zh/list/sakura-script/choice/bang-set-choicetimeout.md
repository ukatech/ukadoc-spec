# `\![set,choicetimeout,時間]`

**カテゴリ:** 选项命令

指定选项的超时时间。单位为毫秒。<br />
计时从对话显示完毕后开始。<br />
仅在当前脚本中有效。写在选项之后也有效。<br />
选项超时时，将触发[OnChoiceTimeout](../../shiori-event/choice/OnChoiceTimeout.md)事件。

省略时间：恢复默认值<br />
时间指定为0或-1：不超时

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[早押し,FastPush]\![set,choicetimeout,500]
```
