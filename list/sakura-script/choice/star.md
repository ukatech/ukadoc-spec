# `\*`

**カテゴリ:** 選択肢コマンド

これが記述されたスクリプトでは、選択肢はタイムアウトされない。<br />
そのスクリプト中のみ有効。選択肢より後ろに書いても有効。

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[タイムアウトしない選択肢,NotTimeout]\*。選択時は通常通り、OnChoiceSelectExイベント(トークがなければOnChoiceSelectイベント)が発生する。
```
