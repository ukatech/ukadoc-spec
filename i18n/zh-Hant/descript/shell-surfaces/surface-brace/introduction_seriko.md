# 動畫（SERIKO）

## 概要

伺か（Ukagaka）的 shell 具有動畫功能。這是透過連續繪製靜止影像的影格，呈現類似影片的效果。

動畫是針對各個 surface 設定的。動畫各影格使用的影像也同樣是另一個 surface。此時，即使被引用為影格的 surface 另有動畫定義，通常也會忽略（但僅限 SSP，另有稱為多重 dressup 的機制。請參閱[dressup](introduction_mayuna.md)一節）。

設定各個 surface 時，必須定義動畫本身何時開始、各影格使用哪個 surface，以及以何種方式和時間間隔繪製等內容。

另外，surfaces.txt 中一系列與動畫相關的規格，稱為 SERIKO。

## 基本格式與記述例

```
surface0
{
// 瞬き
animation0.interval,rarely
animation0.pattern0,overlay,101,700,200,100
animation0.pattern1,overlay,102,700,200,100
animation0.pattern2,overlay,101,700,200,100
animation0.pattern3,overlay,-1,700,0,0

// トークに合わせて口を動かす
animation10.interval,talk,2
animation10.pattern0,overlay,200,700,200,120
animation10.pattern1,overlay,201,700,200,120
animation10.pattern2,overlay,202,700,200,120
animation10.pattern3,overlay,-1,700,0,0
}
```

surfaces.txt 中的動畫定義例如如下所示。

以上是在 surface0 上定義「眨眼」和「配合對話動嘴」這兩個動畫。

所有動畫定義都包含 interval 定義和 pattern 定義。此外還有選項定義，以及 SSP 專用的動畫觸碰判定定義，但這些都可以省略；interval 定義則不可省略，而且必須出現在一系列動畫定義的開頭。pattern 定義也至少必須有一個。

[interval 定義](animation-star-.interval.md)用來設定動畫何時播放。上例中出現了「rarely」、「talk」和「never」三種指定。詳情請參閱[動畫間隔一節](h-animationinterval/introduction_animationinterval.md)；大意是「眨眼」動畫偶爾播放，而「配合對話動嘴」動畫則會在角色每說兩個字時播放。

[pattern 定義](animation-star-.pattern-star.md)用來設定動畫的各個「影格」。其中設定該影格的繪製方法（請參閱[繪製方法](h-drowmethod/introduction_drawmethod.md)一節）、顯示前的等待時間，以及相對於下方影格要移動多少位置來繪製。只要準備所需數量的影格即可。pattern\* 的 \* 中的數字是從 0 開始的連續編號。

## 各動畫之間的關係

所有動畫都有 ID（具體指定方式請參閱 animation\*.interval 一節）。

同一個 surface 內不可有重複的 ID；而在不同 surface 之間，具有相同 ID 的動畫預期應代表相同意義。例如，角色有面向正面的 surface0 和面向側面的 surface1，並且兩者都設定了「眨眼」動畫。由於角色姿勢不同，實際用來呈現眨眼的影格影像應該不同，但兩個 surface 仍應使用相同的動畫 ID。尤其在後述的[dressup](introduction_mayuna.md)中，這種 ID 與意義之間的關聯是必要的。

所有不同的動畫基本上彼此獨立，並會非同步地開始和結束。<br />
例如，眨眼動畫和配合對話移動嘴部的動畫，應該各自開始和結束，而不必在意另一個動畫是否正在播放；只要定義為 ID 不同的動畫，實際上也會如此運作。

另一方面，也提供了透過 start 或 alternativestart 等用來執行其他動畫的特殊繪製方法，讓動畫本身成為執行其他動畫的觸發條件。<br />
此外，也可以指定 exclusive 選項來執行互斥動畫。
