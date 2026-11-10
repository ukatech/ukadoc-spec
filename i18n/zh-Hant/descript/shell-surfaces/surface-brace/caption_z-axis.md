# 各元素的上下層級

## 上層與下層

以下將畫面前側稱為上層，畫面後側稱為下層。

## 各部件的上下層級

在element及dressup（間隔為bind的動畫）中，elementID・patternID較小者位於下層，較大者位於上層。

## 基礎surface與各動畫的上下層級

基礎surface基本上是所有合成內容中最底層的圖像，但指定了SSP的[background選項](animation-star-.option-2.md)的動畫，會合成在基礎surface下方（背面）。

包含dressup在內，各動畫之間的上下層級通常依動畫ID由大到小排列（編號較大的會配置在畫面前側）。但在SSP中，若在descript brace中定義[animation-sort](../descript-brace/animation-sort.md)，也可以改為由小到大排列。

## 命中判定（collision）的上下層級

某個surface的命中判定，基本上以surfaces.txt中先出現的collision定義為上層。但在SSP中，若在descript brace中定義[collision-sort](../descript-brace/collision-sort.md)，也可以依collisionID設定為由小到大或由大到小排列。

此外，在SSP中，可以透過[animation\*.collision](animation-star-.collision-star.md)的設定，設定僅在特定動畫顯示時才有效的命中判定。這種情況下會先考量各動畫的上下層級，再依照一般順序評估各動畫與基礎surface的命中判定。

以下以animation-sort設定為descend為例，從上層到下層依序整理如下：

1. ID較大的普通動畫中，較上層的命中判定
2. ID較大的普通動畫中，較下層的命中判定
3. ID較小的普通動畫中，較上層的命中判定
4. ID較小的普通動畫中，較下層的命中判定
5. 基礎surface中，較上層的命中判定
6. 基礎surface中，較下層的命中判定
7. ID較大的附有background選項的動畫中，較上層的命中判定
8. ID較大的附有background選項的動畫中，較下層的命中判定
9. ID較小的附有background選項的動畫中，較上層的命中判定
10. ID較小的附有background選項的動畫中，較下層的命中判定

（此處的動畫也包含dressup）。
