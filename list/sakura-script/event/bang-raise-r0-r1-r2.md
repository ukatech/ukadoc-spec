# `\![raise,イベント名,r0,r1,r2...]`

**カテゴリ:** イベントコマンド

イベントを実行する。<br />
第3引数以降はReference0以降に順番に格納される。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
このトークの末端にあるraiseが再生された時、SHIORIイベント「OnRaiseTest」がSSPから通知される。Reference0には「test」が入っている。\![raise,OnRaiseTest,test]
```
