# Dressup（MAYUNA）

## 概要

伺か（Ukagaka）的 shell 具有稱為 dressup 的機制。此機制可在單一 shell 中顯示或隱藏多個服裝等零件，也可切換其種類。

伺か（Ukagaka）的 shell 中，dressup 被視為動畫的一種。<br />
但與其他動畫不同，它不會逐格播放；動畫開始時，會立即合成所有影格（pattern）及基底 surface，之後便以靜態圖片處理（因此會忽略 pattern 定義中的權重參數）。<br />
這種「繪製結果彷彿與基底 surface 合而為一」的特性，非常適合用來表現服裝等物件。

dressup 作為動畫的開始與結束，主要透過切換 owner draw 選單中的 dressup 選單來控制。在 SSP 中，除此之外也可使用 Sakura Script 的[`\![bind]`](../../../list/sakura-script/surface/bang-bind.md)標籤，從 ghost 端進行控制。<br />
owner draw 選單的設定是在[descript.txt](../../shell/index.md)中進行，而非 surfaces.txt；請參閱該頁面。

另外，surfaces.txt 中與一連串動畫相關的規格稱為 MAYUNA。

## 基本格式與記述範例

```
surface0
{
// 服1の定義　アニメーションIDは0
animation0.interval,bind
animation0.pattern0,add,500,0,50,100

// 服2の定義　アニメーションIDは1
animation1.interval,bind
animation1.pattern0,add,501,0,50,100
}

//--- 以下着せ替えパーツ定義 ---
// 服1
surface500
{
element0,overlay,dress1.png,0,0
}

// 服2
surface501
{
element0,overlay,dress2.png,0,0
}
```

surfaces.txt 中的 dressup 定義例如如上所示。

上例在 surface0 中定義了「服1」與「服2」兩種 dressup。

與一般動畫定義相同，必須有 interval 定義與 pattern 定義。interval 定義指定 bind，即表示該動畫是 dressup 定義。

動畫的 pattern 定義會依影格數量逐一設定；但 dressup 是靜態圖片，因此合成的是所需數量的零件，而非影格。如同範例，若構成 dressup 的零件只有一個，pattern 行就只需一行。另外，dressup 的各零件會立即合成，因此會忽略權重參數。

pattern 定義的繪製方法將於後文說明。

## 可使用的繪製方法

在 MATERIA（伺か原版）中，可使用為 dressup 準備的 4 種方法，也就是「bind」「add」「reduce」「insert」。其中 bind 是舊規格，add 則與其向下相容。

在 SSP 中，也可在 dressup 使用部分原本為一般動畫準備的繪製方法。

有關 dressup 可使用的繪製方法等詳細資訊，請參閱[繪製方法](h-drowmethod/introduction_drawmethod.md)一節。

## interval 組合指定中的 bind

在 SSP 中，如[動畫間隔一節](h-animationinterval/introduction_animationinterval.md)所述，可以組合指定 interval。

當組合指定中包含 bind 時，動畫會失去 bind 單獨使用時原有的靜態圖片特性（pattern 定義中的權重參數不再被忽略）。不過動畫的持續時間不變，因此例如使用 bind+runonce 這類組合指定時，所有 pattern 繪製完成後的畫面會持續顯示，直到基底 surface 改變或 dressup 狀態變化為止。

因此，在包含 bind 的 interval 組合指定中，應在 pattern 定義的最後一行合成希望保留為靜態圖片的繪製結果，而不要結束動畫。

## 多重 dressup 定義（僅限 SSP）

若作為動畫影格參照的 surface 上也定義了該 surface 的動畫，通常會忽略這些動畫。

但在 SSP 中，只有 interval 為 bind 的動畫（即 dressup）不會被忽略，而會套用。

因此，對於會受到 dressup 影響的動畫結構，可以在動畫影格端設定對應 dressup 的定義。

另外，也可以將多重 dressup 巢狀套用，但會忽略循環參照。
