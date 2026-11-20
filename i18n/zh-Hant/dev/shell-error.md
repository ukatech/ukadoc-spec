# 排除錯誤訊息

## 排除錯誤訊息

開發時，有時會遇到回報 SSP 出現這類錯誤的 bug 報告。<br />
本頁列出一些有助於排除錯誤訊息的參考資訊。<br />
這並非能徹底解決問題的手冊，但應該能提供一些提示。

## 目次

1. [～ 不存在。](shell-error.md#-存在していません)
2. [出現舊定義或新定義相關訊息](shell-error.md#旧定義新定義がどうこう言われた)

## ～ 不存在。

這是最常出現的錯誤。大多數情況是動畫 ID 寫錯或遺漏定義等容易修正的問題，但有些情況也可能難以處理。

### \[GHOST\]default(master) shell 不存在。

依照伺か (Ukagaka) 的規格，shell/master 資料夾是必要的，缺少時會產生相容性問題。<br />
但如果無論如何都不想製作 master shell，可以使用以下定義來迴避。

[seriko.defaultsurfacedirectoryname](../descript/ghost/descript-txt/seriko.defaultsurfacedirectoryname.md)

### \[SERIKO\]Surface=0(或10) 不存在。

依照伺か (Ukagaka) 的規格，編號0及10的 surface 會受到特殊處理，作為「預設 surface」，例如以 `\s` 標籤指定不存在的編號時會改為顯示它們。<br />
即使不考慮編號0，應該也有不少情況是不想製作編號10，這時請試著新增以下定義。

[sakura.seriko.defaultsurface](../descript/shell/descript-txt/sakura.seriko.defaultsurface.md)

[kero.seriko.defaultsurface](../descript/shell/descript-txt/kero.seriko.defaultsurface.md)

[char\*.seriko.defaultsurface](../descript/shell/descript-txt/char-star-.seriko.defaultsurface.md)

## 出現舊定義或新定義相關訊息

「使用舊定義時，卻使用了新的定義方式」<br />
「使用新定義時，卻使用了舊的定義方式」<br />
遇到這類錯誤訊息時，請參考以下內容。

[descript - version](../descript/shell-surfaces/descript-brace/version.md)

[關於 SERIKO 的舊定義與新定義](../descript/shell-surfaces/surface-brace/caption_seriko-redefine.md)

某些情況下，只要在 surfaces.txt 的最上方新增以下內容，就不會再出現錯誤。

```
descript
{
version,1
}
```
