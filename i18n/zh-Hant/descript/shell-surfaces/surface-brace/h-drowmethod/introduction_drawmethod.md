# 描畫方法

## 概要

[animation pattern 定義](../animation-star-.pattern-star.md)與[element 定義](../element-star.md)中，各影格（元件）的合成與描畫方法。

除了合成影像之外，也有用來取代[基底 surface](../caption_basesurface.md)（base）、移動基底 surface（move），以及插入、執行其他動畫（insert、start、stop、alternativestart、alternativestop）等各種用途的方法。

## dressup 中描畫方法的處理方式

在 dressup 定義中，非影像合成的方法（move、insert、start、stop、alternativestart、alternativestop）無效（會以 overlay 處理）。但只有在最初的 pattern 中使用時，base 才有效，因此可以實現僅在 dressup 啟用時才取代基底 surface 的機制。

做為 dressup 專用方法實作的 add 和 bind，在實作上與 overlay 相同。在 dressup 中，這三者無論指定哪一個，效果都相同。

## element 定義中描畫方法的處理方式

在 element 定義中，非影像合成的方法（base、move、insert、start、stop、alternativestart、alternativestop）無效（會以 overlay 處理）。

其他 dressup 專用方法 add、bind 也無效（但由於 SSP 的實際實作會將無效的指定視為 overlay，因此結果仍會依照指定進行描畫）。

不言而喻，第一個 element（element0；若不存在surface\*.png，則後續項目也可能如此）所指定的描畫方法，大多數都等同於 base。但 asis 方法會讓透明色原樣顯示，這一點仍然有效。

此外，當由 element 合成的 surface 做為動畫元件使用時，element 合成的結果會視為一張影像處理。但請注意，這項實作自 SSP2.3.53 起才有；在此之前並未定義。

## 合成類方法在 element、動畫、dressup 中的差異與共通點

合成類方法在 element、動畫、dressup 中各自具有不同的意義。

element 定義的目的是取得一張做為基底 surface 的靜態影像。在 element 定義中，會在截至前一步的合成結果上繼續合成下一層，反覆進行，最後取得一張合成結果的靜態影像。

dressup 定義與 element 定義相同，也是取得靜態影像的機制，因此描畫方法的處理流程與 element 定義十分相似。在 dressup 的 pattern 定義中，會先將第一個 pattern 合成到基底 surface 上，之後再將下一層合成到截至前一步的合成結果上，反覆進行，最後取得一張合成結果的靜態影像。因此，dressup 的行為會如同與基底 surface 合而為一。

相較之下，非 dressup 的一般動畫是影片式表現，因此其流程與前兩者大不相同。動畫的各個 pattern 定義僅用來定義構成動畫的各個影格，彼此獨立。各個 pattern 定義會合成基底 surface 與新影像，產生新的影格，因此前一個 pattern 定義（前一個影格）的合成結果不會影響下一個影格。藉由如此接連描畫新的影格，便能實現影片式表現。

然而，在所有情況下，合成類方法都有一個共通點：負責合成「原始影像」與「新影像」這兩張影像。因此，ukadoc 為了方便說明描畫方法，將*「原始影像」*稱為*基底圖層*，將後者的*「新影像」*稱為*新圖層*。

換句話說，動畫的各個 pattern 定義會以基底 surface 做為基底圖層，合成新圖層來產生影格。相較之下，dressup 與 element 合成則是以截至前一步的合成結果做為基底圖層，反覆合成新圖層，最後取得一張靜態影像。

## 描畫方法與透明色

左上角 1 像素的顏色會做為透明色處理，實際顯示時，相同顏色的部分會呈現透明；這一點對於用於 pattern 定義的 surface，以及用於 element 定義的影像也相同。

此時合成的各張影像，其透明色的 RGB 值不必特別一致。

另外，各種描畫方法對透明色的處理各有特色，請參閱各項說明。

## 基底圖層與新圖層的偏移與重疊

將新圖層合成至基底圖層外部區域時（因影像大小或位置所致）的行為，取決於 baseware 的實作。

在 MATERIA 中，超出基底圖層的部分不會顯示。

在 CROW 中，若進行合成而超出基底圖層，便無法正確描畫。

在 SSP 中，允許合成超出基底圖層的新圖層；其行為是*在基底圖層中補上全透明區域，直到新圖層不再超出範圍*。

反過來說，新圖層外側的區域是*與全透明區域不同的空白區域*，合成時*不會發生任何變化，基底圖層的內容會原樣保留*。這是理解 replace 方法與 reduce 方法時，尤其需要注意的前提，因為這兩種方法中新圖層的全透明區域會影響合成結果。
