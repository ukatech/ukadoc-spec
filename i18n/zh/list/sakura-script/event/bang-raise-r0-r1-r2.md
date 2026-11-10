# `\![raise,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

执行事件。<br />
第3个及之后的参数会依次存入Reference0及后续项。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
このトークの末端にあるraiseが再生された時、SHIORIイベント「OnRaiseTest」がSSPから通知される。Reference0には「test」が入っている。\![raise,OnRaiseTest,test]
```
