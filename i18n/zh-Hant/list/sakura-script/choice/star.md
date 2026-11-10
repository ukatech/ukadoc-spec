# `\*`

**カテゴリ:** 選択肢コマンド

Choices do not time out in scripts where this is written.<br />
This setting is effective only for the current script. It is effective even if written after the choices.

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[タイムアウトしない選択肢,NotTimeout]\*。選択時は通常通り、OnChoiceSelectExイベント(トークがなければOnChoiceSelectイベント)が発生する。
```
