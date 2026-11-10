# 排除錯誤訊息

## 排除錯誤訊息

開發時，偶爾會遇到回報 bug 時提到 SSP 出現這類錯誤的情況。<br />
本文列出一些有助於排除錯誤訊息的參考資訊。<br />
這不是一份能徹底解決問題的手冊，但希望能提供一些小提示。

## 目次

1. [～ 不存在。](shell-error.md#-存在していません)
2. [出現舊定義／新定義相關訊息](shell-error.md#旧定義新定義がどうこう言われた)

## ～ 不存在。

這是最常出現的錯誤。大多數情況是動畫 ID 寫錯，或是漏寫定義等，通常很容易修正，但也有一些較難處理的情況。

### \[GHOST\]default(master) shell 不存在。

根據伺か (Ukagaka) 規格，shell/master 資料夾是必要的，若不存在會造成相容性問題。<br />
不過，如果無論如何都不想建立 master shell，可以透過以下定義避開問題。

[seriko.defaultsurfacedirectoryname](../descript/ghost/descript-txt/seriko.defaultsurfacedirectoryname.md)

### \[SERIKO\]Surface=0（或10）不存在。

在伺か (Ukagaka) 規格中，0號與10號 surface 有特殊用途；例如使用`\s`標籤指定不存在的編號時，會改為顯示這些「預設 surface」。<br />
先不論0號，應該也有不少情況是不想建立10號 surface；請嘗試加入以下定義。

[sakura.seriko.defaultsurface](../descript/ghost/descript-txt/sakura.seriko.defaultsurface.md)

[kero.seriko.defaultsurface](../descript/ghost/descript-txt/kero.seriko.defaultsurface.md)

[char\*.seriko.defaultsurface](../descript/ghost/descript-txt/char-star-.seriko.defaultsurface.md)

## 出現舊定義／新定義相關訊息

如果遇到類似以下的錯誤訊息，請檢查下列項目。<br />
「使用舊定義時，卻使用了新的定義方式」<br />
「使用新定義時，卻使用了舊的定義方式」

[descript - version](../descript/shell-surfaces/descript-brace/version.md)

[SERIKO 舊定義與新定義](../descript/shell-surfaces/surface-brace/caption_seriko-redefine.md)

有時只要將以下內容加到surfaces.txt最上方，就能排除錯誤。

```
descript
{
version,1
}
```
