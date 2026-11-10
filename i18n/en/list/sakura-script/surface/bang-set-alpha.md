# `\![set,alpha,数値,オプション]`

**カテゴリ:** Surface command

Set the transparency of the current scope's surface to a value from 0 to 100. 0 is fully transparent, and 100 is opaque. Values above 100 are clamped to 100. Negative values redraw the surface without changing its value.<br />
Options allow you to specify an animation duration and wait for it to complete.<br />
Effective until the ghost ends.

- --time=milliseconds……Animation duration in milliseconds. If omitted or negative, defaults to 0 (applied immediately). Can also be specified as a positional parameter (for backward compatibility).
- --wait……Wait for the animation to complete before continuing script execution. If omitted, execution is asynchronous (the next operation starts immediately). SSP 2.7.52 and later.

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
