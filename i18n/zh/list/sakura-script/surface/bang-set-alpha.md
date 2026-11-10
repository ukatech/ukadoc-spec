# `\![set,alpha,数値,オプション]`

**カテゴリ:** Surface command

Change the transparency of the current scope's surface from 0 to 100. 0 is fully transparent, and 100 is opaque. Values above 100 are clamped to 100. Negative values only redraw without changing the value.<br />
Options allow specifying the animation duration and waiting for it to complete.<br />
Effective until the ghost ends.

- --time=milliseconds……Animation duration (milliseconds). Defaults to 0 (applied immediately) if omitted or negative. Can also be specified as a positional parameter (for backward compatibility).
- --wait……Wait for the animation to complete before continuing script execution. If omitted, execution is asynchronous (continues to the next operation immediately). SSP 2.7.52 and later.

**対応:** SSP

## 記述例

```sakurascript
\0\![set,alpha,0]本体側が透明になり見えなくなる。\1\![set,alpha,50]相方側がだいたい半透明になる。
```

```sakurascript
\![set,alpha,50,--time=1000]1秒かけて透過度50へ変化する（非同期）。
```

```sakurascript
\![set,alpha,50,--time=2000,--wait]2秒かけて透過度50へ変化する（完了まで待機）。
```

```sakurascript
\![set,alpha,100,--time=1000,--wait]1秒かけて不透明に戻す（完了まで待機）。
```
