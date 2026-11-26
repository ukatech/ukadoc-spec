# icon.interval,播放間隔

**カテゴリ:** descript.txt

[icon](icon.md)指定的動畫圖片（ANI・GIF・APNG・WebP）的播放時機。
可指定的值與[\![set,tasktrayicon]](../../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)的 --interval 相同（always・runonce・runcount,N・never・rarely・sometimes・random,N・periodic,N）。在 descript.txt 中可直接寫成 `icon.interval,random,5`。

未指定時，遵循檔案所含的循環次數。播放結束後會停在最後一格。
不適用於以標籤（`\![set,tasktrayicon]`）指定的圖示（僅使用標籤的 --interval）。

**既定値:** 無值（遵循檔案所含的循環次數）

**対応:** SSP 2.9.40
