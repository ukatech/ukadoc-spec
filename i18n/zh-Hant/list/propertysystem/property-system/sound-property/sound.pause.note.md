# 關於寫入音效屬性 \[2.8.72\]

音效屬性中，[position](sound.position.md)、[playing](sound.playing.md) 和 [pause](sound.pause.md) 支援透過[`\![set,property,～]`](../../../sakura-script/property-system-operation/bang-set-property.md)寫入。其他音效屬性皆為唯讀。

寫入時會轉換為對應的 Sakura Script 標籤，並以相同方式執行。因此，結果與直接寫入標籤完全相同；指定無效時（例如對已停止的媒體寫入 pause），也會和標籤一樣不會有任何動作。

轉換後的標籤會以元素名稱指定目標，因此若有多個媒體使用相同的元素名稱，即使透過[index(ID)](../currentghost.sound.index-ID.md)指定目標，寫入仍會作用於元素名稱相符的最新媒體。請注意，讀取與寫入的目標可能不同。

此外，寫入會以非同步方式執行，因此即使在寫入後立即讀取相同屬性，結果也可能尚未反映。
