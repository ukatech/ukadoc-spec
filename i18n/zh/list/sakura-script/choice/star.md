# `\*`

**カテゴリ:** Choice command

In a script containing this command, choices do not time out.<br />
This setting is effective only within the current script. It is also effective if written after the choice.

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[タイムアウトしない選択肢,NotTimeout]\*。選択時は通常通り、OnChoiceSelectExイベント(トークがなければOnChoiceSelectイベント)が発生する。
```
