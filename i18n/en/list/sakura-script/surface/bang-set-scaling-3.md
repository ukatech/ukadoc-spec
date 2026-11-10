# `\![set,scaling,横倍率,縦倍率,オプション]`

**カテゴリ:** Surface command

Precisely set the surface's scale factors. The unit is %.<br />
Options allow you to specify an animation duration and wait for it to complete.

- --time=milliseconds……Animation duration in milliseconds. If omitted or negative, defaults to 0 (applied immediately). Can also be specified as a positional parameter (for backward compatibility).
- --wait……Wait for the animation to complete before continuing script execution. If omitted, execution is asynchronous (the next operation starts immediately). SSP 2.7.52 and later.

**対応:** CROW / SSP 2.7.31

## 記述例

```sakurascript
\![set,scaling,200,200,--time=2000]2秒かけて200%へ変化する（非同期）。
```

```sakurascript
\![set,scaling,200,200,--time=3000,--wait]3秒かけて200%へ変化する（完了まで待機）。
```

```sakurascript
\![set,scaling,100,100,--time=1000,--wait]1秒かけて等倍に戻す（完了まで待機）。
```
