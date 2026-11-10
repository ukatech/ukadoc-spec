# `\![set,scaling,横倍率,縦倍率,オプション]`

**カテゴリ:** Surface command

Precisely change the surface's scaling factor. The unit is %.<br />
Options can specify the animation duration and whether to wait for it to finish.

- --time=milliseconds……Animation duration in milliseconds. If omitted or negative, the value is 0 (applied immediately). Can also be specified as a positional parameter (for backward compatibility).
- --wait……Wait for the animation to finish before continuing script execution. If omitted, execution is asynchronous (the next operation begins immediately). SSP 2.7.52 and later.

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
