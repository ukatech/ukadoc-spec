# `\*`

**カテゴリ:** 選項命令

在記述此指令的腳本中，選項不會逾時。<br />
僅在該腳本中有效。即使寫在選項後面也有效。

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[タイムアウトしない選択肢,NotTimeout]\*。選択時は通常通り、OnChoiceSelectExイベント(トークがなければOnChoiceSelectイベント)が発生する。
```
