# 動畫間隔

## 概要

在[animation\*.interval](../animation-star-.interval.md)中指定動畫運作的週期、時機（觸發條件）。

## 組合指定（SSP 擴充功能）

在 SSP 中，可以使用「+」分隔並列出多個動畫間隔，組合成一項指定。由於這項規格原本預期用於指定 dressup，因此即使不使用 bind 時看似正常運作，也要留意可能發生問題。

以下列出組合指定的範例。

- **bind+always**：dressup 開啟時，一律執行的動畫。
- **bind+runonce**：dressup 開啟時，切換至定義該 dressup 的 surface 時，或在顯示該 surface 期間開啟該 dressup 時，僅執行一次的動畫。
- **bind+random,頻度**：dressup 開啟時，每秒以 1/頻度 的機率觸發的動畫。
- **bind+periodic,間隔**：dressup 開啟時，每隔（間隔）秒觸發的動畫。
- **bind+runonce+random,5**：dressup 開啟時，切換至定義該 dressup 的 surface 時，或在顯示該 surface 期間開啟該 dressup 時，執行一次；之後每秒以五分之一的機率播放的動畫。

對 bind 使用「+」分隔並組合其他指定時，bind 間隔原有的「忽略 pattern 定義的權重參數，並與底圖 surface 合併為靜態圖像」等特性會消失。

此外，對 random、periodic、talk 等需要參數的指定，即使是組合指定，參數也要寫在最後。

以下是*錯誤*的寫法。

```
animation0.interval,random,5+bind
```

以下是*正確*的寫法。

```
animation1.interval,bind+random,5
```

不可組合帶有參數的間隔指定。
