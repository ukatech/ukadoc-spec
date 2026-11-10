# `\![raise,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Executes an event.<br />
The third and subsequent arguments are stored in Reference0 onward, in order.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
このトークの末端にあるraiseが再生された時、SHIORIイベント「OnRaiseTest」がSSPから通知される。Reference0には「test」が入っている。\![raise,OnRaiseTest,test]
```
