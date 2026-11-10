# `\![raise,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

執行事件。<br />
第 3 個引數起會依序存入 Reference0 以後的欄位。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
このトークの末端にあるraiseが再生された時、SHIORIイベント「OnRaiseTest」がSSPから通知される。Reference0には「test」が入っている。\![raise,OnRaiseTest,test]
```
