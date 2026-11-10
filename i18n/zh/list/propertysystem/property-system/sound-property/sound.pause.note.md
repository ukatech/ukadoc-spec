# 关于声音属性的写入 \[2.8.72\]

声音属性中，[position](sound.position.md)、[playing](sound.playing.md)、[pause](sound.pause.md)支持通过[`\![set,property,～]`](../../../sakura-script/property-system-operation/bang-set-property.md)写入。其他声音属性均为只读。

写入会转换为与之对应的 Sakura Script 标签，并按相同方式执行。因此，结果与直接写入标签完全相同；指定无效时（例如向已停止的媒体写入 pause），也与标签一样不会产生任何效果。

由于转换后的标签通过元素名指定目标，如果存在多个元素名相同的媒体，即使通过[index(ID)](../currentghost.sound.index-ID.md)指定目标，写入也会应用于元素名匹配的最新媒体。请注意，写入目标有时会与读取目标不同。

此外，写入是异步执行的，因此写入后立即读取同一属性时，结果可能尚未更新。
